# ============================================================
# ARQUIVO PRINCIPAL: main.py
# Sistema de Lançamento de Notas — Nível Fácil
# ============================================================
# Este arquivo orquestra o programa inteiro.
# Ele usa as funções dos módulos em /funcoes para:
#   - Ler e validar entradas do usuário
#   - Salvar e exibir notas em JSON
# ============================================================

from funcoes.validacoes import validar_turma, validar_aluno, validar_nota
from funcoes.arquivo import salvar_nota, ler_notas


def obter_turma():
    """
    Solicita ao usuário o nome da turma em loop até receber uma entrada válida.
    Se o usuário digitar "sair", retorna None para sinalizar encerramento.
    
    Retorno:
    str ou None
    """
    while True:
        entrada = input("Nome da turma: ")
        
        # Verifica se o usuário quer sair
        if entrada.strip().lower() == "sair":
            return None
            
        # Valida a turma usando a função do módulo de validações
        if validar_turma(entrada):
            return entrada.strip()
        else:
            print("Erro: Nome da turma inválido. Tente novamente ou digite 'sair'.")


def obter_aluno():
    """
    Solicita ao usuário o nome do aluno em loop até receber uma entrada válida.
    Se o usuário digitar "sair", retorna None.
    
    Retorno:
    str ou None
    """
    while True:
        entrada = input("\nNome do aluno (ou 'sair'): ")
        
        # Verifica se o usuário quer sair
        if entrada.strip().lower() == "sair":
            return None
            
        # Valida o aluno (deve ter ao menos duas palavras)
        if validar_aluno(entrada):
            return entrada.strip()
        else:
            print("Erro: Digite o nome completo (nome e sobrenome válidos) ou 'sair'.")


def obter_nota(numero_da_nota):
    """
    Solicita uma nota ao usuário em loop até receber um valor válido.
    
    Parâmetros:
    numero_da_nota (int): 1, 2 ou 3 — usado na mensagem exibida ao usuário
    
    Retorno:
    float: a nota validada e convertida
    """
    while True:
        entrada = input(f"Nota {numero_da_nota}: ")
        
        # Valida e converte a nota usando o módulo de validações
        nota_convertida = validar_nota(entrada)
        
        if nota_convertida is not None:
            return nota_convertida
        else:
            print("Erro: Nota inválida. Digite um valor numérico entre 0.0 e 10.0.")


def main():
    """
    Função principal que coordena o fluxo do programa.
    """
    print("=" * 45)
    print("  Sistema de Lançamento de Notas")
    print("  Digite 'sair' a qualquer momento para encerrar")
    print("=" * 45)
    
    # Passo 1: Captura o nome da turma
    turma = obter_turma()
    if turma is None:
        print("\nEncerrando o sistema. Até logo!")
        return
        
    # Passo 2: Loop para cadastrar múltiplos alunos na turma escolhida
    while True:
        aluno = obter_aluno()
        if aluno is None:
            break
            
        # Captura as 3 notas do aluno
        nota1 = obter_nota(1)
        nota2 = obter_nota(2)
        nota3 = obter_nota(3)
        
        # Salva os dados no arquivo JSON da turma
        salvar_nota(turma, aluno, nota1, nota2, nota3)
        print("\n✔ Nota salva com sucesso!")
        
        # Exibe todos os registros atuais da turma
        ler_notas(turma)
        
    # Passo 3: Mensagem final de encerramento
    print("\nEncerrando o sistema. Até logo!")


# ── Ponto de entrada do programa ──────────────────────────
if __name__ == "__main__":
    main()
