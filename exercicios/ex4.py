# for i in range(1, 100 + 1):
#     if i % 3 == 0 and i % 5 != 0:
#         print("Multiplo de 3: ", i)
#     elif i % 5 == 0 and i % 3 != 0:
#         print("Multiplo de 5: ", i)

def eh_par(n):
    if n % 2 == 0:
        return True
    else:
        return False
    
for j in [1, 2, 3, 4, 5, 6]:
    print(eh_par(j))