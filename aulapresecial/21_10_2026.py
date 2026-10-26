
"""
frase = input("frase: ").lower()
vogais = 0
for letra in frase:
    if letra in "aeiou":
        vogais += 1
print(f"Vogais: {vogais}")
"""
"""
for i in range(1, 5):
    for j in range(1, 5):
        print(f"{i * j:3}", end="")
    print()
"""
"""
try: 
    numero = int(input("Digite um número: "))
    resultado = 10 / numero
    print(f"Resultado: {resultado}")
except ValueError:
    print("Erro: digite um número válido.")
except ZeroDivisionError:
    print("Não é possível dividir por zero.")
"""
"""
try:
    numero = int(input("Digite um número: "))
    resultado = 10 / numero
except ZeroDivisionError as e:
    print(f"Erro: {e}")
else:
    print(f"Resultado: {resultado}")
finally:
    print("Encerrando operação.")
"""
"""
idade = -5
try:
    if idade < 0:
        raise ValueError("Idade não pode ser negativa.")
    print("Idade válida.")
except ValueError as erro:
    print(f"Erro: {erro}")
"""
"""
while True:
    texto = input("Nota (0 a 10): ")
    try:
        nota = float(texto)
    except ValueError:
        print(f"Só números.")
        continue
    if 0 <= nota <= 10:
        break
    print("Fora de faixa.")
print(f"Nota: {nota}")
"""
"""
import random
random.seed(100)
tentativas = 0
dado = 0
while dado != 6:
    dado = random.randint(1, 6)
    tentativas += 1
print(f"Tentativas: {tentativas}: {dado}")
print("Tirou 6!")
"""

alunos = ["Ana", "Bruno", "Carlos"]
dados_mistos = [1, "Teste", True, 3.14]
print(alunos[0], alunos[-1])
print(len(alunos), "Bruno" in alunos)
print(dados_mistos)
''