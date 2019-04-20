# EP 2019-1: Escape Insper
# Disciplina: Design de Software 
# Professor: Fábio José Ayres
# Turma: 1B
# Alunos: 
# - aluno A: Thalia Loiola Silva, thalials@al.insper.edu.br
# - aluno B: Marcos Vinícius da Silva, marcosvs3@al.insper.edu.br

#INÍCIO DA INTRODUÇÃO
RED   = "\033[1;31m" 
RESET = "\033[0;0m"

print(RED + "Olá, GAMER!\nQual é o seu nome?" + RESET) 

#Indentificando o gamer;
nome = input()
print()

#Boas vindas ao gamer;
print(RED + "Bem-vindo(a), {0}! Está preparado(a) para uma grande aventura?!\n"
      "Aproveite o jogo, mas tome cuidado com suas escolhas, pois elas podem "
      "te levar para muuuito longe!" .format(nome)  + RESET)

#Iniciando o Jogo;
enter = input(RED + "Aperte a tecla enter para continuar." + RESET)
print()
#FIM DA INTRODUÇÃO

def carregar_cenarios():
    cenarios = {
        "inicio": {
            "titulo": "Saindo de casa!",
            "descricao": "Você esta no portão de casa e deve decidir qual é a opção mais rápida de chegar até o Insper.",
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
                "conhecer o novo mundo" : "Atenção! Podem existir criaturas estranhas à solta!",
                "opcao2" : "comentario2",
                "opcao3" : "..."
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

def carrega_monstros():
    personagens = {
            "tecnico do FabAlien": { #jogador dentro do FabAlien
                    "opçoes de luta": {
                            "chute" : "Não é a melhor opção, mas é de fácil execução!",
                            "rasgar seu jaleco": "Você deixará ele sempre proteção!",
                            "fugir": "Você perderá tempo e pode ficar com zero na EP"}}
                }
            
    return personagens


def main():
    BLUE  = "\033[1;34m"
    RED   = "\033[1;31m" 
    RESET = "\033[0;0m"
    
    #Contextualizando o início do jogopara o gamer;        
    print(BLUE + "Na hora do sufoco!" + RESET)
    print(BLUE + "------------------" + RESET)
    print()
    print(RED + "Parecia uma ideia boa: Vou só assistir um novo episódio de "
         "'La Casa de Papel' enquanto espero o horário de ir para o Insper. "
         "Mas, certamente, isso não deu muito certo..." + RESET)
    print()
    print(RED + "Ao olhar o grupo do Whatsapp da sala, você notou que haviam muitas"
          " mensagens no grupo e isso poderia significar duas coisas: Perigo ou"
          " zoeira. Infelizmente, não era a segunda opção... Você leu as "
          "mensagens e lembrou que havia um EP para entregar! E não somente "
          "isso: estava em casa e precisava chegar o quanto antes para entregar"
          " seu trabalho, pois o professor não aceitaria atrasos." + RESET)
    print()
    print(BLUE + "Boa sorte! Pois os desafios estão apenas começando..." + RESET)
    print()
    
    #Retornando aos Dicionários - Início;
    cenarios, nome_cenario_atual = carregar_cenarios()

    game_over = False
    while not game_over:
        #Apresentando cenarios
        cenario_atual = cenarios[nome_cenario_atual]
        
        #Título do cenário atual;
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
            #Parte do Marcos (aluno B):
            print("Escolha sua opção:")
            print()
            for escolha in opcoes:
                print('{0}: {1}'.format(escolha, opcoes[escolha]))
            #professor fez
            escolha = input("O que você vai fazer? ")
            print()
            
            if escolha in opcoes:
                nome_cenario_atual = escolha
                
                
            #Termina o jogo para o gamer;   
            else:
                print(RED + "Sua indecisão foi sua ruína!" + RESET)
                game_over = True

    print(RED + "Você morreu!" + RESET)

# Programa principal.
if __name__ == "__main__":
    main()


    

