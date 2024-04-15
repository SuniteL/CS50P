question = input("What is the Answer to the Great Question of Life, the Universe and Everything? ")

case = question.casefold()
deep = case.strip()

if deep == "42":
    print("Yes")
elif deep == "forty-two":
    print("Yes")
elif deep == "forty two":
    print("Yes")
else:
    print("No")
