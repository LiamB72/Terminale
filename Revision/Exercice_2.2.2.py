#Exercices 2.2

#2.2.2 :

operande=int(input("votre table de multiplication"))

for n in range(1,21):
    print(operande,"*",n,"= ",end='')
    if (operande*3 == n*operande):
       print(n*operande, "*")
    else:
        print(n*operande)
print()