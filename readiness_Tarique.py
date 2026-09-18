print("Hello, I am Sadat Tarique, and my student ID is R01839482.")

def mean_max(numbers):
    mean = sum(numbers) / len(numbers)
    maxi = max(numbers)
    print(f"Mean: {mean}, Max: {maxi}")
    return mean, maxi

num = [1, 2, 3, 4, 5]

mean_max(num)