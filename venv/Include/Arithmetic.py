def Fibo(a):
    if a == 1 or a == 2:
        return 1
    else:
        return Fibo(a - 1) + Fibo(a - 2)


print(Fibo(6))

