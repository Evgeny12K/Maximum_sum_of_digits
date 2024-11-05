def sum_of_digits(number):
    """Возвращает сумму цифр числа."""
    return sum(int(digit) for digit in str(abs(number)))

def main():
    max_number = None
    max_digit_sum = 0

    print("Введите целые числа (введите 0 для завершения):")

    while True:
        try:
            number = int(input())
        except ValueError:
            print("Пожалуйста, введите целое число.")
            continue

        if number == 0:
            break

        digit_sum = sum_of_digits(number)
        if digit_sum > max_digit_sum:
            max_digit_sum = digit_sum
            max_number = number

    if max_number is not None:
        print(f"Число с максимальной суммой цифр: {max_number}")
    else:
        print("Ни одно число не было введено.")

if __name__ == "__main__":
    main()