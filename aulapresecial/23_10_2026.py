
# def calcular_imc(peso: float, altura: float) -> float:
#     """
#     Calcula o Índice de Massa Corporal (IMC).

#     Args: 
#         peso (float): O peso da pessoa em quilogramas.
#         altura (float): A altura da pessoa em metros.

#     Returns:
#         float: O valor do IMC calculado.
#     """
#     return peso / (altura ** 2)
# print(round(calcular_imc(70, 1.75), 2))
# print(calcular_imc.__doc__.splitlines()[0])

"""
def com_log(funcao):
    def interna(*args, **kwargs):
        print(f"Chamando {funcao.__name__}")
        return funcao(*args, **kwargs)
    return interna

@com_log
def somar(a, b):
    return a + b

print(somar(2, 3))
"""

"""
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)
print([fib(i) for i in range(8)])
"""

"""
def resumo(*notas, **opcoes):
    # *notas = várias notas | **opcoes = configurações extras (ex: casas)
    return {
        # Média: Soma e divide pela quantidade, arredondando (padrão 2 casas)
        'media': round(sum(notas) / len(notas), opcoes.get('casas')),
        'maior': max(notas), # Maior nota
        'menor': min(notas)  # Menor nota
    }

# Teste rápido (casas=1 arredonda para 1 casa decimal):
print(resumo(7.5, 8.2, 6.9, casas=1))
"""

''