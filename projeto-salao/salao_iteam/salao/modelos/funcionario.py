# salao/modelos/funcionario.py
# =============================================================================
# ITEAM | Projeto: Salão de Beleza & Barbearia
# Módulo : salao.modelos.funcionario
# Assunto: Herança, super() e Polimorfismo              (Seções 5.3.2 e 5.6)
# =============================================================================

from salao.modelos.pessoa import Pessoa

class Funcionario(Pessoa):
    """
    Representa um funcionário do salão. Herda de Pessoa e adiciona cargo e salário base.
    """
    def __init__(self, nome: str, cpf: str, telefone: str, cargo: str, salario_base: float):
        super().__init__(nome, cpf, telefone)  # ← Corrigido (BUG 3): adicionado o argumento 'telefone'
        self.cargo        = cargo.strip().title()
        self.salario_base = salario_base

    def calcular_salario(self) -> float:
        """Retorna o salário final. Pode ser sobrescrito pelas subclasses."""
        return self.salario_base

    def __str__(self):
        return (f"[{self.cargo}] {self.nome} "
                f"| Salário: R$ {self.calcular_salario():.2f}"
        )


class Coordenador(Funcionario):
    """
    Coordenador recebe salário base + bônus percentual.
    Demonstra sobrescrita de método (polimorfismo).
    """
    def __init__(self, nome: str, cpf: str, telefone: str, salario_base: float, percentual_bonus: float):
        super().__init__(nome, cpf, telefone, "Coordenador", salario_base)
        self.percentual_bonus = percentual_bonus   # ex: 0.15 = 15 %

    def calcular_comissao(self) -> float:
        return self.salario_base * self.percentual_bonus  # ← Corrigido (BUG 4): calcula o bônus real baseado na base e percentual

    def calcular_salario(self) -> float:
        """Salário do coordenador = base + bônus."""
        return self.salario_base + self.calcular_comissao()

    def __str__(self):
        return (f"[Coordenador] {self.nome} "
                f"| Base: R$ {self.salario_base:.2f} "
                f"| Bônus: R$ {self.calcular_comissao():.2f} "
                f"| Total: R$ {self.calcular_salario():.2f}"
        )

