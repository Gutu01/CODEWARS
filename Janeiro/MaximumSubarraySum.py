def max_sequence(arr):
    
    maior = soma = 0

    for i in arr:
        if soma + i >= 0:
            soma += i
            if soma > maior:
                maior = soma
        else:
            soma = 0

    return maior