def sum_of_digits(number):
    return sum(int(digit) for digit in str(abs(number)))

def main(numbers):
    max_number = None
    max_digit_sum = 0

    print("Вводимые целые числа:")

    for number in numbers:
        digit_sum = sum_of_digits(number)
        if digit_sum > max_digit_sum:
            max_digit_sum = digit_sum
            max_number = number

    if max_number is not None:
        print(f"Число с максимальной суммой цифр: {max_number}")
    else:
        print("Ни одно число не было введено.")

if __name__ == "__main__":
    main([15, 29, 8, 0])
