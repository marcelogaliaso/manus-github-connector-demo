"""
Demonstração do Conector GitHub - Manus
Arquivo criado programaticamente via integração GitHub do Manus.
"""

def saudacao(nome: str) -> str:
    """Retorna uma saudação personalizada."""
    return f"Olá, {nome}! Este arquivo foi criado pelo conector GitHub do Manus."


if __name__ == "__main__":
    print(saudacao("Mundo"))
    print("Capacidades demonstradas:")
    capacidades = [
        "Autenticação OAuth",
        "Leitura de perfil e repositórios",
        "Criação de repositórios",
        "Gerenciamento de branches",
        "Commits e push de arquivos",
        "Criação e gerenciamento de issues",
        "Pull Requests",
        "Consulta ao histórico de commits",
    ]
    for i, cap in enumerate(capacidades, 1):
        print(f"  {i}. {cap}")
