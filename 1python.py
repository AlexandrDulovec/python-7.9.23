X = int(input("Zadej lichý číslo X: "))

if X % 2 == 0:
    print("Zadej lichý číslo.")
else:
    for i in range(1, X + 1):
        if i <= (X // 2) + 1:
            spaces = (X // 2 + 1) - i
            numbers = i
        else:
            spaces = i - (X // 2 + 1)
            numbers = X - i + 1
        row = " " * spaces + str(numbers) * numbers
        print(row)
