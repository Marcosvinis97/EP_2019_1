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

print(RED + "Olá, Gamer!" + RESET)
print(RED + "Qual é o seu nome?" + RESET)
nome = input() #Indentificando o gamer;
print()

print(RED + "Bem-vindo(a)," + RESET, "{0}!".format(nome),RED + "\nEstá preparado(a) para uma grande aventura?!\n"
      "Aproveite o jogo, mas tome cuidado com suas escolhas, pois elas podem "
      "te levar para muuuito longe!" + RESET) #Boas vindas ao gamer;

enter = input(RED + "Aperte a tecla enter para continuar." + RESET) #Iniciando o Jogo;
print()
#FIM DA INTRODUÇÃO

#INÍCIO FUNÇÃO CENÁRIOS
def carregar_cenarios():
    cenarios = {
        "INICIO": {
            "titulo": "É HORA DE DAR NO PÉ",
            "descricao": "Você esta no portão de casa e deve decidir qual é a melhor opção para chegar até o Insper.",
            "opcoes": {
                "UBER": "texto", #PODE SER A MAIS RÁPIDA/MAIS LENTA(TRANSITO)/MAIS SEGURA(CARRO BLINDADO)
                "BIKE": "texto", #MAIS RAPIDA(DESVIA DO TRANSITO)/ALUNO FEDIDO E CANSADO(PROFESSOR NÃO ATENDE ALUNOS FEDIDOS)
                "CAMINHANDO": "texto", #MAIS PERIGOSA/ALUNO NÃO CHEGA FEDIDO   
                "DESISTO": "texto" #DESANIMO
            }
        },
        "UBER": {
            "titulo": "É HORA DO RUSH",
            "descricao": "A cidade está um caos e o motorista do Uber escolheu o pior caminho possível. Se continuar assim, você chegara no Insper após o seu fechamento.",
            "opcoes": {
                "BIKE": "texto", #MAIS RAPIDA(DESVIA DO TRANSITO)/ALUNO FEDIDO E CANSADO(PROFESSOR NÃO ATENDE ALUNOS FEDIDOS)
                "CAMINHANDO": "texto", #MAIS PERIGOSA/ALUNO NÃO CHEGA FEDIDO 
                "DESISTO": "texto" #DESANIMO
            }
        },
        "BIKE": { 
            "titulo": "A FENDA",
            "descricao": "Você pedalou rão rápido que acabou abrindo uma fenda no espaço-tempo, te levando para outro mundo.",
            "opcoes": { 
                "conhecer o novo mundo" : "Atenção! Podem existir criaturas estranhas à solta!",
                "opcao2" : "comentario2",
                "opcao3" : "..."
            } 
        },
        "CAMINHANDO": {
            "titulo": "MOTORISTA TRANQUILO",
            "descricao": "Você pediu um uber, mas o motorista tem medo de ser multado por limite de velocidade...",
            "opcoes": {
                "inicio": "Fugir do carro no primeiro sinal vermelho e voltar correndo para casa!"
            }
        },
        "4": { #nesse momento, abrirá uma fenda que levara o jogador para outro mundo 
            "titulo": "A fenda",
            "descricao": "Você estava tão rápido que abriu uma fenda no espaço-tempo, te levando para outro mundo!",
            "opcoes": { 
                "conhecer o novo mundo" : "Atenção! Podem existir criaturas estranhas à solta!",
                "opcao2" : "comentario2",
                "opcao3" : "..."
            } 
        },
        "5": { #nesse momento, abrirá uma fenda que levara o jogador para outro mundo 
            "titulo": "A fenda",
            "descricao": "Você estava tão rápido que abriu uma fenda no espaço-tempo, te levando para outro mundo!",
            "opcoes": { 
                "conhecer o novo mundo" : "Atenção! Podem existir criaturas estranhas à solta!",
                "opcao2" : "comentario2",
                "opcao3" : "..."
            } 
        },
        "6": { #nesse momento, abrirá uma fenda que levara o jogador para outro mundo 
            "titulo": "A fenda",
            "descricao": "Você estava tão rápido que abriu uma fenda no espaço-tempo, te levando para outro mundo!",
            "opcoes": { 
                "conhecer o novo mundo" : "Atenção! Podem existir criaturas estranhas à solta!",
                "opcao2" : "comentario2",
                "opcao3" : "..."
            } 
        },
        "7": { #nesse momento, abrirá uma fenda que levara o jogador para outro mundo 
            "titulo": "A fenda",
            "descricao": "Você estava tão rápido que abriu uma fenda no espaço-tempo, te levando para outro mundo!",
            "opcoes": { 
                "conhecer o novo mundo" : "Atenção! Podem existir criaturas estranhas à solta!",
                "opcao2" : "comentario2",
                "opcao3" : "..."
            } 
        },
        "8": { #nesse momento, abrirá uma fenda que levara o jogador para outro mundo 
            "titulo": "A fenda",
            "descricao": "Você estava tão rápido que abriu uma fenda no espaço-tempo, te levando para outro mundo!",
            "opcoes": { 
                "conhecer o novo mundo" : "Atenção! Podem existir criaturas estranhas à solta!",
                "opcao2" : "comentario2",
                "opcao3" : "..."
            } 
        },
        "DESISTO": { 
            "titulo": "FRACOTE",
            "descricao": "Pobre {0}!" .format(nome),
            "opcoes": { 
            } 
        }
    }
    nome_cenario_atual = "INICIO"
    return cenarios, nome_cenario_atual
#FIM FUNÇÃO CERNÁRIOS

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
    print(RED + "Boa sorte! Pois os desafios estão apenas começando..." + RESET)
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
            print(RED + "Você chateou muito o Mestre Ayres. E ele não tem piedade." + RESET)
            print()
            game_over = True
            
        else:
            print()
            print(RED + "Escolha sua opção:" + RESET)

            for escolha in opcoes:
                print(RED + '{0}: {1}'.format(escolha, opcoes[escolha]) + RESET)
                
            print()
            print(RED + "E então, o que vai fazer?!?" + RESET)
            escolha = input(RED + "Digite sua escolha: " + RESET)
            
            #O jogo continua para o gamer;
            if escolha in opcoes:
                nome_cenario_atual = escolha
                
            #O jogo termina para o gamer;  
            else:
                print(RED + "Sua indecisão foi sua ruína!" + RESET)
                print()
                game_over = True

    print(RED + "Infelizmente {0}, você morreu!" .format(nome) + RESET)

# Programa principal.
if __name__ == "__main__":
    main()



    

