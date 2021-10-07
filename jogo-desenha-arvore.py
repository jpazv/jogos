def triangulo(n):
    a = 1
    b = 2*n-2
    while a < 2*n-1:
        for linha in range(1, n+1):
            print(' '*b, '*'*a)
            a += 2
            b -= 1


triangulo(10)