# -*- coding: utf-8 -*-
# EP 2019-1: Escape Insper
#
# Alunos: 
# - aluno A: Thalia Loiola Silva, thalials@al.insper.edu.br
# - aluno B: Marcos Vinínius da Silva, marcosvs3@al.insper.edu.br

#introdução
nome = input("Olá! Qual o seu nome? " )
print()
print("Bem-vindo(a), {0}! Está preparado(a) para uma grande aventura?!\nAproveite o jogo e ... cuidado com suas escolhas, "
      "pois elas podem te levar para muuuito longe!".format(nome))
enter = input("Aperte enter para continuar")
print()

def carregar_cenarios():
    cenarios = {
        "inicio": {
            "titulo": "Sala de estar",
            "descricao": "Voce esta na sala de estar da sua casa",
            "opcoes": {
                "ir de bike": "Você chegará ao Insper muito sujo, mas chegará!",
                "pedir um uber": "Está em horário de pico: pense bem!"
            }
        },
        "ir de bike": {
            "titulo": "A hora do Rush!",
            "descricao": "Você está na rua",
            "opcoes": {
                "inicio": "Desça da bike e volte andando para casa",
                "usar potencia total": "Pedale o mais rápido possível!"
            }
        },
        "usar potencia total": { #nesse momento, abrirá uma fenda que levara o jogador para outro mundo 
            "titulo": "A fenda",
            "descricao": "Você estava tão rápido que abriu uma fenda no espaço-tempo, te levando para outro mundo!",
            "opcoes": { 
                "opcao1" : "comentario1",
                "opcao2" : "comentario2"
                    } #aí só Jesus na causa
        },
        "pedir um uber": {
            "titulo": "Motorista tranquilo",
            "descricao": "Você pediu um uber, mas o motorista tem medo de ser multado por limite de velocidade...",
            "opcoes": {
                "inicio": "Fugir do carro no primeiro sinal vermelho e voltar correndo para casa!"
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
    #Retornando os dicionários
    cenarios, nome_cenario_atual = carregar_cenarios()

    game_over = False
    #enquanto não for fim de jogo:
    while not game_over:
        #Apresentando cenarios
        cenario_atual = cenarios[nome_cenario_atual]
        
       #titulo do cenário com os traços embaixo
        titulo_cenario = cenarios[nome_cenario_atual]["titulo"] 
        print(titulo_cenario)
        print("-"*len(titulo_cenario))
        
        #descrição do cenário
        print(cenarios[nome_cenario_atual]["descricao"])
        
        #Apresentação das escolhas que o jogador pode fazer dentro do cenario 
        #que ele estiver:
        opcoes = cenario_atual['opcoes']
        if len(opcoes) == 0:
            print("Acabaram-se suas opções! Mwo mwo mwooooo...")
            game_over = True
        else:
            #Parte do Marcos (aluno B): essa parte foi copiada do Cícero! 
            print("Escolha sua opção:")
            print()
            for escolha in opcoes:
                print('{0}: {1}'.format(escolha, opcoes[escolha]))
            #professor fez
            escolha = input("O que você vai fazer? ")
            print()
            
            if escolha in opcoes:
                nome_cenario_atual = escolha
            else:
                print("Sua indecisão foi sua ruína!")
                game_over = True

    print("Você morreu!")

# Programa principal.
if __name__ == "__main__":
    main()
