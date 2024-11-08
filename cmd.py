def is_palindrome(input_str):
    return input_str == input_str[::-1]

def all_lowercase(input_str):
    return input_str.islower()

def all_digits(input_str):
    return input_str.isdigit()

def length_check(input_str, threshold=10):
    return len(input_str) > threshold

def empty_check(input_str):
    return len(input_str) == 0

def main():
    while True:
        print("\nSelect an option:")
        print("1. Palindrome Check")
        print("2. Lowercase Check")
        print("3. Digit Check")
        print("4. Length Check")
        print("5. Empty Check")
        print("6. Exit Program")
        
        choice = input("Enter your choice (1-6): ")

        if not choice.isdigit() or (int(choice) < 1 or int(choice) > 6):
            print("Invalid choice. Please enter a number between 1 and 6.")
            continue

        if choice == '6':
            print("Exiting the program.")
            break
        
        user_input = input("Enter a string to check: ")

        if choice == '1':
            if is_palindrome(user_input):
                print("The string is a palindrome.")
            else:
                print("The string is not a palindrome.")
        
        elif choice == '2':
            if all_lowercase(user_input):
                print("All characters are lowercase.")
            else:
                print("Not all characters are lowercase.")
        
        elif choice == '3':
            if all_digits(user_input):
                print("All characters are digits.")
            else:
                print("Not all characters are digits.")
        
        elif choice == '4':
            threshold = int(input("Enter the length threshold: "))
            if length_check(user_input, threshold):
                print(f"The string length exceeds {threshold} characters.")
            else:
                print(f"The string length does not exceed {threshold} characters.")
        
        elif choice == '5':
            if empty_check(user_input):
                print("The string is empty.")
            else:
                print("The string is not empty.")

if __name__ == "__main__":
    main()
