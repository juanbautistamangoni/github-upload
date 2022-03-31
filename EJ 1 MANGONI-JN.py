#Funciones.
def aplicamin_sacatilde(aux_a,aux_b):   
    """Aplica minúsculas a todos los caracteres y reemplaza vocales con tilde"""
    contilde=["á","é","í","ó","ú"]
    sintilde=["a","e","i","o","u"]
    aux_1=aux_a.lower()
    aux_2=aux_b.lower()
    frase1=""
    frase2=""
    for caracter in aux_1:
        if caracter in contilde:
            posi=contilde.index(caracter)
            frase1+=sintilde[posi]
        else:
            frase1+=caracter
    for caracter in aux_2:
        if caracter in contilde:
            posi=contilde.index(caracter)
            frase2+=sintilde[posi]
        else:
            frase2+=caracter
    return frase1, frase2

def busca_coincidencias(frase,frase_bis):    
    """Busca y registra los caracteres que aparecen en ambas frases"""
    contador=0
    contador_bis=0
    flag=0
    for character in frase:
        if character.isalpha():
            if character in frase_bis:
                contador+=1
            else:
                flag=1
                break
    if flag!=1:
        for characterbis in frase_bis:
            if characterbis.isalpha():
                if characterbis in frase:
                    contador_bis+=1
                else:
                    break
    if contador==contador_bis:
        return True
    else:
        return False
#Programa principal.
print("Tipee una primera frase/oración:")
oracion1=input()
print("Tipee una segunda frase/oración:")
oracion2=input()
print()
#Invocación de funciones creadas.
oracion_a,oracion_b=aplicamin_sacatilde(oracion1,oracion2)
valor_verdad=busca_coincidencias(oracion_a,oracion_b)
if valor_verdad:
    print("Las frases son anagramas")
else:
    print("Las frases NO son anagramas")
        
        
        
        