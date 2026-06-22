def fatorial(n):
    if n <= 1:
        return 1
    
    return fatorial(n - 1) * n

print(fatorial(7))

def soma(n):
    if n <= 1:
        return n
    
    return soma(n // 10) + n % 10

print(soma(678))

