def sum_digits(n):
    sum = 0
    temp = n
    while temp!= 0:
        remainder = temp % 10
        sum += remainder
        temp = temp // 10
    return sum
