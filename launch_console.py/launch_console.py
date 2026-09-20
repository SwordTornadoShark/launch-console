name = input("What's your name? ")
print("Welcome to " + "name" + "'s Launch Console!")

running = True
while running:
    print("1) I am a Sophmore")
    print("2) I want to learn how to make my own application using python")
    print("3) Exit")
    choice = input("Pick 1-4: ")
    if choice == "1":
        print("I'm a builder-in-training at Code2College.")
    elif choice == "2":
        print("My goal: ship my first real project this term.")
    elif choice == "3":
        print("My favorite project was the text based hang man.")
    elif choice == "4":
        print("Goodbye!")
        running = False
    else:
        print("Please pick 1, 2, 3, or 4.")
