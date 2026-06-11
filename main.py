#imports
from service import Service

#main
def main():
    fichier_config = "data/config.tsv"

    # Un flagger va lancer des requêtes, signaler des états de requêtes
    app = Service(fichier_config)
    #app.mainloop()
    app.stop()



#execution
main()