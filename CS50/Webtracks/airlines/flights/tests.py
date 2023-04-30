from django.test import TestCase, Client
from .models import Flight, Airport, Passenger

# Create your tests here.
class FlightTest(TestCase):
    def setUp(self):
        a = Airport.objects.create(code="A", city="City A")
        b = Airport.objects.create(code="B", city="City B")

        Flight.objects.create(origin = a, destination = b, duration = -100)
        Flight.objects.create(origin = a, destination = a, duration = 100)
        Flight.objects.create(origin = a, destination = b, duration = 100)

    def test_departures(self):
        a = Airport.objects.get(code="A")
        self.assertEqual(a.departures.count(), 3)

    def test_arrivals(self):
        a = Airport.objects.get(code="A")
        self.assertEqual(a.arrivals.count(), 1)

    def test_valid_flight_destination(self):
        a = Airport.objects.get(code="A")
        b = Airport.objects.get(code="B")
        f = Flight.objects.get(origin = a, destination = a, duration = 100)
        self.assertFalse(f.is_valid_flight())

    def test_valid_flight_duration(self):
        a = Airport.objects.get(code="A")
        b = Airport.objects.get(code="B")
        f = Flight.objects.get(origin = a, destination = b, duration = -100)
        self.assertFalse(f.is_valid_flight())
        
    def test_valid_flight(self):
        a = Airport.objects.get(code="A")
        b = Airport.objects.get(code="B")
        f = Flight.objects.get(origin = a, destination = b, duration = 100)
        self.assertTrue(f.is_valid_flight())

    def test_index(self):
        c = Client()
        response = c.get("/flights/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["flights"].count(), 3)

    def test_flight_page(self):
        a = Airport.objects.get(code="A")
        f = Flight.objects.get(origin=a, destination=a)
        c = Client()
        response = c.get(f"/flights/{f.id}")
        self.assertEqual(response.status_code, 200)