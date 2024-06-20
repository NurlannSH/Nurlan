def histogram(numbers):
    for num in numbers:
        print('*' * num)

numbers = list(map(int, input("Enter numbers separated by space: ").split()))
histogram(numbers)