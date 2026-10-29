# salao/modelos/equipamento.py
# =============================================================================
# ITEAM | Projeto: Salão de Beleza & Barbearia
# Módulo : salao.modelos.equipamento
# Assunto: Métodos Especiais (__str__, __repr__, __eq__)    (Seção 5.4)
# =============================================================================

class Equipamento:
    """
    Representa um equipamento do salão (secador, cadeira, autoclave...).
    Demonstra métodos especiais dunder.
    """
    def __init__(self, codigo: str, nome: str, descricao: str, valor: float):
        self.__codigo    = codigo.strip().upper()
        self.nome        = nome.strip().title()
        self.__descricao = descricao.strip()
        self.valor       = valor

    @property
    def codigo(self):
        return self.__codigo

    def __str__(self):
        return (f"[{self.__codigo}] {self.nome} "
                f"| {self.__descricao} "       # ← Corrigido (BUG 5): alterado de self.descricao para self.__descricao
                f"| R$ {self.valor:.2f}"
        )

    def __repr__(self):
        return f"Equipamento(codigo='{self.__codigo}', nome='{self.nome}')"

    def __eq__(self, outro):
        if not isinstance(outro, Equipamento):
            return False
        return self.__codigo == outro._Equipamento__codigo  # ← Corrigido (BUG 6): compara pelo código único usando name-mangling

