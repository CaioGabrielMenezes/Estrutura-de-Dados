def pesquisaBinaria(lista, alvo):
    #Definindo os limites da lista
    baixo = 0
    alto = len(lista) - 1

    #Enquanto não percorrer toda a lista....
    while baixo <= alto:

        #pega o índice do meio da lista e o seu elemento
        meio = (baixo + alto) // 2
        chute = lista[meio]
        #Compara o elemento da lista com seu alvo 
        if chute == alvo:
            return meio
        
        #se o chute for maior que o alvo significa que deve ajustar o parâmetro da lista para menos
        if chute > alvo:
            alto = meio - 1
        else:
            baixo = meio + 1

    return None


minha_lista = [1,3,5,7,9]
print(pesquisaBinaria(minha_lista, -1))