import random

def get_integer_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("You should enter valid number.")

def main():
    print("Welcome to infer an input number.")

    n = get_integer_input("Enter minimum number: ")
    m = get_integer_input("Enter maximum number: ")

    while n > m:
        print("It is invalid input. You should enter them again.")
        n = get_integer_input("Enter minimum number: ")
        m = get_integer_input("Enter maximum number: ")

    secret_number = random.randint(n,m)

    print(f"\n Please infer a number between {n} and {m}. You have ten trials.")

    for attempt in range(1,11):
        guess = get_integer_input(f"Trial: {attempt}/10: ")

        if guess == secret_number:
            print(f"Congradurations! You get right number in {attempt} times.")
            break
        elif guess < secret_number:
            print("You should enter bigger number.")
        
        elif guess > secret_number:
            print("You should enter lesser number.")

        if attempt == 10:
            print(f"残念、10回試しても正解しませんでした。正解は {secret_number} でした。")

if __name__ == '__main__':
    main()
