# EP 2019-1: Escape Insper
#
# Alunos: 
# - aluno A: Thalia Loiola Silva, thalials@al.insper.edu.br
# - aluno B: Marcos Vinínius da Silva, marcosvs3@al.insper.edu.br

#introdução
nome = input("Olá! Qual o seu nome? " )
print()
print("Bem-vindo(a), {0}! Está preparado(a) para uma grande aventura?!\nAproveite o jogo e ... cuidado com suas escolhas, "
      "pois elas podem te levar para longe!".format(nome))
enter = input("Aperte enter para continuar")
print()

def carregar_cenarios():
    cenarios = {
        "inicio": {
            "titulo": "Saguao do perigo",
            "descricao": "Voce esta no saguao de entrada do insper",
            "opcoes": {
                "andar professor": "Tomar o elevador para o andar do professor",
                "biblioteca": "Ir para a biblioteca"
            }
        },
        "andar professor": {
            "titulo": "Andar do desespero",
            "descricao": "Voce chegou ao andar da sala do seu professor",
            "opcoes": {
                "inicio": "Tomar o elevador para o saguao de entrada",
                "professor": "Falar com o professor"
            }
        },
        "professor": {
            "titulo": "O monstro do Python",
            "descricao": "Voce foi pedir para o professor adiar o EP. "
                         "O professor revelou que é um monstro disfarçado "
                         "e devorou sua alma.",
            "opcoes": {}
        },
        "biblioteca": {
            "titulo": "Caverna da tranquilidade",
            "descricao": "Voce esta na biblioteca",
            "opcoes": {
                "inicio": "Voltar para o saguao de entrada"
            }
        }
    }
    nome_cenario_atual = "inicio"
    return cenarios, nome_cenario_atual


def main():
    print("Na hora do sufoco!")
    print("------------------")
    print()
    print("Parecia uma ideia boa: Vou só assistir um novo episódio de "
         "'La Casa de Papel' enquanto espero o horário de ir para o Insper. "
         "Mas, certamente, isso não deu muito certo...")
    print()
    print("Ao olhar o grupo do Whatsapp da sala, você notou que haviam muitas"
          " mensagens no grupo e isso poderia significar duas coisas: Perigo ou"
          " zoeira. Infelizmente, não era a segunda opção... Você leu as "
          "mensagens e lembrou que havia um EP para entregar! E não somente "
          "isso: estava em casa e precisava chegar o quanto antes para entregar"
          " seu trabalho, pois o professor não aceitaria atrasos. Boa sorte! Pois"
          " os desafios estão apenas começando...")
    print()

    cenarios, nome_cenario_atual = carregar_cenarios()

    game_over = False
    while not game_over:
        cenario_atual = cenarios[nome_cenario_atual]

        print(nome_cenario_atual)
        print("-"*len(nome_cenario_atual))
        print(cenarios[nome_cenario_atual]["descricao"])

        opcoes = cenario_atual['opcoes']
        if len(opcoes) == 0:
            print("Acabaram-se suas opções! Mwo mwo mwooooo...")
            game_over = True
        else:

            # Aluno B: substitua este comentário e a linha abaixo pelo código
            # para pedir a escolha do usuário.
            escolha = ""

            if escolha in opcoes:
                nome_cenario_atual = escolha
            else:
                print("Sua indecisão foi sua ruína!")
                game_over = True

    print("Você morreu!")


# Programa principal.
if __name__ == "__main__":
    main()
