arr = [int(input()) for _ in range(5)]

price = min(arr[:3]) + min(arr[3:]) - 50

print(price)