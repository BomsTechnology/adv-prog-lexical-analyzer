
def parse_number_list(input_str):
    """
    Parses and validates a list of numbers in the format: [number, number, ...]
    Returns a list of numbers if valid, otherwise raises ValueError.
    """
    input_str = input_str.strip()
    if not (input_str.startswith('[') and input_str.endswith(']')):
        raise ValueError("Input must start with '[' and end with ']'.")
    # Remove brackets
    numbers_str = input_str[1:-1].strip()
    if not numbers_str:
        raise ValueError("No numbers provided inside the brackets.")
    # Split numbers
    number_tokens = [token.strip() for token in numbers_str.split(',')]
    numbers = []
    for token in number_tokens:
        if not token:
            raise ValueError("Empty value detected between commas.")
        try:
            number = float(token)
            numbers.append(number)
        except ValueError:
            raise ValueError(f"Invalid number detected: '{token}'")
    return numbers

def get_user_input():
    """
    Accepts user input for a list of numbers.
    """
    print("Enter the numbers in the format: [number1, number2, ...]")
    return input("Numbers: ")

def main():
    """
    Main function to drive the lexical analyzer and average calculator.
    """
    try:
        user_input = get_user_input()
        numbers = parse_number_list(user_input)
        if len(numbers) == 0:
            print("Error: No numbers provided.")
        else:
            average = sum(numbers) / len(numbers)
            print(f"Average is {average}")
    except ValueError as av:
        print(f"Input Error: {av}")

if __name__ == "__main__":
    # Test cases:
    # 1. Valid input: [5, 8, 12, 4, 10]
    # 2. Invalid input: [5, , 10]
    # 3. Invalid format: 5,8,10
    # 4. Empty input: []
    main()