def findLargest(num1, num2):
    if num1 > num2:
        return f"liczba num1: {num1} jest większa niz num2: {num2}"
    elif num1 < num2:
        return f"liczba num2: {num2} jest większa niz  num1: {num1}"
    elif num1 == num2:
        return f"liczba num2: {num2} jest równa num1: {num1}"
print(findLargest(3,10))
print(findLargest(12,7))
        