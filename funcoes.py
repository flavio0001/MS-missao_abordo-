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

        data_hora_inicio = datetime.datetime.strptime(tempo_inicio, "%d/%m/%Y %H:%M")
        data_hora_fim = datetime.datetime.strptime(tempo_fim, "%d/%m/%Y %H:%M")

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

        missoes.append({
            "nome": nome_missao,
            "data_hora_inicio": data_hora_inicio,
            "data_hora_fim": data_hora_fim,
            "equipe": equipe.copy()
        })
        print(f"Missão {nome_missao} adicionada com sucesso!")
        break

def verificar_status(missao):
    agora = datetime.datetime.now()

    inicio = missao["data_hora_inicio"]
    fim = missao["data_hora_fim"]

    if agora < inicio:
        if (inicio - agora).total_seconds() <= 3600:
            print(f"A missão '{missao['nome']}' está prestes a iniciar.")
        else:
            print(f"A missão '{missao['nome']}' ainda vai iniciar.")
    elif inicio <= agora <= fim:
        print(f"A missão '{missao['nome']}' está em andamento.")
    else:
        print(f"A missão '{missao['nome']}' já foi concluída.")
