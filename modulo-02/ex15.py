# ==========================================
# FUNÇÕES DAS OPÇÕES DO MENU
# ==========================================

def conversor_temperatura() -> None:
    """Converte Celsius para Fahrenheit."""
    print("\n--- [1] CONVERSOR DE TEMPERATURA ---")
    try:
        celsius = float(input("Digite a temperatura em Celsius: "))
        fahrenheit = (celsius * 1.8) + 32
        print(f"🌡️  {celsius}°C equivale a {fahrenheit:.1f}°F")
    except ValueError:
        print("⚠️  AVISO: Entrada inválida! Digite apenas números.")

def verificar_primo() -> None:
    """Verifica se um número inteiro é primo."""
    print("\n--- [2] VERIFICADOR DE NÚMERO PRIMO ---")
    try:
        numero = int(input("Digite um número inteiro: "))
        if numero < 2:
            print(f"❌ O número {numero} não é primo.")
            return
        
        # Verifica se é divisível por algum número entre 2 e a raiz quadrada dele
        eh_primo = True
        for i in range(2, int(numero ** 0.5) + 1):
            if numero % i == 0:
                eh_primo = False
                break
                
        if eh_primo:
            print(f"✅ O número {numero} É PRIMO!")
        else:
            print(f"❌ O número {numero} NÃO é primo.")
    except ValueError:
        print("⚠️  AVISO: Entrada inválida! Digite um número inteiro.")

def analisar_senha() -> None:
    """Analisa a força de uma senha (simplificado)."""
    print("\n--- [3] ANALISADOR DE SENHA ---")
    try:
        senha = input("Digite sua senha para análise: ")
        
        if len(senha) < 8:
            print("🔴 Senha FRACA: A senha deve ter pelo menos 8 caracteres.")
        elif not any(char.isdigit() for char in senha):
            print("🟡 Senha MÉDIA: A senha precisa conter pelo menos um número.")
        elif not any(char.isalpha() for char in senha):
            print("🟡 Senha MÉDIA: A senha precisa conter pelo menos uma letra.")
        else:
            print("🟢 Senha FORTE: Ótimos critérios de segurança!")
    except Exception:
        # Captura qualquer erro inesperado na leitura (ex: interrupção do teclado)
        print("⚠️  AVISO: Ocorreu um erro ao ler a senha.")

def calculadora_segura() -> None:
    """Realiza uma operação matemática básica com tratamento de erros."""
    print("\n--- [4] CALCULADORA SEGURA ---")
    try:
        num1 = float(input("Digite o primeiro número: "))
        operacao = input("Digite a operação (+, -, *, /): ")
        num2 = float(input("Digite o segundo número: "))
        
        if operacao == "+":
            resultado = num1 + num2
        elif operacao == "-":
            resultado = num1 - num2
        elif operacao == "*":
            resultado = num1 * num2
        elif operacao == "/":
            if num2 == 0:
                raise ZeroDivisionError
            resultado = num1 / num2
        else:
            print("⚠️  AVISO: Operação inválida! Use apenas +, -, * ou /.")
            return

        print(f"🧮 Resultado: {num1} {operacao} {num2} = {resultado:.2f}")
        
    except ValueError:
        print("⚠️  AVISO: Você precisa digitar números válidos.")
    except ZeroDivisionError:
        print("⚠️  AVISO: Não é possível dividir por zero!")

# ==========================================
# SISTEMA PRINCIPAL (MENU)
# ==========================================

def exibir_menu() -> None:
    """Imprime o menu principal na tela."""
    print("=" * 32)
    print("      SISTEMA ITEAM - MENU      ")
    print("=" * 32)
    print("[1] Conversor de temperatura")
    print("[2] Verificador de número primo")
    print("[3] Analisador de senha")
    print("[4] Calculadora segura")
    print("[0] Sair")
    print("=" * 32)

def main() -> None:
    """Loop principal que mantém o sistema ativo."""
    while True:
        exibir_menu()
        
        # try/except para garantir que o usuário digite um número no menu
        try:
            opcao = int(input("👉 Escolha uma opção: "))
        except ValueError:
            print("\n⚠️  AVISO: Opção inválida! Por favor, digite um número.\n")
            continue # Ignora o resto do loop e volta para o menu
            
        print() # Pula uma linha para ficar mais bonito

        # Roteamento das opções com if/elif/else
        if opcao == 1:
            conversor_temperatura()
        elif opcao == 2:
            verificar_primo()
        elif opcao == 3:
            analisar_senha()
        elif opcao == 4:
            calculadora_segura()
        elif opcao == 0:
            print("👋 Saindo do sistema... Até logo!")
            break # Encerra o loop while True e fecha o programa
        else:
            print("⚠️  AVISO: Opção não encontrada. Tente novamente.")
            continue # Ignora o resto e volta para o menu
            
        # Pausa dramática para o usuário conseguir ler o resultado antes do menu voltar
        input("\nPressione ENTER para voltar ao menu...")

# Inicia o programa
if __name__ == "__main__":
    main()
