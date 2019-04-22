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

print(RED + "Bem-vindo(a)," + RESET, "{0}!".format(nome),RED + "\n\nEstá "
      "preparado(a) para uma grande aventura?!")
print()
print(RED + "Aproveite o jogo, mas tome cuidado com suas escolhas, pois elas "
      "podem "
      "te levar para muuuito longe!" + RESET) # Boas-vindas ao gamer;
# Iniciando o Jogo
enter = input(RED + "Aperte a tecla enter para continuar." + RESET) 
print()
# FIM DA INTRODUÇÃO

# INÍCIO FUNÇÃO CENÁRIOS
def carregar_cenarios():
    cenarios = {
        "INICIO": {
            "titulo": "É HORA DE DAR NO PÉ",
            "descricao": "Você esta no portão de casa e deve decidir qual é a "
            "melhor opção para chegar até o Insper.",
            "opcoes": {
                "UBER": "Pode ser a opção mais rápida ou não, pois a cidade "
                "está um caos neste dia de entrega... Vai arriscar?",
                "BIKE": "Você chegará a tempo no Insper, entretanto, "
                "provavelmente estará fedendo e o Mestre Ayres não gosta de "
                "alunos fedidos... ",
                "CORRENDO": "Correndo você podera desviar do trânsito, "
                "entretanto, há boatos de ataques a corredores ao redor "
                "do Insper...Vai arriscar?",   
                "DESISTO": "Pegar DP não deve ser tão ruim assim..." 
            }
        },
        "UBER": {
            "titulo": "É HORA DO RUSH",
            "descricao": "A cidade está um caos por conta das entregas dos "
            "EP's e o motorista do Uber escolheu o pior caminho possível. "
            "Se continuar assim, você chegara no Insper após o horário "
            "limite da entrega... Você ainda tem chances!! Tem outras opções!",
            "opcoes": {
                "BIKE": "Você chegará a tempo no Insper, entretanto, "
                "provavelmente estará fedendo e o Mestre Ayres não gosta de "
                "alunos fedidos... ",
                "CORRENDO": "Correndo você podera desviar do transito, "
                "entretanto, há boatos de que Alunos Corredores estão "
                "desaparecendo ao redor do Insper...Vai arriscar?", 
                "DESISTO": "Pegar DP não deve ser tão ruim assim..."
            }
        },
        "BIKE": { 
            "titulo": "A FENDA",
            "descricao": "CARAMBAAAA!!!! Você pedalou tão rápido que acabou abrindo uma fenda "
            "no espaço-tempo, te levando para OUTRA DIMENSÃO!!!! Louco, não?!? E agora, o que você vai fazer??",
            "opcoes": { 
                "CONHECER NOVO MUNDO": "Que lugar é esse?!?! Tente encontrar "
                "uma maneira de sair para entregar seu EP!!",
                "DESISTO" : "Pesgar DP não deve ser tão ruim assim... Espere "
                "por socorro ai mesmo, vão sentir sua falta em algum momento. Ou não... rsrsrs!"
            } 
        },
        "CORRENDO": {
            "titulo": "QUEM AVISA AMIGO É",
            "descricao": "Essa é uma escolha arriscada, pois há diversos alunos"
            " desaparecendo ao redor do Insper, sem explicação, "
            "deseja continuar?? Depois não vai dizer que não foi avisado!",
            "opcoes": {
                "UBER": "Pode ser a opção mais rápida ou não, pois a cidade "
                "está um caos neste dia de entrega... Vai arriscar?",
                "BIKE": "Você chegará a tempo no Insper, entretanto, "
                "provavelmente estará fedendo e o Mestre Ayres não gosta "
                "de alunos fedidos... ",
                "CONTINUAR": "Tenha noção de que fazer isso é extremamente arriscado!", 
                "DESISTO": "Pegar DP não deve ser tão ruim assim..."
            }
        },
        "CONHECER NOVO MUNDO": {
            "titulo": "UNIVERSO PARALELO",
            "descricao": "Atenção: Você foi levado para um lugar muito parecido"
            " com o prédio novo do Insper!! Será que o professor está ai?? O tempo está acabando!!",
            "opcoes": { 
                "ELEVADOR" : "Será que o Mestre Ayres está neste prédio? Talvez"
                " ele esteja aqui mesmo... Que tal subir até o andar dele para "
                "conferir...",
                "RECEPCIONISTA" : "Aparenta ser uma pessoa boa. Será que ela "
                "ajudaria com informações?",
                "DESISTIR" : "Pegar DP não deve ser tão ruim assim. Que "
                "tal ficar na recepção mesmo... Esperando por ajuda."
            } 
        },
        "ELEVADOR": {
            "titulo": "TUDO OU NADA",
            "descricao": "Você não devia ter feito isto... Neste momento você "
            "está dentro do elevador, mas ele só consegue te levar para o 3º "
            "andar, onde fica o FabAlien!?!. Entretanto, para a porta do elevador "
            "abrir é necessário acertar a pergunta: Como se escreve "
            "corretamente o nome do professor de DESOFT? Vale resaltar que caso"
            " você erre a pergunta o elevador despenca... rsrsrs",
            "opcoes": { 
                "FABIO AYRES" : "Será?",
                "FÁBIO AIRES" : "Será?",
                "FÁBIO AYRES" : "Será?"
            } 
        },
        "FÁBIO AYRES": { 
            "titulo": "PARABÉNS",
            "descricao": "Você conseguiu chegar ao 3° andar, onde fica o "
            "FabAlien. Mas todo cuidado é pouco!",
            "opcoes": { 
                "ENTRAR" : "Vá em frente! O tempo está quase acabando!",
                "DESISTIR" : "Pegar DP não deve ser tão ruim assim. Que tal "
                "ficar na recepção mesmo... Esperando por ajuda."
            } 
        },
        "ENTRAR": {
            "titulo": "LUTE OU MORRA!",
            "descricao": "Por essa você não esperava: o técnico do FabAlien "
            "está empenhado em não te deixar entregar a EP a tempo. Você "
            "precisa detê-lo!",
            "opcoes": { 
                "RASGAR SEU JALECO" :"Você deixará ele sempre proteção!",
                 "FUGIR": "Você perderá tempo e pode ficar com zero na EP",
            } 
        },
         "RASGAR SEU JALECO": {
            "titulo": "VOCÊ CONSEGUIU!",
            "descricao": "Parabéns!! 10 pontos pela conquista! "
            "A vitória está próxima! ",
            "opcoes": { 
                "MAQUINA 3D" : "Aquela máquina está chamando mais "
                "atenção que as demais! O que será que tem nela...?",
            } 
        },
         "MAQUINA 3D": {
            "titulo": "UAU!",
            "descricao": "O técnico estava trabalhando em um novo projeto e, "
            "aparentemente, havia impresso uma outra fenda no espaço-tempo!",
            "opcoes": {     
             "ENTRAR NA FENDA" : "Não se sabe o que exatamente vai acontecer.",
             "DESISTO" : "Tem nem perigo! Prefiro pegar DP." 
            } 
        },
        "ENTRAR NA FENDA": {
            "titulo": "ONDE ESTOU?",
            "descricao": "Não sabemos ao certo, mas parece que você conseguiu "
            "voltar à Terra e melhor ainda: a fenda te levou direto ao Insper!"
            " Parabéns pela decisão! Você ganhou 8 pontos.",
            "opcoes": {     
             "SALA DOS PROFESSORES" : "Rápido!! O tempo está se esgotando!",
             "SUJINHOS": "Hoje é sexta... O professor deve entender"
            } 
        },
        "SALA DOS PROFESSORES": {
            "titulo": "UFA!!",
            "descricao": "Você chegou a tempo! O professor está lá sentado, "
            "esperando ansiosamente pela sua EP. ",
            "opcoes": {     
             "ENTREGAR EP" : "Entregue enquanto há tempo!",
             "OBSERVAR" : "Ele não se parece muito com o Mestre Ayres... Pense "
             "bem antes de entregar a EP."
            } 
        },
        "ENTREGAR EP": {
            "titulo": "AS APARÊNCIAS ENGANAM!",
            "descricao": "O mestre Ayres não é quem parecia ser. A criatura era "
            "monstro que se alimenta de EP'S. Você deixou ele mais forte!",
            "opcoes": {     
            } 
        },
        "OBSERVAR": {
            "titulo": "ALGO DE ERRADO NÃO ESTÁ CERTO",
            "descricao": "Sábia escolha! Porém, o professor notou sua presença!"
            " Você não está na Terra. Está em outra dimensão e esse professor é"
            "na verdade uma criatura faminta. Lute enquanto pode!",
            "opcoes": {  
            "ENTREGAR EP" : "Depois de tudo o que você passou, pode ser coisa da "
            "sua cabeça...",
            "NOTEBOOK" : "Quebre o notebook dele! Ele perde forças nesse ato."
            
            } 
        },
        "NOTEBOOK": {
            "titulo": "VOCÊ DERROTOU A CRIATURA, MAS O TEMPO TE DERROTOU.",
            "descricao": "UAU! Houve uma explosão e você voltou para sua casa,"
            "mas esqueceu que o tempo é medido de forma diferente quando se está em outra dimensão... "
            "Se passaram 50 anos desde aquele dia que você estava na sala assistindo "
            "Netflix. Infelizmente, seu professor não aceita atrasos.",
            "opcoes": {
            } 
        },
         "SUJINHOS": {
            "titulo": "QUE FEIO!",
            "descricao": "Vai mesmo deixar o professor te esperando? ",
            "opcoes": {     
            } 
        },
         "FUGIR": {
            "titulo": "FRACOTE!",
            "descricao": "Te pegamos. Você não tem opção a não ser lutar! Você "
            "perdeu 7 pontos por ser medroso.",
            "opcoes": {     
             "ENTRAR" : "Deixa de moleza."
            } 
        },
            "RECEPCIONISTA": { 
            "titulo": "QUE VENÇA O MELHOR!",
            "descricao": "A recepcionista está com FOME DE HUMANOS!!! Você precisa"
            " entrar no combate com ela AGORA se quiser seguir em frente!",
            "opcoes": { 
                    "VOADORA" : "Dê uma voadora na recepcionista!",
                    "CHUTAR" : "Chute o mais forte que conseguir!" 
            } 
        },
            "VOADORA": { 
            "titulo": "ISSO AÍ!",
            "descricao": "Você acertou em cheio e ganhou 4 pontos! Agora a "
            "recepcionista não será mais um problema.",
            "opcoes": { 
                    "ELEVADOR" : "Vá para o elevador e volte a conhecer onde "
                    "você está!"
            } 
        },
             "CHUTAR": { 
            "titulo": "FRACOTE",
            "descricao": "Você não estava forte suficiente.",
            "opcoes": { 
            } 
        },
            "DESISTO": { 
            "titulo": "FRACOTE",
            "descricao": "Pobre jogador!",
            "opcoes": { 
            } 
        },
        "CONTINUAR": { 
            "titulo": "TEIMOSO!",
            "descricao": "Você foi sequestrado por Técnicos do FabAlien, isso mesmo, FabAlien. Agora você sera cobaia para experiências com alunos que gostam de atrasos!",
            "opcoes": { 
            } 
        },
        "FABIO AYRES": { 
            "titulo": "ERROUU",
            "descricao": "Pobre jogador! É Fábio Ayres.",
            "opcoes": { 
            } 
        },
        "FÁBIO AIRES": { 
            "titulo": "ERROUU",
            "descricao": "Pobre jogador! É Fábio Ayres.",
            "opcoes": { 
            } 
        }            
    }
    nome_cenario_atual = "INICIO"
    return cenarios, nome_cenario_atual
