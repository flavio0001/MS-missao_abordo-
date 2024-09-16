import datetime

equipe = {}
def adicionar_missao(missoes):
    while True:
        nome_missao = str(input("Informe o nome da missão:")).strip().upper()
        if nome_missao == '':
            print("O nome da missão não pode ficar em branco")
            exit()
        else:
            while True:
                data_inicio = str(input("Informe a data início: No formato: DD/MM/AAAA: ")).strip()
                try:
                    datetime.datetime.strptime(data_inicio, "%d/%m/%Y")
                    break
                except ValueError:
                    print("Data inválida. Por favor, escolha o formato DD/MM/AAAA.")

            while True:
                hora_inicio = str(input("Hora início. No formato: HH:MM: ")).strip()
                try:
                    datetime.datetime.strptime(hora_inicio, "%H:%M")
                    break
                except ValueError:
                    print("Hora inválida. Por favor, coloque o horário correto no formato HH:MM.")

            tempo_inicio = f"{data_inicio} {hora_inicio}"

            while True:
                data_fim = str(input("Informe a data final: No formato: DD/MM/AAAA: ")).strip()
                try:
                    datetime.datetime.strptime(data_fim, "%d/%m/%Y")
                    break
                except ValueError:
                    print("Data inválida. Por favor, escolha o formato DD/MM/AAAA.")

            while True:
                hora_fim = str(input("Hora final. No formato: HH:MM: ")).strip()
                try:
                    datetime.datetime.strptime(hora_fim, "%H:%M")
                    break
                except ValueError:
                    print("Hora inválida. Por favor, coloque o horário correto no formato HH:MM.")
                    tempo_inicio = f"{data_fim} {hora_fim}"

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
