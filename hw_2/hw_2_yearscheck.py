name = input("Enter your name: ")
print("Your name contains the letter 'a'.") if 'a' in name.lower() else print("Your name does not contain the letter 'a'.")
age = int(input('Enter your age: '))
print('A number of your age is even.') if not age % 2 else print('A number of your age is odd.')
if not age % 3 and 'w' in name:
    print('This year will happy for you!')
if not age % 10 - 9:
    print('Your anniversary is coming soon!')