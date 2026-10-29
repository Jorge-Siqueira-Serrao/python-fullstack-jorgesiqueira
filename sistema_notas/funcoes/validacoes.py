# ============================================================
# MÓDULO: validacoes.py
# Responsável por todas as funções de validação do sistema
# ============================================================

def validar_turma(nome_turma):
    """
    Valida o nome da turma informado pelo usuário.
    Regras:
    - Não pode ser uma string vazia ou só espaços
    - Não pode ser igual a "sair" (palavra reservada para encerrar)
    
    Parâmetros:
    nome_turma (str): valor digitado pelo usuário
    
    Retorno:
    bool: True se válido, False caso contrário
    """
    # Remove espaços extras nas pontas
    texto = nome_turma.strip()
    
    # Verifica se está vazio ou se é igual a "sair" (ignorando maiúsculas/minúsculas)
    if not texto or texto.lower() == "sair":
        return False
        
    return True


def validar_aluno(nome_aluno):
    """
    Valida o nome do aluno informado pelo usuário.
    Regras:
    - Não pode ser uma string vazia ou só espaços
    - Não pode ser igual a "sair"
    - Deve conter ao menos duas palavras (nome e sobrenome)
    
    Parâmetros:
    nome_aluno (str): valor digitado pelo usuário
    
    Retorno:
    bool: True se válido, False caso contrário
    """
    # Remove espaços extras
    texto = nome_aluno.strip()
    
    # Verifica se está vazio ou é igual a "sair"
    if not texto or texto.lower() == "sair":
        return False
        
    # Separa as palavras usando .split()
    palavras = texto.split()
    
    # Confirma se informou ao menos 2 palavras (nome e sobrenome)
    if len(palavras) < 2:
        return False
        
    return True


def validar_nota(valor_digitado):
    """
    Valida e converte uma nota digitada pelo usuário.
    Regras:
    - Deve ser um número (aceita ponto ou vírgula como decimal)
    - Deve estar entre 0.0 e 10.0 (inclusive)
    
    Parâmetros:
    valor_digitado (str): string digitada pelo usuário
    
    Retorno:
    float ou None: o valor convertido se válido, ou None se inválido
    """
    # Substitui vírgula por ponto para aceitar "7,5" como "7.5" e remove espaços
    texto = valor_digitado.strip().replace(",", ".")
    
    try:
        # Tenta converter para float
        nota = float(texto)
        
        # Verifica se o número está dentro do intervalo permitido [0.0, 10.0]
        if 0.0 <= nota <= 10.0:
            return nota
        else:
            return None
            
    except ValueError:
        # Se falhar na conversão (ex: letras ou caracteres inválidos), retorna None
        return None
