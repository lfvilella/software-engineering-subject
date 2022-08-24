from types_ import NUMBER_TYPE, NUMBERS_TYPE


def validate_number(number: NUMBER_TYPE):
    if not isinstance(number, (int, float)):
        raise ValueError(f"The item '{number}' should be a number "
                         f"not '{type(number)}'")


def validate_numbers(numbers: NUMBERS_TYPE):
    if not isinstance(numbers, list):
        raise ValueError("The param 'numbers' should be list of numbers")
    if not numbers:
        raise ValueError("The param 'numbers' cannot be empty")
    for item in numbers:
        validate_number(item)
