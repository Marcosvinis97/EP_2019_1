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

print(RED + "Bem-vindo(a)," + RESET, "{0}!".format(nome),RED + "\nEstá preparado(a) para uma grande aventura?!")
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
            "descricao": "Você esta no portão de casa e deve decidir qual é a melhor opção para chegar até o Insper.",
            "opcoes": {
                "UBER": "Pode ser a opção mais rápida ou não, pois a cidade está um caos neste dia de entrega... Vai arriscar?",
                "BIKE": "Você chegará a tempo no Insper, entretanto, provavelmente estará fedendo e o Mestre Ayres não gosta de alunos fedidos... ",
                "CORRENDO": "Correndo você podera desviar do transito, entretanto, há boatos de ataques a corredores ao redor do Insper...Vai arriscar?",   
                "DESISTO": "Pegar DP não deve ser tão ruim assim..." 
            }
        },
        "UBER": {
            "titulo": "É HORA DO RUSH",
            "descricao": "A cidade está um caos por conta das entregas dos EP's e o motorista do Uber escolheu o pior caminho possível. Se continuar assim, você chegara no Insper após o horário limite da entrega.",
            "opcoes": {
                "BIKE": "Você chegará a tempo no Insper, entretanto, provavelmente estará fedendo e o Mestre Ayres não gosta de alunos fedidos... ",
                "CORRENDO": "Correndo você podera desviar do transito, entretanto, há boatos de que Alunos Corredores estão desaparecendo ao redor do Insper...Vai arriscar?", 
                "DESISTO": "Pegar DP não deve ser tão ruim assim..."
            }
        },
        "BIKE": { 
            "titulo": "A FENDA",
            "descricao": "Você pedalou tão rápido que acabou abrindo uma fenda no espaço-tempo, te levando para outro mundo!! Louco, não?!?",
            "opcoes": { 
                "CONHECER NOVO MUNDO": "Que lugar é esse?!?! Tente encontrar uma maneira de entregar seu EP!! Ou tente sair o mais rápido possível!!",
                "DESISTO" : "Pesgar DP não deve ser tão ruim assim... Espere por socorro!"
            } 
        },
        "CORRENDO": {
            "titulo": "QUEM AVISA AMIGO É",
            "descricao": "Essa é uma escolha arriscada, pois há diversos alunos desaparecendo ao redor do Insper, sem explicação, deseja continuar?? Depois não vai dizer que não avisei! rsrs",
            "opcoes": {
                "BIKE": "Você chegará a tempo no Insper, entretanto, provavelmente estará fedendo e o Mestre Ayres não gosta de alunos fedidos... ",
                "DESISTO": "Pegar DP não deve ser tão ruim assim..."
            }
        },
        "CONHECER NOVO MUNDO": {
            "titulo": "UNIVERSO PARALELO",
            "descricao": "Atenção: Você foi levado para um lugar muito parecido com o prédio novo do Insper!! Mas não se iluda, você não está no seu mundo!",
            "opcoes": { 
                "ELEVADOR" : "Será que o Mestre Ayres está neste prédio? Talvez ele esteja aqui mesmo... Que tal subir até o andar dele para conferir...",
                "RECEPCIONISTA" : "Aparenta ser uma pessoa boa. Será que ela ajudaria com informações? rsrs Cuidado!",
                "DESISTIR" : "Pegar DP não deve ser tão ruim assim. Que tal ficar na recepção mesmo... Esperando por ajuda."
            } 
        },
        "ABRIGO": {
            "titulo": "texto",
            "descricao": "texto",
            "opcoes": { 
                "OPÇÃO" : "texto",
                "OPÇÃO" : "texto",
                "DESISTIR" : "texto"
            } 
        },
        "INSPER": { 
            "titulo": "texto",
            "descricao": "texto",
            "opcoes": { 
                "OPÇÃO" : "texto",
                "OPÇÃO" : "texto",
                "DESISTIR" : "texto"
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
def carrega_monstros():
    personagens = {
            "tecnico do FabAlien": { # jogador dentro do FabAlien
                    "opçoes de luta": {
                            "chute" : "Não é a melhor opção, mas é de fácil execução!",
                            "rasgar seu jaleco": "Você deixará ele sempre proteção!",
                            "fugir": "Você perderá tempo e pode ficar com zero na EP"}
            },
            "Mestre Ayres": { # jogador dentro do FabAlien/poderes telepaticos
                    "opçoes de luta": {
                            "chute" : "Não é a melhor opção, mas é de fácil execução!",
                            "rasgar seu jaleco": "Você deixará ele sempre proteção!",
                            "fugir": "Você perderá tempo e pode ficar com zero na EP"}
            }
        }
    return personagens
# FIM FUNÇÃO MONSTROS 

def main():
    BLUE  = "\033[1;34m"
    RED   = "\033[1;31m" 
    RESET = "\033[0;0m"
    
    # Contextualizando o início do jogo para o gamer;        
    print(BLUE + "NA HORA DO SUFOCO" + RESET)
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
            print()

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
