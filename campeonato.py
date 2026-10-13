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
 
 
def partida_ja_registrada(mandante, visitante):
    """Verifica se o confronto (mandante x visitante) já aconteceu."""
    for p in partidas:
        if p["mandante"] == mandante and p["visitante"] == visitante:
            return True
    return False
 
 
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
 
 
def atualizar_estatisticas(time, gols_pro, gols_contra):
    """Atualiza (por atribuição) as estatísticas de um time após uma partida."""
    time["jogos"] += 1
    time["gols_pro"] += gols_pro
    time["gols_contra"] += gols_contra
 
    if gols_pro > gols_contra:
        time["vitorias"] += 1
        time["pontos"] += PONTOS_VITORIA
    elif gols_pro == gols_contra:
        time["empates"] += 1
        time["pontos"] += PONTOS_EMPATE
    else:
        time["derrotas"] += 1
 
 
def registrar_partida(nome_mandante=None, nome_visitante=None,
                      gols_m=None, gols_v=None):
    """Registra uma partida. Se os parâmetros forem None, lê do teclado."""
    if len(times) < 2:
        print("  Cadastre pelo menos 2 times antes de registrar partidas.")
        return
 
    if nome_mandante is None:
        print("  Times cadastrados: " + ", ".join(t["nome"] for t in times))
        nome_mandante = input("Time mandante: ").strip()
        nome_visitante = input("Time visitante: ").strip()
 
    pos_m = buscar_time(nome_mandante)
    pos_v = buscar_time(nome_visitante)
 
    # Decisões: validações das regras de negócio
    if pos_m == -1 or pos_v == -1:
        print("  Time não encontrado. Verifique os nomes.")
        return
    if pos_m == pos_v:
        print("  Um time não pode jogar contra ele mesmo.")
        return
    if partida_ja_registrada(times[pos_m]["nome"], times[pos_v]["nome"]):
        print("  Essa partida já foi registrada (turno único por mando).")
        return
 
    if gols_m is None:
        gols_m = ler_inteiro(f"Gols do {times[pos_m]['nome']}: ")
        gols_v = ler_inteiro(f"Gols do {times[pos_v]['nome']}: ")
 
    # Alteração de estado: histórico de partidas e estatísticas dos dois times
    partidas.append({
        "mandante": times[pos_m]["nome"],
        "visitante": times[pos_v]["nome"],
        "gols_m": gols_m,
        "gols_v": gols_v,
    })
    atualizar_estatisticas(times[pos_m], gols_m, gols_v)
    atualizar_estatisticas(times[pos_v], gols_v, gols_m)
    print(f"  Resultado registrado: {times[pos_m]['nome']} {gols_m} x "
          f"{gols_v} {times[pos_v]['nome']}")
 
 
def saldo_de_gols(time):
    return time["gols_pro"] - time["gols_contra"]
 
 
def criterio(time):
    """Critérios de classificação, em ordem de prioridade:
    1) pontos  2) vitórias  3) saldo de gols  4) gols pró."""
    return (time["pontos"], time["vitorias"], saldo_de_gols(time),
            time["gols_pro"])
 
 
def ordenar_tabela():
    """Ordena uma cópia da lista de times com Bubble Sort (decrescente)."""
    tabela = times[:]          # cópia, para não alterar a ordem de cadastro
    n = len(tabela)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if criterio(tabela[j]) < criterio(tabela[j + 1]):
                tabela[j], tabela[j + 1] = tabela[j + 1], tabela[j]
    return tabela
 
 
def exibir_classificacao():
    if len(times) == 0:
        print("  Nenhum time cadastrado.")
        return
 
    tabela = ordenar_tabela()
    print()
    print(f"{'Pos':<4}{'Time':<18}{'P':>4}{'J':>4}{'V':>4}{'E':>4}"
          f"{'D':>4}{'GP':>4}{'GC':>4}{'SG':>5}")
    print("-" * 55)
    posicao = 1
    for t in tabela:
        print(f"{posicao:<4}{t['nome']:<18}{t['pontos']:>4}{t['jogos']:>4}"
              f"{t['vitorias']:>4}{t['empates']:>4}{t['derrotas']:>4}"
              f"{t['gols_pro']:>4}{t['gols_contra']:>4}"
              f"{saldo_de_gols(t):>5}")
        posicao += 1
 
    lider = tabela[0]
    if lider["jogos"] > 0:
        print(f"\n  Líder: {lider['nome']} com {lider['pontos']} ponto(s).")
 
 
def exibir_menu():
    print("\n===== CAMPEONATO DE PONTOS CORRIDOS =====")
    print("1 - Cadastrar time")
    print("2 - Registrar partida")
    print("3 - Ver classificação")
    print("0 - Sair")
 
 
def main():
    opcao = -1
    while opcao != 0:
        exibir_menu()
        opcao = ler_inteiro("Escolha uma opção: ")
 
        if opcao == 1:
            cadastrar_time()
        elif opcao == 2:
            registrar_partida()
        elif opcao == 3:
            exibir_classificacao()
        elif opcao == 0:
            print("Encerrando o programa. Até logo!")
        else:
            print("  Opção inválida.")
 
 
if __name__ == "__main__":
    main()


