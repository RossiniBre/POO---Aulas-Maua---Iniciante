def fatorial(n):
    if n == 0 or n == 1:
        return 1
    
     
    return n * fatorial(n-1)

print(fatorial(5))

def fibonnaci(n):
    if n == 0 or n == 1:
        return n
    
    return fibonnaci(n-1) + fibonnaci(n-2)

print(fibonnaci(10))

def soma(n):
    if len(n) <= 1:
        return n[0]
    
    return n[0] + soma(n[1:]) 

print(soma([6, 2, 8]))

# def palindromo(n):
#     if n[1:] + palindromo(n[1:-1]) + n[-1] == n:
#         return True
    
#     return n[1:] + palindromo(n[1:-1]) + n[-1]

# print(palindromo("Ovo"))

def contagem(n):
    if n == 0:
        return 0

    print(n)

    return contagem(n-1)

print(contagem(10))