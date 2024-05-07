import random

room = []
state = ['S', '_'] 
room.append(random.choice(state))
room.append(random.choice(state))
sucesso = 0
back = 0

class vaccum:
         
        def __init__(self, position):
                self.position = position

        def esquerda():
                print('virando a esquerda\n')
        
        def direita():
                print('virando a direita\n')

        def out():
                print('saindo da sala\n')

        def limpar(position):
                global back
                i = position
                j = len(room) + 2
                clean = 0
                while(i != j - 1): #fazendo um while partindo de "position" varrendo o vetor até o final e quando chega no final, varre do final até o inicio 
                        if room[i] == 'S': #limpa a sala se ela está suja                              
                                a = 'limpando sala '
                                print(a + str(i))
                                room[i] = '_'
                                a = 'pontuação: '
                                global sucesso
                                sucesso += 1
                                print(a + str(sucesso))
                                vaccum.out()
                                return i
                        else: #imprimir se vai para direita esquerda ou faz nada
                                if back == 0 and i == len(room) - 1: 
                                        print('nada\n')#vaccum.esquerda()
                                elif back == 0:
                                        vaccum.direita()
                                elif back == 1 and i == 0:
                                        print('nada\n')#vaccum.direita()
                                else:
                                        vaccum.esquerda()
                        if back == 0: #define se irá mover para frente ou para trás o indice do vetor
                                i+=1
                        else:
                                i-=1
                        j = 0
                        if(i > len(room) - 1):#se chegar ao final do vetor mantem a posição
                                i = len(room) - 1
                                back = 1
                        
                 #verifica se todas as salas estão limpas
                print('todas as salas estão limpas: ')
                for z in range(len(room)):
                        print(room[z])
                print('\n')
                return position
                

class ambi:
        def __init__(self, position, repeat):
                self.position = position
                self.repeat = repeat
        
        def sujar(self,position, repeat): #função para sujar as salas aleatoriamente e ligar o aspirador
                i = 0
                global back
                print('iniciando aspirador\n')
                while(i < repeat):      
                        j = 0
                        for j in range(len(room) - 1): #fazendo um for para ter a possibilidade de sujar as salas a cada interação
                                if room[j] != 'S': #se a sala ja estiver suja n necessita sujar
                                        room[j] = random.choice(state)
                        position = vaccum.limpar(position) #chamando a função para o aspirador limpar a sujeira
                        back = 0
                        i = i + 1

                print('desligando aspirador\n')
                a = 'pontuação total(2): '
                print(a + str(sucesso))

