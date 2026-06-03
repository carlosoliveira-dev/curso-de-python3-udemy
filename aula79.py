# Exemplo de uso dos sets
letras = set()
while True:
    letra = input('Digite: ')
    is_letter = not letra.isdigit()
    have_one_letter = len(letra) == 1

    if is_letter and have_one_letter:
        letras.add(letra.lower())
        if 'l' in letras:
            print('PARABÉNS')
            break
    print(letras)