# Calculate the 40th number of the fiboncci sequence.

# Write a function 'fib(n)' that takes in a number as an argument. The function should return the n-th number of the Fibonacci sequence.

# fib(n) - 1, 1 , 2, 3, 5, 8, 13, 21, 34, ...


# First Method
class FibFirst:
    def fib_value(self, num: int):
        if num <= 2:
            return 1

        return self.fib_value(num - 1) + self.fib_value(num - 2)


series_1 = FibFirst()
print(series_1.fib_value(10))


# Second Method
class FibSecond:
    def fib_value(
        self, num: int, prev_value: int = 0, current_value: int = 1, count: int = 1
    ):
        if num == 1:
            return prev_value

        temp_current = current_value
        current_value += prev_value
        prev_value = temp_current
        count += 1

        if count == num:
            return current_value

        return self.fib_value(num, prev_value, current_value, count)


# series_2 = FibSecond()
# print(series_2.fib_value(10))


# Third Method (using memoization) [Recommended Method]
def fib(n, memo={}):
    if n in memo:
        return memo[n]

    if n <= 2:
        return 1

    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)

    return memo[n]


# print(fib(6))
