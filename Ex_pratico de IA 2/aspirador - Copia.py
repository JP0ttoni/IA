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

        def limpar(position):
                global back
                if room[position]  == 'S': #limpa a sala se ela está suja
                        a = 'limpando sala '
                        print(a + str(position))
                        room[position] = '_'
                        a = 'pontuação: '
                        global sucesso
                        sucesso += 1
                        print(a + str(sucesso))
                else: #não faz nada se a sala ja está limpa
                        b = 'sala '
                        c = ' ja está limpa'
                        print(b + str(position) + c)
                #printando de acordo com a posição que o aspirador vai se mexer
                if back == 0 and position == len(room) - 1:
                        vaccum.esquerda()
                elif back == 0:
                        vaccum.direita()
                elif back == 1 and position == 0:
                        vaccum.direita()
                else:
                        vaccum.esquerda()

                if back == 0 : #move pra frente o indice do vetor
                        position += 1   
                
                if back == 1:#move pra tras o indice do vetor
                        position -= 1

                if position > len(room) - 1:#se chegar no final mantém a posição e começa a varrer pra tras
                        position = len(room) - 1 
                
                if position < 0:#se chega no inicio mantem a posição e começa a varrer pra frente
                        position = 0
                        

                return position

class ambiente:
        def __init__(self, position, repeat):
                self.position = position
                self.repeat = repeat
        
        def sujar(self,position, repeat): #função para sujar as salas aleatoriamente e ligar o aspirador
                global back
                i = 0
                j = 0
                print('iniciando aspirador: \n')
                while(i < repeat):                     
                        if room[position] != 'S': #se a sala ja estiver suja n necessita sujar
                                room[position] = random.choice(state)

                        position = vaccum.limpar(position) #chamando a função para o aspirador limpar a sujeira
                        i = i + 1
                        if back == 0:
                                j += 1
                        else:
                                j -=1

                        if j > len(room) - 1: #se chegar no final mantém a posição e começa a varrer pra tras
                                j = len(room) - 1
                                back = 1
                        if j < 0: #se chega no inicio mantem a posição e começa a varrer pra frente
                                j = 0
                                back = 0
                print('desligando aspirador\n')
                a = 'pontuação total (1): '
                print(a + str(sucesso))

