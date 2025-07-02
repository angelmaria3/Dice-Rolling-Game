import random
p=True
while p:
    ch=input("Roll the dice? (Y/N):").strip().lower()
    if ch=="y":
        n1=random.randint(1,6)
        n2=random.randint(1,6)
        print(f'({n1}, {n2})')
    elif ch=="n":
        print("Thanks for playing!")
        break
    else:
        print("Invalid choice")
