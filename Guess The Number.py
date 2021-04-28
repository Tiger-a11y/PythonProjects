# Exercise 3 :- Guess the number
# Key points :- 1. no of guesses 9
#               2. no of guesses left
#               3. no of guesses he took to finish
#               4. Game over
N = 18
x = 1
print("Number of guesses is limited to only 9 times: ")
while x <= 9:
    n = int(input("Guess the number :\n"))
    if n < N:
        print("enter greater number.\n")
    elif n > N:
        print("enter lesser number.\n ")
    else:
        print(" !! HIT The No !!\n")
        print(x, "no.of guesses he took to finish.")
        break
    print(9 - x, " guesses left")
    x = x + 1

if x > 9:
    print("Game Over")
