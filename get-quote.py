import random

def main():

    # Open the file and read in all the lines
    f = open("quotes.txt")
    quotes = f.readlines()
    f.close()

    # Select a line at random
    last = len(quotes) - 1
    rnd = random.randint(0, last)

    # Print the selected line
    print(quotes[rnd])

if __name__== "__main__":
    main()
