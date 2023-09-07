def licheprirozenecislo(X):
    for i in range(1, 2 * X):
        for j in range(1, 2 * X):
            value = X - max(abs(X - i), abs(X - j))
            print(value, end=" ")
        print()
X = int(input("Lichý přirozený číslo: "))
if X % 2 == 0 or X <= 0:
    print("Lichý přirozený číslo větší než 0.")
else:
    licheprirozenecislo(X)