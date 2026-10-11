PONTOS_VITORIA = 3
PONTOS_EMPATE = 1
 
# Estado global do programa
times = []
partidas = []
 
 
def ler_inteiro(mensagem, minimo=0):
    """Repete a leitura até o usuário digitar um inteiro >= minimo."""
    while True:
        texto = input(mensagem).strip()
        try:
            valor = int(texto)
        except ValueError:
            print("  Entrada inválida: digite um número inteiro.")
            continue
        if valor < minimo:
            print(f"  O valor deve ser maior ou igual a {minimo}.")
            continue
        return valor
 
 
def buscar_time(nome):
    """Retorna a posição do time na lista (ignorando maiúsculas) ou -1."""
    for i in range(len(times)):
        if times[i]["nome"].lower() == nome.lower():
            return i
    return -1
 
 
def adicionar_time(nome):
    """Cria o time com todas as estatísticas zeradas e o adiciona à lista."""
    time = {
        "nome": nome,
        "jogos": 0,
        "vitorias": 0,
        "empates": 0,
        "derrotas": 0,
        "gols_pro": 0,
        "gols_contra": 0,
        "pontos": 0,
    }
    times.append(time)
 
 
def cadastrar_time():
    nome = input("Nome do time: ").strip()
    if nome == "":
        print("  O nome não pode ser vazio.")
    elif buscar_time(nome) != -1:
        print("  Já existe um time com esse nome.")
    else:
        adicionar_time(nome)
        print(f"  Time '{nome}' cadastrado com sucesso!")
 
 
def exibir_menu():
    print("\n===== CAMPEONATO DE PONTOS CORRIDOS =====")
    print("1 - Cadastrar time")
    print("0 - Sair")
 
 
def main():
    opcao = -1
    while opcao != 0:
        exibir_menu()
        opcao = ler_inteiro("Escolha uma opção: ")
 
        if opcao == 1:
            cadastrar_time()
        elif opcao == 0:
            print("Encerrando o programa. Até logo!")
        else:
            print("  Opção inválida.")
 
 
if __name__ == "__main__":
    main()
 

Claude terminou a resposta
