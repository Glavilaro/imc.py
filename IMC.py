personas=int(input("personas : "))
while personas > 0:

 nombre= input("ingrese su nombre : ")

 edad= int(input("ingrese su edad por favor : "))

 altura= float(input("ingrese su altura en metros : "))

 peso=float(input("ingrese su peso:  "))

 IMC=peso /(altura * altura)

 if (edad < 18):
     print("usted es menor de edad")
 else:
     print("usted es mayor de edad")
     print("IMC: " + str(IMC))

 if IMC >=0 and IMC<=15.99:
     print("delgadez severa")
 elif IMC >=16.00 and IMC<= 16.99:
     print("delgadez moderada")
 elif IMC >= 17.00 and IMC <= 18.49:
     print("delgadez leve")
 elif IMC >= 18.50 and IMC <=24.99:
     print("normal")
 elif IMC >= 25.00 and IMC <= 29.99:
     print("sobrepeso")
 elif IMC >= 30.00 and IMC <= 34.99:
     print("obesidad leve")
 elif IMC >= 35.00 and IMC <= 39.00:
     print("obesidad media")
 elif IMC >= 40.00:
     print("obesidad morvida")

     personas = personas -1




