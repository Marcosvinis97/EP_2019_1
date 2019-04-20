# EP 2019-1: Escape Insper
# Disciplina: Design de Software 
# Professor: Fábio José Ayres
# Turma: 1B
# Alunos: 
# - Thalia Loiola Silva, thalials@al.insper.edu.br
# - Marcos Vinícius da Silva, marcosvs3@al.insper.edu.br

# INÍCIO DA INTRODUÇÃO
RED   = "\033[1;31m" 
RESET = "\033[0;0m"

print(RED + "Olá, Gamer!" + RESET)
print(RED + "Qual é o seu nome?" + RESET)
nome = input() # Indentificando o gamer;
print()

print(RED + "Bem-vindo(a)," + RESET, "{0}!".format(nome),RED + "\nEstá "
      "preparado(a) para uma grande aventura?!")
print()
print(RED + "Aproveite o jogo, mas tome cuidado com suas escolhas, pois elas podem "
      "te levar para muuuito longe!" + RESET) # Boas-vindas ao gamer;

enter = input(RED + "Aperte a tecla enter para continuar." + RESET) # Iniciando o Jogo;
print()
# FIM DA INTRODUÇÃO

# INÍCIO FUNÇÃO CENÁRIOS
def carregar_cenarios():
    cenarios = {
        "INICIO": {
            "titulo": "É HORA DE DAR NO PÉ",
            "descricao": "Você esta no portão de casa e deve decidir qual é"
            " a melhor opção para chegar até o Insper.",
            "opcoes": {
                "UBER": "Pode ser a opção mais rápida ou não!", #PODE SER A MAIS RÁPIDA/MAIS LENTA(TRANSITO)/MAIS SEGURA(CARRO BLINDADO)
                "BIKE": "Você chegará a tempo no Insper, mas estará fedendo!", #MAIS RAPIDA(DESVIA DO TRANSITO)/ALUNO FEDIDO E CANSADO(PROFESSOR NÃO ATENDE ALUNOS FEDIDOS)
                "CAMINHANDO": "Corre!!", #MAIS PERIGOSA/ALUNO NÃO CHEGA FEDIDO   
                "DESISTO": "Pegar DP não deve ser tão ruim assim..." #DESANIMO
            }
        },
        "UBER": {
            "titulo": "É HORA DO RUSH",
            "descricao": "A cidade está um caos e o motorista do Uber escolheu"
            " o pior caminho possível. Se continuar assim, você chegara no"
            " Insper após o seu fechamento.",
            "opcoes": {
                "BIKE": "Você chegará mais rápido! No entanto, chegará muito fedido "
                " e seu professor não gosta de alunos fedidos!", #MAIS RAPIDA(DESVIA DO TRANSITO)/ALUNO FEDIDO E CANSADO(PROFESSOR NÃO ATENDE ALUNOS FEDIDOS)
                "CAMINHANDO": "Pense bem: pode não dar para chegar a tempo!"
                " (pelo menos, não chegará fedendo)" , #MAIS PERIGOSA/ALUNO NÃO CHEGA FEDIDO 
                "DESISTO": "Pegar DP não deve ser tão ruim assim..." #DESANIMO
            }
        },
        "BIKE": { 
            "titulo": "A FENDA",
            "descricao": "Você pedalou rão rápido que acabou abrindo uma fenda"
            " no espaço-tempo, te levando para outro mundo.",
            "opcoes": { 
                "CONHECER O NOVO MUNDO" : "Atenção! Podem existir criaturas "
                " estranhas à solta",
                "DESISTO" : "É muita pressão! Prefiro a DP"
            } 
        },
        "CAMINHANDO": {
            "titulo": "texto",
            "descricao": "texto",
            "opcoes": {
                "BIKE": "texto",
                "DESISTIR": "texto"
            }
        },
        "CONHECER O NOVO MUNDO": {
            "titulo": "UNIVERSO PARALELO",
            "descricao": "Atenção: você foi levado para um lugar muito parecido "
            "com o novo prédio do Insper! Mas não se iluda: o lugar está tomado"
            " por monstros!",
            "opcoes": { 
                "PEGAR O ELEVADOR" : "Ande devagar, pois o local está escuro.",
                "RECEPCIONISTA" : "Aparenta ser uma boa criatura. Pegue informações com ele.",
            } 
        },
        "PEGAR O ELEVADOR": {
            "titulo": "ELEVADOR DA MORTE",
            "descricao": "Você está dentro do elevador, mas ele só consegue te"
            " levar para o 3° andar, onde fica o FabAlien. Caso aperte outro botão,"
            "o elevador despenca e vc perder o jogo. Mas, para isso, é necessário "
            "acertar a charada: qual o nome correto do professor de desoft? ",
            "opcoes": { 
                "FABYO AIRES" : "",
                "FABIO AYRES" : "",
                "DESISTO" : "Muito complexo"
            } 
        },
        "FABYO AIRES": { 
            "titulo": "VOCÊ MORREU!",
            "descricao": "Não foi dessa vez!",
            "opcoes": { 
            } 
        },
        "BIBLIOTECA": { 
            "titulo": "texto",
            "descricao": "texto",
            "opcoes": { 
                "OPÇÃO" : "texto",
                "OPÇÃO" : "texto",
                "DESISTIR" : "texto"
            } 
        },
        "ELEVADOR": {
            "titulo": "texto",
            "descricao": "texto",
            "opcoes": { 
                "OPÇÃO" : "texto",
                "OPÇÃO" : "texto",
                "DESISTIR" : "texto"
            }
        },
        "GARAGEM": { 
            "titulo": "texto",
            "descricao": "texto",
            "opcoes": { 
                "OPÇÃO" : "texto",
                "OPÇÃO" : "texto",
                "DESISTIR" : "texto"
            } 
        },
        "REFEITORIO": { 
            "titulo": "texto",
            "descricao": "texto",
            "opcoes": { 
                "OPÇÃO" : "texto",
                "OPÇÃO" : "texto",
                "DESISTIR" : "texto"
            } 
        },
        "SALA DO PROFESSOR": {
            "titulo": "texto",
            "descricao": "texto",
            "opcoes": { 
                "OPÇÃO" : "texto",
                "OPÇÃO" : "texto",
                "DESISTIR" : "texto"
            } 
        },
        "DESISTO": { 
            "titulo": "FRACOTE",
            "descricao": "Pobre jogador!" .format(nome),
            "opcoes": { 
            } 
        }
    }
    nome_cenario_atual = "INICIO"
    return cenarios, nome_cenario_atual
