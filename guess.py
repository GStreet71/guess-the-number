from random import randint
from colorama import Fore, Style

def get_num():
    num = randint(1, 1000001)
    return num

def main():
    get_num()
    num = get_num()
    count = 0
    while True:
        try:
            guess = int(input(Fore.CYAN + "What is your guess?: "))
        except ValueError:
            print("Input a valid number.")
            continue
        if guess >= 0 and guess > num:
            count += 1
            print(Fore.YELLOW + "Too high. Guess lower.")
            continue
        elif guess >= 0 and guess < num:
            count += 1
            print(Fore.RED + "Too low. Guess higher.")
            continue
        elif guess == num:
            count +=1
            print(Fore.BLUE + f"Correct!\n\nIt took you {count} guesses to get it correct!")
            break
        else:
            print(Fore.MAGENTA + "You found the secret quit" + Style.RESET_ALL)
            exit()

print(Fore.CYAN + "One-Million-To-One\n")
main()
