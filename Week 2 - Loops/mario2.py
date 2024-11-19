def main():
    print_square(3)

#for each row in suqare
def print_square(size):
    
    # For each brick in row
    for i in range(size):

        # Print brick
        for j in range(size):
            print("#", end="")
        print()

main()