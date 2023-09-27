def cripto(frase):
    tradutor = ""
    for letra in frase:
        if letra in "Aa": tradutor = tradutor + "0"
        elif letra in "Bb": tradutor = tradutor + "9"
        elif letra in "Cc": tradutor = tradutor + "8"
        elif letra in "Dd": tradutor = tradutor + "4"
        elif letra in "Ee": tradutor = tradutor + "6"
        elif letra in "Ff": tradutor = tradutor + "7"
        elif letra in "Gg": tradutor = tradutor + "1"
        elif letra in "Hh": tradutor = tradutor + "3"
        elif letra in "Ii": tradutor = tradutor + "2"
        elif letra in "Jj": tradutor = tradutor + "5"
        elif letra in "Kk": tradutor = tradutor + "!"
        elif letra in "Ll": tradutor = tradutor + "@"
        elif letra in "Mm": tradutor = tradutor + "#"
        elif letra in "Nn": tradutor = tradutor + "$"
        elif letra in "Oo": tradutor = tradutor + "%"
        elif letra in "Pp": tradutor = tradutor + "&"
        elif letra in "Qq": tradutor = tradutor + "*"
        elif letra in "Rr": tradutor = tradutor + ")"
        elif letra in "Ss": tradutor = tradutor + "("
        elif letra in "Tt": tradutor = tradutor + "_"
        elif letra in "Uu": tradutor = tradutor + "-"
        elif letra in "Vv": tradutor = tradutor + "="
        elif letra in "Ww": tradutor = tradutor + "+"
        elif letra in "Xx": tradutor = tradutor + "§"
        elif letra in "Yy": tradutor = tradutor + "?"
        elif letra in "Zz": tradutor = tradutor + "/"
        
        
        else:
            tradutor = tradutor + letra
    return tradutor        

frase = (cripto(input("Digite sua frase: ")))
frase_descript = frase
def
print(frase)

