def main():
    what_are_the_odds(int(input("Please choose a number: ")))


def what_are_the_odds(n):
    total = 0
    number_list = list(range(n+1))
    for num in number_list:
        if num % 2 != 0:
            total += num
    print(f"The sum of all odd numbers between 1 and {n} is {total}.")


if __name__ == '__main__':main()
