def rot13(message):

    trocado = []

    alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    alfabeto_maior = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

    for i in message:                               
        if i in alfabeto:
            trocado.append(alfabeto[(alfabeto.index(i)+13)%26])
        elif i in alfabeto_maior:
            trocado.append(alfabeto_maior[(alfabeto_maior. index(i)+13)%26])
        else: 
            trocado.append(i)

    return ''.join(trocado)