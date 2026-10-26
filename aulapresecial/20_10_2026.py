"""
saldo = 120.0
valor = 150.0
limite_extra = 50.0  # Exemplo de saldo + limite

if valor <= saldo:
    saldo -= valor
    print("Compra aprovada")
elif valor <= (saldo + limite_extra):
    print("Compra aprovada utilizando o limite extra!")
    saldo += limite_extra
else:
    print("Saldo insuficiente")
print(f"Saldo: R$ {saldo:.2f}")
"""

"""
nome = ""
print(bool(nome), bool([]), bool(0), bool("a"))
if not nome:
    print("Nome vazio")
idade = 20
status = "adulto" if idade >= 18 else "menor"
print(status)

"""

"""
idade = int(input("Idade: "))
est = input("Estudante (S/N): ") == "S"
if idade < 12 or idade > 60:
    preco = 10
elif est:
    preco = 15
else:
    preco = 30
print(f"Ingresso: R$ {preco:.2f}")
"""
