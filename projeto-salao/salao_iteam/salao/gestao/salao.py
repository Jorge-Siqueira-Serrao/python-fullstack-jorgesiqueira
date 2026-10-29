# salao/gestao/salao.py
# =============================================================================
# ITEAM | Projeto: Salão de Beleza & Barbearia
# Módulo : salao.gestao.salao
# Assunto: Composição, agregação e design de classes       (Seção 5.5)
# =============================================================================

from salao.equipes.equipe import Equipe
from salao.modelos.equipamento import Equipamento
from salao.modelos.funcionario import Funcionario, Coordenador

class Salao:
    """
    Classe principal do sistema. Gerencia equipes, equipamentos e coordenador.
    Demonstra COMPOSIÇÃO: o Salão 'tem' equipes e equipamentos.
    """
    def __init__(self, nome: str, endereco: str, coordenador: Coordenador):
        self.nome        = nome.strip().title()
        self.endereco    = endereco.strip()
        self.coordenador = coordenador
        self.__equipes:     list[Equipe]      = []
        self.__equipamentos: list[Equipamento] = []

    # --- Gestão de equipes ---
    def adicionar_equipe(self, equipe: Equipe):
        if not isinstance(equipe, Equipe):  # ← Corrigido (BUG 12): validação de tipo adicionada
            raise TypeError("Apenas objetos Equipe podem ser adicionados.")
        self.__equipes.append(equipe)
        print(f"  Equipe '{equipe.nome_equipe}' registrada no salão.")

    def listar_equipes(self):
        print(f"\n{'='*48}")
        print(f"  EQUIPES DO SALÃO — {self.nome}")
        print(f"{'='*48}")
        for equipe in self.__equipes:
            print(f"  {equipe}")
            print(f"    Serviços: {equipe.descricao_servicos()}")

    # --- Gestão de equipamentos ---
    def adicionar_equipamento(self, equipamento: Equipamento):
        if not isinstance(equipamento, Equipamento):
            raise TypeError("Apenas Equipamento pode ser adicionado.")
        self.__equipamentos.append(equipamento)
        print(f"  Equipamento '{equipamento.nome}' cadastrado.")

    def listar_equipamentos(self):
        print(f"\n{'='*48}")
        print(f"  EQUIPAMENTOS — {self.nome}")
        print(f"{'='*48}")
        total = 0.0
        for eq in self.__equipamentos:
            print(f"  {eq}")
            total += eq.valor
        print(f"\n  Valor total do acervo: R$ {total:.2f}")

    # --- Relatório financeiro ---
    def relatorio_financeiro(self):
        print(f"\n{'='*48}")
        print(f"  RELATÓRIO FINANCEIRO — {self.nome}")
        print(f"{'='*48}")
        print(f"  Coordenador: {self.coordenador}")
        print()

        total = 0.0
        todos_funcionarios: list[Funcionario] = []
        for equipe in self.__equipes:
            todos_funcionarios.extend(equipe._membros)

        for f in todos_funcionarios:
            total += f.calcular_salario()  # ← Corrigido (BUG 13): alterado de salario_base para calcular_salario()
            print(f"  {f}")

        # Adiciona o salário do coordenador também
        total += self.coordenador.calcular_salario()
        print(f"\n  Folha total (incluindo coordenador): R$ {total:.2f}")
        print(f"{'='*48}")

    def __str__(self):
        return (f"Salão: {self.nome} | "
                f"Endereço: {self.endereco} | "
                f"Equipes: {len(self.__equipes)} | "
                f"Equipamentos: {len(self.__equipamentos)}"
        )

