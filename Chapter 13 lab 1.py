#Chad Collard
#Chapter 13 Lab 1
#Recursion
#7/15/2025

def main():
    character = str(input("What character would you like to repeat? " ))
    times = int(input(f"How many {character}'s would you like: "))
    characters(times, character)

def characters(times, character):
    if times > 0:
        print(f'{character}')
        characters(times - 1, character)

if __name__== "__main__":
    main()


