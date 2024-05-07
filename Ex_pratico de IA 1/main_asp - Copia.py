#from aspirador_2 import ambi
from aspirador import ambiente
 
ambnt = ambiente(0, 1000) #definindo que o aspirador vai começar na sala 0 e vai repetir o processo 1000 vezes
ambnt.sujar(0, 1000)

#ambnt = ambi(0,1000) #definindo que o aspirador vai começar na sala 0 e vai repetir o processo 1000 vezes
#ambnt.sujar(0, 1000)

#percebe-se que com o desempenho de 2 salas ele não é tão melhor do que o "agente não completamente observável"
#porem quando se adiciona mais salas o numero de probabilidade ter pelo menos uma sala suja aumenta muito
#assim melhorando demais o desempenho do "Agente Reativo Simples em Ambiente Completamente Observável"