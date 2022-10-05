
import random
def experimento():
    pecas = ['D', 'N'] # Todos os possiveis estados das Peças (Defeituosa - D, Normal - N)
    tipo_pecas = random.randint(0,1) # randomicamente escolher
    if pecas[tipo_pecas] == 'N': #  Verificar
        return 1 # retorna 1 Peça Normal
    return 0 # senao Defeituosa

if __name__ == '__main__':
    producao = []
    for N_amostral in range(1000000):
        producao.append(experimento())
    amostragem = []
    for _ in range(10000):
        amostragem.append(random.choice(producao))

    #Pegar somente as peças defeituosas
    D = [d for d in amostragem if d == 0]
    A = len(D)
        # Printar os resultados como porcentagem do numero total de iterações
    print(f"A probabilidade é {round( (A / len(producao)) * 100)}% " f"em uma amostra de {len(producao)}")


