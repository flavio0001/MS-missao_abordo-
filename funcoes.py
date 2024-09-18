import datetime

equipe = {}


def obter_data(mensagem):
    while True:
        data = input(mensagem).strip()
        try:
            datetime.datetime.strptime(data, "%d/%m/%Y")
            return data
        except ValueError:
            print("Data inválida. Por favor, escolha o formato DD/MM/AAAA")


def obter_hora(mensagem):
    while True:
        hora = input(mensagem).strip()
        try:
            datetime.datetime.strptime(hora, "%H:%M")
            return hora
        except ValueError:
            print("Hora inválida. Por favor, escolha o formato HH:MM")


def adicionar_missao(missoes):
    while True:
        nome_missao = input("Informe o nome da missão: ").strip().upper()
        if not nome_missao:
            print("O nome da missão não pode ficar em branco")
            continue

        data_inicio = obter_data("Informe a data início (DD/MM/AAAA): ")
        hora_inicio = obter_hora("Informe a hora início (HH:MM): ")
        data_fim = obter_data("Informe a data final (DD/MM/AAAA): ")
        hora_final = obter_hora("Informe a hora final (HH:MM): ")

        tempo_inicio = f"{data_inicio} {hora_inicio}"
        tempo_fim = f"{data_fim} {hora_final}"

        print(f"Missão: {nome_missao}")
        print(f"Data e hora de início: {tempo_inicio}")
        print(f"Data e hora de fim: {tempo_fim}")

        for i in range(5):
            while True:
                entrada = input(f"Digite o {i + 1}º cargo e o nome do membro (separados por dois pontos): ").strip()
                if ":" not in entrada:
                    print("Formato inválido. Use o formato 'cargo:nome'.")
                    continue

                try:
                    cargo, nome = entrada.split(":")
                    equipe[cargo.strip()] = nome.strip()
                    break
                except ValueError:
                    print("Erro ao processar a entrada. Tente novamente.")

        missoes[nome_missao] = {
            "inicio": tempo_inicio,
            "fim": tempo_fim,
            "equipe": equipe.copy()
        }
        print(f"Missão {nome_missao} adicionada com sucesso!")
        break


missoes = {}
adicionar_missao(missoes)
print(missoes)
