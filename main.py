
from addTwoInt import add
import sys

if __name__ == "__main__":
	reponse= input("Tapez oui pour multiplier non pour bye bye ")
	print(reponse)
	if(reponse == "oui"):
		if(len(sys.argv)==3):
			print(sys.argv)
			x = int(sys.argv[1])
			y = int(sys.argv[2])
			print(mul(x,y))
		elif(len(sys.argv)==2):
			x = int(sys.argv[1])
			y = int(input("Tapez la troisieme valeur ? "))
			print(mul(x,y))
		elif(len(sys.argv)==1):
			x = int(input("Tapez la deuxieme valeur ? "))
			y = int(input("Tapez la troisieme valeur ? "))
			print(mul(x,y))
		else:
			print("Erreur")
 if(reponse == "non"):
                        print("Bye Bye")
