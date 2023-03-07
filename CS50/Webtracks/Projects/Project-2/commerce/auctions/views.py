from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import ListForm

from .models import User, Listing, Bids, Comments

def index(request):    
    listings = Listing.objects.all()
    return render(request, "auctions/index.html", {
        "listings": listings
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


@login_required
def create_listing(request):
    if request.method == "POST":
        form = ListForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            bid = form.cleaned_data["bid"]
            description = form.cleaned_data["description"]
            category = form.cleaned_data["category"]

            if img_url := form.cleaned_data["img_url"]:
                img_url = img_url
            listing = Listing(
                user=request.user, 
                title=title, bid=bid, 
                description=description, 
                img_url=img_url, 
                category=category)
            listing.save()
            return HttpResponseRedirect(reverse(f"listings", args=(listing.id,)))
        else:
                render(request, "auctions/create_listing.html",{
                    "form": form
                })

    return render(request, "auctions/create_listing.html", {
        "form": ListForm()
    })

def listings(request, n):

    listing = Listing.objects.get(pk=n)
    message = None
    CU = False
    winner = False
    if request.method == "POST":
        bid_amount = int(request.POST["bid_amount"])
        if bid_amount > listing.bid:
            b = Bids(user=request.user, listing=listing, bid=bid_amount)
            b.save()
        else:
            message = "Your bid is less than the intial price!"
    if request.user == listing.user:
        CU = True
    if request.user.id == listing.winner_pk:
        winner = True
    return render(request, "auctions/listings.html", {
        "listing": listing,
        "message": message,
        "comments": Comments.objects.filter(listing=listing),
        "current_user": CU,
        "winner": winner
    })

def deactivate(request, id):
    listing = Listing.objects.get(pk=id)
    listing.active = False
    listing.save()
    bids = Bids.objects.filter(listing=listing)
    max_bid = bids.first()
    for b in bids:
        if b.bid > max_bid.bid:
            max_bid = b
    listing.winner_pk = max_bid.user.id
    listing.save()
    return HttpResponseRedirect(reverse("listings", args=(id,)))

@login_required()
def add_watchlist(request, id):
    listing = Listing.objects.get(pk=id)
    request.user.watchlist.add(listing)
    return HttpResponseRedirect(reverse("watchlist"))

@login_required()
def remove_watchlist(request, id):
    listing = Listing.objects.get(pk=id)
    request.user.watchlist.remove(listing)
    return HttpResponseRedirect(reverse("watchlist"))


def watchlist(request):
    watch_list = request.user.watchlist.all()
    return render(request, "auctions/watchlist.html", {
        "watchlist": watch_list
    })


def categories(request):
    if request.method == 'POST':
        filter = request.POST["filter"]
        listings = Listing.objects.filter(category=filter)
        return render(request, "auctions/index.html", {
            "listings": listings
        })

    _ = Listing.objects.values('category')
    cat_list = set([ i["category"] for i in _ ])
    return render(request, "auctions/categories.html",{
        "categories": cat_list,
    })

def comment(request):
    if request.method == "POST":
        text = request.POST["comment"]
        listing_id=int(request.POST["listing"])
        listing = Listing.objects.get(pk=listing_id)
        c = Comments(user=request.user, listing=listing, comment=text)
        c.save()
        return HttpResponseRedirect(reverse("listings", args=(listing.id,)))
