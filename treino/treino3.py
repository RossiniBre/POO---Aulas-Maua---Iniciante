valor = int(input("Digite o valor: "))
nota100 = valor // 100
resto = valor % 100 

nota50 = resto // 50
resto = resto % 50

nota20 = resto // 20
resto = resto % 20

nota10 = resto // 10
resto = resto % 10

nota5 = resto // 5
resto = resto % 5

nota2 = resto // 2
resto = resto % 2

nota1 = resto // 1
resto = resto % 1

print(f"""{nota100} nota(s) de 100
{nota50} nota(s) de 50
{nota20} nota(s) de 20
{nota10} nota(s) de 10
{nota5} nota(s) de 5
{nota2} nota(s) de 2
{nota1} nota(s) de 1""")


