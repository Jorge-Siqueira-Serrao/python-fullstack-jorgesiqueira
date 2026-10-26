import json
import os
from statistics import mean

# --- Funções Auxiliares ---

def _carregar() -> list[dict]:
    """Carrega os dados do arquivo JSON. Retorna lista vazia se não existir."""
    try:
        with open("alunos.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def _salvar(alunos: list[dict]) -> None:
    """Salva a lista de alunos no arquivo JSON."""
    with open("alunos.json", "w", encoding="utf-8") as f:
        json.dump(alunos, f, indent=4, ensure_ascii=False)

# --- Funções Obrigatórias ---

def cadastrar_aluno(nome: str, email: str, idade: int, notas: list[float]) -> dict:
    """Cadastra um aluno e salva no JSON.
    
    Args:
        nome (str): Nome do aluno.
        email (str): E-mail do aluno.
        idade (int): Idade do aluno.
        notas (list[float]): Lista de notas.
        
    Returns:
        dict: O dicionário do aluno cadastrado.
    """
    alunos = _carregar()
    novo_id = max((a["id"] for a in alunos), default=0) + 1
    
    aluno = {"id": novo_id, "nome": nome, "email": email, "idade": idade, "notas": notas, "ativo": True}
    alunos.append(aluno)
    _salvar(alunos)
    return aluno

def listar_alunos() -> list[dict]:
    """Retorna todos os alunos cadastrados."""
    return _carregar()

def buscar_por_nome(nome: str) -> dict | None:
    """Busca um aluno pelo nome (ignora maiúsculas/minúsculas).
    
    Args:
        nome (str): Nome a ser buscado.
        
    Returns:
        dict | None: O aluno encontrado ou None.
    """
    return next((a for a in _carregar() if a["nome"].lower() == nome.lower()), None)

def calcular_media_turma() -> float:
    """Calcula a média geral somando a média individual de cada aluno.
    
    Returns:
        float: A média da turma ou 0.0 se vazia.
    """
    alunos = _carregar()
    if not alunos: return 0.0
    return mean(mean(a["notas"]) for a in alunos if a["notas"])

def exportar_relatorio() -> None:
    """Gera o relatório com estatísticas da turma em 'relatorio_turma.json'."""
    alunos = _carregar()
    if not alunos:
        print("Sem alunos para gerar relatório.")
        return

    # Cria uma lista de dicionários com nome e média de cada aluno
    medias = [{"nome": a["nome"], "media": round(mean(a["notas"]), 2)} for a in alunos if a["notas"]]
    
    relatorio = {
        "total_alunos": len(alunos),
        "media_geral": round(calcular_media_turma(), 2),
        "maior_media": max(medias, key=lambda x: x["media"]),
        "menor_media": min(medias, key=lambda x: x["media"])
    }

    with open("relatorio_turma.json", "w", encoding="utf-8") as f:
        json.dump(relatorio, f, indent=4, ensure_ascii=False)
    print("✅ Relatório 'relatorio_turma.json' exportado!")

# --- Demonstração ---
if __name__ == "__main__":
    # Remove arquivos antigos para começar limpo
    for arquivo in ["alunos.json", "relatorio_turma.json"]:
        if os.path.exists(arquivo): os.remove(arquivo)

    print("1. Cadastrando 4 alunos...")
    cadastrar_aluno("Ana Silva", "ana@email.com", 20, [9.5, 8.0, 10.0])
    cadastrar_aluno("Bruno Costa", "bruno@email.com", 22, [6.0, 7.5, 5.0])
    cadastrar_aluno("Carla Dias", "carla@email.com", 19, [8.0, 8.5, 9.0])
    cadastrar_aluno("Daniel Souza", "daniel@email.com", 21, [4.0, 5.0, 6.5])

    print("\n2. Listando alunos:")
    for a in listar_alunos():
        print(f"   ID: {a['id']} | Nome: {a['nome']} | Notas: {a['notas']}")

    print("\n3. Buscando 'Carla Dias':")
    print(f"   Encontrado: {buscar_por_nome('Carla Dias')}")

    print(f"\n4. Média da turma: {calcular_media_turma():.2f}")

    print("\n5. Exportando relatório:")
    exportar_relatorio()

    