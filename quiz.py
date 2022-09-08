#Quiz leer un numero entero de 5 digitos y determinar si es un numro capicua
print("--------------------------")
print("--------Bienvenido--------")
print("--------------------------")
# input
n=int(input( "Ingrese el valor de n: "))

#processing

if n>9999:
    if n<= 99999:
        a1 = n % 10
        a2= (n%100)//10
        a3=(n%1000)//100
        a4=(n%10000)//1000
        a5=(n - (n%10000)) //10000
        n2 =str(a1)+str(a2)+str(a3)+str(a4)+str(a5)
        if n==n2:
         R=" no es un numero capicua"
        else:
         R="n es un numero capicua"
    else:   
     R="n es un numero mayor de 4 digitos"  
else:
    R="n no cumple con las condiciones" 

#output
print("-------------------")
print("-----Relsultado----")
print(str(R))
     
