MOD = 10**9 + 7

def multiply(A, B):
    # Умножение матриц 2x2 по модулю
    C = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % MOD
    return C

def power(A, n):
    # Быстрое возведение матрицы в степень n
    res = [[1, 0], [0, 1]] # Единичная матрица
    while n > 0:
        if n % 2 == 1:
            res = multiply(res, A)
        A = multiply(A, A)
        n //= 2
    return res

def fib(n):
    if n == 0: return 0
    if n == 1: return 1
    
    T = [[1, 1], [1, 0]]
    T_n = power(T, n)
    
    # Результат Fn находится в T_n[0][1] или T_n[1][0]
    return T_n[0][1]

# Пример
n = 10**18
print(fib(n))
