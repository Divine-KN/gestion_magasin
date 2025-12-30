from magazin_fonction.fonction_de_control import*


#Ce fichiers contients l'ensemble des fonctions principal utilisé dans dans l' application "Magazin"

def creation_compte():

      """Permet de créer un compte

         paramêtre : aucun

         retour : il retourne un dictionnaire de chaînes de caractère ayant les clés "nom","nom du propriétaire" et "numéro impôt"
      """

      identifiant = dict
      try :
            identifiant = {"nom du magazin":input("Entrez le nom du magazin : "),"propriétaire": input("Entrez votre nom : "),"numéro impôt" : input(f'Entrez le numéro impôt : ')}
      except ValueError :
            identifiant = {"nom du magazin":input("Entrez le nom du magazin : "),"propriétaire": input("Entrez votre nom : "),"numéro impôt" : input(f'Entrez le numéro impôt : ')}
      return identifiant
     
def modifier_profile(profile,nombre_d_information):

      """Permet à un utilisateur de modifier les informations cointenues dans son profile

         paramêtre : Dictionnaire d'identifiants et le nombre de donnée à modifier

         retour : il retourne un dictionnaire contenant les identifiants mis à jour
      
      """
      i4 = 1
      while i4 <= nombre_d_information:

            info_a_modifier = input("Entrez l'information à modifier : ")
            info_a_modifier = input("Entrez l'information à modifier : ")
            profile[info_a_modifier] = input(f'''Entrez le nouveau {info_a_modifier} : ''')
            i4 = i4 + 1
      return profile

def enregistrez_article (nombre_de_marchandise_a_enregistrer, marchandises):

      """   Permet d'ajouter des marchandises

            paramêtre : marchandises = listes de marchandises

            nombre_de_marchandise_a_enregistrer = un entier

            retour :il retourne une liste marchandise contenant toutes celles qui ont été enregistrer
      """
      i1 = 1
      while (nombre_de_marchandise_a_enregistrer >= i1):
            try:
                  marchandises.append({"nom":input(f"Entrez le nom de l'article {i1} : ") ,"quantité": int(input(f'Entrez la quantité de  : '))})
                  print(i1)
            except ValueError:
                        print("Erreur de saisie ! Veilliez recommancer s'il vous plait.")
                        marchandises.append({"nom":input(f"Entrez le nom de l'article {i1} : ") ,"quantité": int(input(f'Entrez la quantité de  : '))})
                        print(marchandises) 
            i1 = i1 + 1
      return marchandises

def vente_article (nombre_vendu , marchandises):

      """
            Permet de modifier le contenue des stocks en fonctions d'un vente

            paramêtre : nombre_vendu et marchandises

            retour : Il retourne une liste contenant les marchandises restants
      """
      i2 = 0
      for i2 in range(nombre_vendu) :
            article_vendu = input("Entrez le nom de l'article vendu : ")
            if article_vendu == marchandises[i2]["nom"]:
                  print(marchandises[i2]["nom"])
                  quantite_de_l_article = int(input("Entrez la quantité vendue : "))
                  marchandises[i2]["quantité"] = marchandises[i2]["quantité"] - quantite_de_l_article
      return marchandises
          
def supprimmer_article (nombre_d_article_a_supprimer, marchandises):

      """
            permet de supprimer des marchandises :
            paramêtre :

            nombre_d_article_a_supprimer = un entier
            marchandises = un dictionnaire

            retour:

            La liste marchandise avec les valeurs modifier. Il diminue la quantité de la marchandise voulue.
      """
      #La première boucle permet de parcourir la liste selon nombre d'article à supprimer
      i3 = 0
      for i3 in range(nombre_d_article_a_supprimer):
            article_a_supprimer = input("Entrez le nom de l'article à supprimer : ")
            i4 = 0
            #La deuxième boucle permet de parcourir les marchandise afin de trouver celle que l'on veut supprimer
            while (i4 in range(len(marchandises))):
                  if (article_a_supprimer == marchandises[i4]["nom"]):
                        marchandises[i4] = marchandises.pop(marchandises[i4])
                  i4 = i4 + 1
            print(i3)
      return marchandises

def quitter_application():
      
      """Permet de fermer l'application selon le choix de l'utilisateur

         Paramêtre : aucun

         retour : aucun , il affiche un message puis referme l'application au cas contraire il la relance
      """ 
      #Pour contrôler si le choix entré est  valide
      choix = (input("OUI OU NON ? "))
      while choix != "OUI" and choix != "NON" :
            print(choix)
            choix = input("Erreur ! Veillez entrez 'OUI'ou 'NON' :")
            print (choix)
      #Vérifie si OUI ou NON , il veut quitter l'application 
      if choix == "OUI":
            print("Fermeture de l'application  !")
            raise SystemExit
      elif choix == "NON":
            print("Mécanisme qui permettra de recommencez l'application")