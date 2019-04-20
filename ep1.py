# EP 2019-1: Escape Insper
# Disciplina: Design de Software 
# Professor: Fábio José Ayres
# Turma: 1B
# Alunos: 
# - Thalia Loiola Silva, thalials@al.insper.edu.br
# - Marcos Vinícius da Silva, marcosvs3@al.insper.edu.br

#INÍCIO DA INTRODUÇÃO
RED   = "\033[1;31m" 
RESET = "\033[0;0m"
GREEN = "\033[0;32m"

print(RED + "Olá Gamer!" + RESET)
print(GREEN + "Qual é o seu nome?" + RESET)
nome = input() #Indentificando o gamer;
print()

print(RED + "Bem-vindo(a), {0}! Está preparado(a) para uma grande aventura?!\n"
      "Aproveite o jogo, mas tome cuidado com suas escolhas, pois elas podem "
      "te levar para muuuito longe!" .format(nome)  + RESET) #Boas vindas ao gamer;

enter = input(GREEN + "Aperte a tecla enter para continuar." + RESET) #Iniciando o Jogo;
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
    GREEN = "\033[0;32m"
    RESET = "\033[0;0m"
    
    # Contextualizando o início do jogo para o gamer;        
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
    
    # Dicionário - Início;
    cenarios, nome_cenario_atual = carregar_cenarios()

    game_over = False
    while not game_over:
        cenario_atual = cenarios[nome_cenario_atual]
        
        # Título do cenário atual;
        titulo_cenario = cenarios[nome_cenario_atual]["titulo"] 
        print(BLUE + titulo_cenario + RESET)
        print(BLUE + "-"*len(titulo_cenario) + RESET)
        
        # Descrição do cenário atual;
        print(RED + cenarios[nome_cenario_atual]["descricao"] + RESET)
        
        # Opções do gamer no cenário atual;
        opcoes = cenario_atual['opcoes']
        if len(opcoes) == 0: # O jogo termina para o gamer;
            print(RED + "Acabaram-se suas opções! Mwo mwo mwooooo..." + RESET)
            print()
            game_over = True
            
        else:
            print(RED + "Escolha sua opção:" + RESET)
            print()
            
            for escolha in opcoes:
                print(RED + '{0}: {1}'.format(escolha, opcoes[escolha]) + RESET)
                
            print()    
            print(RED + "E então, o que vai fazer?!?" + RESET)
            escolha = input(RED + "Digite o número da sua escolha:\n" + RESET)
            
            #O jogo continua para o gamer;
            if escolha in opcoes:
                nome_cenario_atual = escolha
                
            #O jogo termina para o gamer;  
            else:
                print(RED + "Sua indecisão foi sua ruína!" + RESET)
                print()
                game_over = True

    print(RED + "Você morreu!" + RESET)

# Programa principal.
if __name__ == "__main__":
    main()



    

