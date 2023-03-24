N1=int(input("Digite um número:"))
tot=0
for c in range(1, N1+1):

    if N1 % c == 0:
        tot=tot+1

if tot<=2:
    print(f"O número {N1} é primo")

else:
    print(f"O número {N1} não é primo, pois é divisível por {tot} números")     
        

 
 


