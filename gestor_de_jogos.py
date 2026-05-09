import datetime
import json

lista = []

JOGOS_JSON = "jogos.json"

def escrever_dados(jogos):
    try:
        with open(JOGOS_JSON, "w") as arquivo:
            json.dump(jogos, arquivo, indent = 4)
            print("Jogos salvos com sucesso!")
    except Exception as erro:
        print(f"Erro ao salvar jogos: {erro}")

def carregar_dados():
    try:
        with open(JOGOS_JSON, "r") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        print("Falha ao tentar encontrar o arquivo 'jogos.json'. Retornando uma lista vazia")
        return [] 
    except json.JSONDecodeError:
        print("O arquivo 'jogos.json' está vazio ou corrompido. Retornando uma lista vazia")
        return []

def encontrar_jogo(nome_jogo, silencioso = False):
    for jogo in lista:
        if jogo['nome'].lower() == nome_jogo.lower():
            return jogo
    if not silencioso:
        print("Jogo não encontrado!")
    return None

def update_jogo(nome_jogo):
    modificar_jogo = encontrar_jogo(nome_jogo)

    if modificar_jogo is not None:
        try:
            status = int(input("Você já zerou o jogo? Digite '1' para SIM e '2' para NÃO: "))
            if status == 1:
                tempo = float(input("\nQuantas horas você levou para zerar o jogo?\n"))
                modificar_jogo['tempo'] = tempo
                modificar_jogo['concluido'] = True
                data = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                atualizacao = {"data": data, "concluido": True, "tempo": tempo}
                modificar_jogo['historico'].append(atualizacao)
                print(f"\nO status do jogo '{nome_jogo}' foi marcado como concluído!\n")
                escrever_dados(lista)
            elif status == 2:
                atualizar_tempo = int(input(f"Gostaria de atualizar o tempo de jogo de '{nome_jogo}'? Digite '1' para SIM e '2' para NÃO: "))
                if atualizar_tempo == 1:
                    tempo = float(input("\nQual o seu tempo de jogo atual?\n"))
                    modificar_jogo['tempo'] = tempo
                    data = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    atualizacao = {"data": data, "tempo": tempo}
                    modificar_jogo['historico'].append(atualizacao)
                    print(f"\nO tempo de jogo de '{nome_jogo}' foi atualizado com sucesso!\n")
                    escrever_dados(lista)
                elif atualizar_tempo == 2:
                    print(f"\nNenhuma alteração feita no jogo '{nome_jogo}'\n")
                else:
                    print("\nComando desconhecido\n")
            else:
                print("\nComando desconhecido\n")
        except ValueError:
            print("Valor incorreto.")
    
def deletar_jogo(nome_jogo):
    excluir_jogo = encontrar_jogo(nome_jogo)
    if excluir_jogo is not None:
        lista.remove(excluir_jogo)
        print(f"\nO jogo {nome_jogo} foi excluído!\n")
        escrever_dados(lista)

def mostrar_jogo():
    if len(lista) == 0:
        print("\nNão tem nenhum jogo para ser listado no momento.\n")
    else:
        for jogo in lista:
            print(f"JOGO: {jogo['nome'].upper()}")
            print(f"TEMPO DE JOGO: {jogo['tempo']} horas")
            print(f"CONCLUÍDO: {'Sim' if jogo.get('concluido', False) else 'Não'}")
            if jogo['historico']:
                print("HISTÓRICO:")
                for entrada in jogo['historico']:
                    data_hora = datetime.datetime.strptime(entrada['data'], "%Y-%m-%d %H:%M:%S")
                    print(f"  DATA: {data_hora.strftime('%d/%m/%Y')}")
                    print(f"  HORA: {data_hora.strftime('%H:%M')}")
                    print(f"  CONCLUÍDO: {'Sim' if entrada.get('concluido', False) else 'Não'}")
                    print(f"  TEMPO DE JOGO: {entrada['tempo']}h")
                    print()
            else:
                print("HISTÓRICO: Nenhuma atualização")
            print()

def adicionar_jogo():
    try:
        quantos_jogos = int(input("\nQuantos jogos você quer adicionar?\n"))
        if quantos_jogos > 0:
            for i in range(quantos_jogos):
                nome_jogo = input(f"Digite o nome do jogo {i+1}: ")
                if encontrar_jogo(nome_jogo, silencioso = True):
                    print(f"\nO jogo '{nome_jogo}' já está cadastrado!\n")
                else:
                    cadastro_jogo = {
                        "nome": nome_jogo,
                        "tempo": 0.0,
                        "concluido": False,
                        "historico": []
                    }
                    lista.append(cadastro_jogo)
                    print(f"\nJogo {nome_jogo} adicionado com sucesso!\n")
                    escrever_dados(lista)
    except ValueError:
        print("\nNúmero inválido. Por favor, insira um número inteiro.\n")

def sobre_projeto():
    print("\nProjeto feito em Python para gerenciar jogos que quero zerar. Permite adicionar jogos, registrar o tempo de conclusão, acompanhar o histórico de atualizações e persistir os dados em um arquivo JSON. - By L0ki")

print("_" * 100)
print("\nBem vindo ao Gestor de Jogos!")
lista = carregar_dados()
print(f"Jogos armazenados no banco de dados: {len(lista)}\n")
print("_" * 100)
print("")

ABOUT = "ABOUT"
QUIT = "QUIT"
ADD = "ADD"
SHOW = "SHOW"
UPDATE = "UPDATE"
DELETE = "DELETE"

while True:
    comando = input("Por favor insira um dos comandos seguintes! \nComandos disponíveis: ABOUT - ADD - DELETE - UPDATE - SHOW - QUIT: \n").upper()

    if comando == ABOUT:
        print("_" * 100)
        sobre_projeto()
        print("_" * 100)
        print()

    elif comando == ADD:
        print("_" * 100)
        adicionar_jogo()
        print("_" * 100)
        print()

    elif comando == SHOW:
        print("_" * 100)
        print()
        mostrar_jogo()
        print("_" * 100)
        print()
    
    elif comando == UPDATE:
        print("_" * 100)
        nome_jogo_modificar = input("\nQual jogo você quer alterar o status?\n")
        update_jogo(nome_jogo_modificar)
        print("_" * 100)
        print()

    elif comando == DELETE:
        print("_" * 100)
        nome_jogo_deletar = input("\nQual jogo você quer excluir?\n")
        deletar_jogo(nome_jogo_deletar)
        print("_" * 100)
        print()

    elif comando == QUIT:
        print("_" * 100)
        print("\nSalvando jogos")
        escrever_dados(lista)
        print("\nSaindo do Gestor de Jogos.")
        print("Até mais!\n")
        print("_" * 100)
        print()
        break

    else:
        print("Comando não reconhecido.")
        print()