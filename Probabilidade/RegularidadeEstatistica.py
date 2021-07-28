
import random
def experimento():
    faces = ['C', 'K'] # Todas as possivei Faces (Cara - C, Coroa-K
    top_face = random.randint(0,1) # randomicamente escolher
    if faces[top_face] == 'C': # Verificar
        return 1 # retorna 1 se Cara
    return 0 # senao Coroa

if __name__ == '__main__':
    cara_counter = 0  # variavel contabiliza numero de vezes para face CARA
    # Conduzir o experimento 1 milhão de vezes e contabilizar cara
    for N_amostral in [10,100,1000,10000,100000,1000000]:
        for _ in range(N_amostral):
            cara_counter += experimento()
        # Printar os resultados como porcentafem do numero total de iterações
        print(f"A probabilidade de Obter CARA é {round(cara_counter / N_amostral * 100)}% "
              f"em uma amostra de {N_amostral} lançamentos")


