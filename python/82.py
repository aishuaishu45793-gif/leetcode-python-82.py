# Program 154: Rotate a List

numbers = [1, 2, 3, 4, 5]
k = 2

k = k % len(numbers)

rotated = numbers[-k:] + numbers[:-k] if k else numbers[:]

print("Original list:", numbers)
print("Rotated list:", rotated)