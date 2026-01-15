def to_camel_case(text):
    text = text.replace('_','-')
    text = text.split('-')

    for i in range(len(text)):
        if i > 0:
            text[i] = text[i].capitalize()

    text = ''.join(text)
    return text