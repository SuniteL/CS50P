def hello(to="world"):
    print("Hello,", to)

hello()
# Ask user for their name?
name = input("What's your name? ").strip().title() 
hello(name)