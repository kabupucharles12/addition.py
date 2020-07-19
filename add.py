

import sys
def add(f,g):
    return f+g
if __name__=="__main__":
    
     print(sys.argv)
if(len(sys.argv)==3):
    x = int( sys.argv[1] )
    y = int( sys.argv[2] )
    print (add(f,g))
elif(len(sys.argv)==2):
    x=int(sys.argv[1])
    y=int(input("entrer le troisieme chiffre svp?"))
    print(add(f,g))
elif (len(sys.argv)==1):
    x=int(input("entrer le deuxieme chiffre svp?"))
    y=int(input("entrer le troisieme chiffre svp?"))
    print(add(x,y))
else:
    print("C'est une erreur")
