#Créartion de la fonction de controle de saisie

#Pour les chaines de caractères

def controle_caractere(valeur_entree,valeur_a_comparer):
      """ 
            Permet de verifier si la chaine de caractère saisie correspond à une autre
            Paramètre : la valeur entrée et la valeur à comparer
            retour : le resultat de la compraraison vrai ou faux
      """
      while valeur_entree != valeur_a_comparer :
                  
            print(valeur_entree,valeur_a_comparer)
            print("Vous avez entrée : " , valeur_entree ,"Ceci n'est pas la bonne valeur")
            valeur_entree = input("Entrée incorrecte ! Veiller recommencer :  ")

      return True

#Pour les entiers
def controle_entier(valeur_entree,valeur_a_comparer):
      """ 
            Permet de verifier si le nombre saisie correspond à un autre
            Paramètre : la valeur entrée et la valeur à comparer
            retour : le resultat de la compraraison vrai ou faux
      """

      while valeur_entree != valeur_a_comparer :
                  
            print(valeur_entree,valeur_a_comparer)
            print("Vous avez entrée : " , valeur_entree ,"Ceci n'est pas la bonne valeur")
            valeur_entree = int(input("Entrée incorrecte ! Veiller recommencer :  "))
      return True