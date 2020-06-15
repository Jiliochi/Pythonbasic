def decodeMorse(morse_code):
    q = morse_code.strip().replace('  ', " albert "); t = q.split(); decode = []
    for i in t:
        if i == 'albert':
            decode += ' '
        else:
            decode += MORSE_CODE[i]

    return ''.join(decode)





