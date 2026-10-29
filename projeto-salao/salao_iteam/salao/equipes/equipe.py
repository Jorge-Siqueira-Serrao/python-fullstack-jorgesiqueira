# salao/equipes/equipe.py
# =============================================================================
# ITEAM | Projeto: Salão de Beleza & Barbearia
# Módulo : salao.equipes.equipe
# Assunto: Interface / Classe Abstrata com ABC             (Seção 5.3.3 e 5.7)
# =============================================================================

from abc import ABC, abstractmethod
from salao.modelos.funcionario import Funcionario

class Equipe(ABC):  # ← Corrigido (BUG 7): agora herda de ABC
    """
    Interface base para todas as equipes do salão.
    Define o contrato que TODA equipe deve cumprir.
    """
    def __init__(self, nome_equipe: str):
        self.nome_equipe = nome_equipe
        self._membros: list[Funcionario] = []  # protegido (convenção _)

    def adicionar_membro(self, funcionario: Funcionario):
        """Adiciona um funcionário à equipe."""
        if not isinstance(funcionario, Funcionario):
            raise TypeError("Apenas Funcionario pode ser adicionado à equipe.")
        self._membros.append(funcionario)
        print(f"  + {funcionario.nome} adicionado(a) à equipe '{self.nome_equipe}'.")

    def listar_membros(self):
        """Exibe todos os membros da equipe."""
        print(f"\n  Equipe: {self.nome_equipe}")
        print("  " + "-" * 36)
        if not self._membros:
            print("  (nenhum membro cadastrado)")
        for m in self._membros:
            print(f"  • {m}")

    @abstractmethod
    def descricao_servicos(self) -> str:
        """Retorna os serviços oferecidos pela equipe."""
        pass

    @abstractmethod  # ← Corrigido (BUG 8): adicionado o decorador abstrato
    def realizar_servico(self, cliente: str, servico: str):
        """Registra a realização de um serviço."""
        pass          # ← Corrigido (BUG 8): alterado de raise NotImplementedError para pass

    def __str__(self):
        return f"Equipe '{self.nome_equipe}' | {len(self._membros)} membro(s)"

