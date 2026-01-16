def solution(text, ending):
    texto = []
    texto2 = ''
    for i in range(-1, -len(text)-1, -1):
        
        if i == -1:
            texto.append(text[i])
        else:
            texto.insert(0, text[i])
            
        texto2 = ''.join(texto)
        
        if ending == texto2:
            return True
    
    return False