# FIM FUNÇÃO CERNÁRIOS

def main():
    BLUE  = "\033[1;34m"
    RED   = "\033[1;31m" 
    GREEN = "\033[0;32m"
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
          "mensagens e lembrou que havia um EP para entregar para o seu Mestre, o professor Ayres! E não somente "
          "isso: você estava em casa e precisava chegar O QUANTO ANTES no Insper para entregar seu EP,"
          " pois o professor não aceitaria atrasos." + RESET)
    print()
    print(RED + "Boa sorte," + RESET, " {0}." .format(nome), RED + " Pois os desafios estão apenas começando..." + RESET)
    print()

    enter2 = input(RED + "Aperte a tecla enter para continuar." + RESET) # Continuando o Jogo;
    print()
    # Dicionário - Início;
    cenarios, nome_cenario_atual = carregar_cenarios()
    pontuacao = 0
    
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
            print()
            print(RED + "Você chateou muito o Mestre Ayres. E ele não tem piedade." + RESET)
            print()
            game_over = True
            
        else:
            print()
            print("Pontuação = {0}".format(pontuacao))
            print()
            print(RED + "Escolha sua opção:" + RESET)
            print()

            for escolha in opcoes:
                print(GREEN + '{0}: {1}'.format(escolha, opcoes[escolha]) + RESET)
                print()
            
            print(RED + "E então, o que vai fazer?!?" + RESET)
            escolha = input(RED + "Digite sua escolha: " + RESET) # Decisão do gamer;
            print()
            
            #O jogo continua para o gamer;
            if escolha in opcoes:
                nome_cenario_atual = escolha
                if nome_cenario_atual == "RECEPCIONISTA":
                    pontuacao += 4
                if nome_cenario_atual == "RASGAR SEU JALECO":
                    pontuacao += 10
                if nome_cenario_atual == "ENTRAR NA FENDA":
                    pontuacao += 8
                if nome_cenario_atual == "FUGIR":
                    pontuacao -= 7
                if nome_cenario_atual == "SUJINHOS":
                    pontuacao -= 2
                
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