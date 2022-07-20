greet = input("Greeting: ").strip().lower().split(" ")
first_word = greet[0]
if first_word == 'hello' or first_word == 'hello,':
    print("$0")
elif 'h' == first_word[0] :
    print("$20")
else:
    print("$100")