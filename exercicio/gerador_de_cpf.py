
import random
import sys



nove_digitos=''
for i in range(9):
    nove_digitos+=str(random.randint(0,9))

#aqui eu separo de acordo com o  padrao do cpf(xxx.xxx.xxx-xx)
    tres_digitos=nove_digitos[:3]
    seis_digitos=nove_digitos[3:6]
    noves_digitos=nove_digitos[6:9]
# primeiro numero apos o traço(-)


contador_1=10
total_1=0
for digito_1 in nove_digitos:
    total_1+=int(digito_1) * contador_1
    contador_1-=1
    digito_1=((total_1 * 10) % 11)
    validar= digito_1 if digito_1<=9 else 0

#segundo numero apos o traço(-)
   
dez_digitos=nove_digitos+str(validar)
contador_2=11
total_2=0
for digito_2 in dez_digitos:
    total_2+=int(digito_2) * contador_2
    contador_2-=1
    digito_2=(total_2 * 10) % 11
    validar_2= digito_2 if digito_2<=9 else 0

    
print ( f'{tres_digitos}.{seis_digitos}.{noves_digitos}-{validar}{validar_2}' ) 