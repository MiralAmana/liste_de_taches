class Todolist:
    def __init__(self):
        self.taches=[]
    def ajoutertache(self,tache):
        self.taches.append(tache)
        print("Vous avez ajoutée une tache")
    def supprimertache(self,index):
        if index < len(self.taches):
            del self.taches[index]
            print("Vous avez supprimé une tache")
        else:
            print("Cette taches n'existe pas")
    def tacheterminer(self,index):
        if index < len(self.taches):
            self.taches[index]+= " terminée"
            print("Vous avez terminez votre taches!")

    def affichertache(self):
        if self.taches:
            print("Liste des taches")
            for i, tache in enumerate(self.taches):
                print(f"{i + 1}. {tache}")
        else:
            print("Aucune tache en cours")
def main():
    todolist=Todolist()
    while True:
        print("\n Voici le menu")
        print("1.ajouter une tache")
        print("2.Supprimer une tache")
        print("3.Marquer la fin d'une tache")
        print("4.Afficher votre todolist")
        print("5.Quitter")

        choix = input("Entrez votre choix (1/2/3/4/5): ")

        if choix == '1':
            tache = input("Entrez la nouvelle tâche : ")
            todolist.ajoutertache(tache)
        elif choix == '2':
            index = int(input("Entrez l'indice de la tâche à supprimer : ")) - 1
            todolist.supprimertache(index)
        elif choix == '3':
            index = int(input("Entrez l'indice de la tâche terminée : ")) - 1
            todolist.tacheterminer(index)
        elif choix == '4':
            todolist.affichertache()
        elif choix == '5':
            print("Au revoir !")
            break
        else:
            print("Choix invalide. Veuillez choisir parmi les options disponibles.")


if __name__ == "__main__":
    main()







