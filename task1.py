# 1) створюємо cache у зовнішній функції;
# 2) внутрішня fibonacci пам'ятає cache через замикання;
# 3) якщо число вже рахували, беремо з cache, інакше рахуємо рекурсивно.
def caching_fibonacci():
    cache = {}

    def fibonacci(n):
        if n <= 0:
            return 0
        if n == 1:
            return 1

        if n in cache:
            return cache[n]

        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci


if __name__ == "__main__":
    my_fib = caching_fibonacci()

    print(my_fib(8))
    print(my_fib(15))
