import random


def primary():
    # print("Keep it logically awesome.")

    f = open("quotes.txt")
    quotes = f.readlines()
    f.close()

    last = 13
    rnd = random.randint(0, last)

    # Note If you want to add or remove quotes from your text file, you could change the last
    # variable to update automatically:
    # last = len(quotes) - 1

    # print(quotes[0])
    # print(quotes[13])
    print(quotes[rnd])


if __name__ == "__main__":
    primary()