# FIM FUNÇÃO CERNÁRIOS

# INÍCIO FUNÇAO MONSTROS
def carrega_criaturas():
    personagens = {
            "TECNICO": { # jogador dentro do FabAlien
                    "opçoes de ação": {
                            "chute" : "Não é a melhor opção, mas é de fácil execução!",
                            "rasgar seu jaleco": "Você deixará ele sempre proteção!",
                            "fugir": "Você perderá tempo e pode ficar com zero na EP"
                    }
                         }, 
           "RECEPCIONISTA" : {
                   "opçoes de ação" : {
                           "OPCAO" : "TEXTO",
                           "OPCAO" : "TEXTO"
                           }
                   }
                }
    nome_personagem = "TECNICO"        
    return personagens, nome_personagem
# FIM FUNÇÃO MONSTROS 

def main():
    BLUE  = "\033[1;34m"
    RED   = "\033[1;31m" 
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
    print(RED + "Boa sorte," + RESET, " {0}." .format(nome), RED + " Pois os desafios estão apenas começando..." + RESET)
    print()

    enter2 = input(RED + "Aperte a tecla enter para continuar." + RESET) # Continuando o Jogo;
    print()
    
    # Dicionário - Início;
    cenarios, nome_cenario_atual = carregar_cenarios()
    personagens, nome_personagem = carrega_criaturas()
    game_over = False
    
    while not game_over:
        cenario_atual = cenarios[nome_cenario_atual]
        #personagem = personagens[nome_personagem]
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
            escolha = input(RED + "Digite sua escolha: " + RESET) # Decisão do gamer;
            print()
            
            #O jogo continua para o gamer;
            if escolha in opcoes:
                nome_cenario_atual = escolha
                
            #O jogo termina para o gamer;  
            else:
                print()
                print(RED + "Sua indecisão foi sua ruína!" + RESET)
                print()
                game_over = True

    print(RED + "Infelizmente" + RESET, "{0}," .format(nome), RED + "você morreu!" + RESET)

# Programa principal.
if __name__ == "__main__":
    main()

