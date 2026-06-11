#tout le "backend" de ce projet
#tourne en continu et gère la communication des différents objets du projet

class Service:
    def __init__(self, config_path:str):
        self.config_path = config_path;
        self.params = self.__load_data()

    def stop(self):
        self.__export_data()

    def __export_data(self):
        try :
            f = open(self.config_path, mode="w+")
            for cle,valeur in self.params.items():
                f.write( f"{cle}\t{valeur}\n" )
                
        except Exception as e:
            # devrait ne jamais arriver
            print(e)
    
    def __load_data(self)->dict:
        try :
            f = open(self.config_path, mode="r")
            assert len(f.read().split("\n"))>0
            d = {}
            for line in f.read().split("\n"):
                cells = f.read().split("\t")
                assert len(f.read().split("\n")) == 2
                d[cells[0]] = cells[1]
            return d
        except Exception as e:
            #si erreur de lecture, données par défaut
            return self.__load_default_data()

    def __load_default_data(self)->dict:
        return {
            "seconds_before_check":"3000"
        }