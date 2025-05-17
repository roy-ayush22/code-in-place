import random

a = random.randint(10,99)
b = random.randint(10,99)

right_ans = int(a) + int(b)

def main():
    print("Khansole Academy")
    print(f"What is {a} + {b}?")
    answer = input(f"Your answer: ")

    if int(answer) == int(right_ans):
        print("Correct!")
    else:
        print("Incorrect.")
        print(f"The expected answer is {right_ans}")

    
if __name__ == '__main__':
    main()
