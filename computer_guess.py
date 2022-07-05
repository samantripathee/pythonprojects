import random
def to_guess(upper,lower):
    confirm = ""   
    while (confirm.lower() != 'c'):
        guess = random.randint(upper,lower)
        print(f"My guess is {guess}")
        confirm = input("Was my guess too low(l) or too high(h) or correct(c)? ")
        if confirm.lower() == "h":
            upper = guess
        elif confirm.lower() == "l":
            lower = guess
        print("Yay! Congratulations ME!!")
        
        
x,y = input("Enter the range at which the number falls(Upper,Lower): ").split(",")
to_guess(int(x),int(y))