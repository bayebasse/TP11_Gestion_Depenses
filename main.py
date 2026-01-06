
Les_depenses=[]
while True:
    print("MENU GESTION DES DEPENSES")

    
    print("1. Ajouter une dépense")
    print("2. Afficher toutes les dépenses")
    print("3. Afficher le total des dépenses")
    print("4. Afficher les dépenses par catégorie")
    print("5. Quitter")

    choix=int(input( "Choisissez une nombre 1 et 5 :"))

    if choix==1:
        montant=int(input("Entrez le montant : "))
        categorie=input("Entrez la catégorie : ")
        description=input("Entrez la description : ")

        depense={
            "montant":montant,
            "categorie":categorie,
            "description":description
        }

        Les_depenses.append(depense)
        print("Dépense ajoutée.")

    elif choix==2:
        if len(Les_depenses) == 0:
            print(" Aucune dépense encore prise.")
        else:
            print("Voici la liste des dépenses")
            for une_depense in Les_depenses:
                print("Montant :", une_depense["montant"])
                print("Catégorie :", une_depense["categorie"])
                print("Description :", une_depense["description"])

    elif choix==3:
        total=0
        for une_depense in Les_depenses:
            total = total + une_depense["montant"]
        print(" Total des dépenses :", total)


         #Affichage  les dépenses par catégorie

    elif choix==4:
        categorie_recherche = input("Entrez la catégorie : ")
        trouver=False

        for une_depense in Les_depenses:
            if une_depense["categorie"] == categorie_recherche:
                print("Montant :", une_depense["montant"])
                print("Description :", une_depense["description"])
                trouver=True

        if not trouver:
            print(" On a aucune dépense pour cette catégorie")

    elif choix==5:
        print("Fin du programme")
        break

    else:
        print(" Choix invalide")
