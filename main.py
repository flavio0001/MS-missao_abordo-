import funcoes

print("Bem-vindo ao módulo de missão")

def menu_principal():
    print("\n--- Menu Principal ---")
    print("1. Adicionar missões")
    print("2. Consultar status de uma missão")
    print("3. Listar todas as missões")
    print("4. Encerrar o programa")

def main():
    missoes = []

    while True:
        menu_principal()

        try:
            escolher_opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Por favor, insira um número válido.")
            continue

        match escolher_opcao:
            case 1:
                funcoes.adicionar_missao(missoes)
            case 2:
                if missoes:
                    for i, missao in enumerate(missoes):
                        print(f"{i + 1}. {missao['nome']} - Início: {missao['data_hora_inicio']}")
                    try:
                        escolha_missao = int(input("Escolha a missão para verificar o status: ")) - 1
                        if 0 <= escolha_missao < len(missoes):
                            funcoes.verificar_status(missoes[escolha_missao])
                        else:
                            print("Número de missão inválido.")
                    except ValueError:
                        print("Opção inválida. Por favor, insira um número.")
                else:
                    print("Não há missões cadastradas.")
            case 3:
                if missoes:
                    for missao in missoes:
                        print(f"Missão: {missao['nome']} - Início: {missao['data_hora_inicio']} - Fim: {missao['data_hora_fim']}")
                else:
                    print("Não há missões cadastradas.")
            case 4:
                print("Encerrando o programa...")
                break
            case _:
                print("Opção inválida. Por favor, escolha uma opção de 1 a 4.")

if __name__ == "__main__":
    main()
