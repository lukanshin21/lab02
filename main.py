def eratosthenes(n):
    numbers = [i for i in range(n + 1)]

    numbers[1] = 0

    i = 2
    while i <= n:
        if numbers[i] != 0:
            j = i + i
            while j <= n:
                numbers[j] = 0
                j = j + i
        i += 1
    numbers = [i for i in numbers if i != 0]
    return numbers


n = int(input("Введите натуральное число: "))
result = eratosthenes(n)
print("Простые числа до", n, ":", result)