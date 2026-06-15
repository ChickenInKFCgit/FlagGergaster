""" va scrapper des sites dynamiques qui utilisent javascript. c'est du costaud.
"""
import time as t
from random import randint

import nest_asyncio; nest_asyncio.apply()  # This is needed to use sync API in repl
from playwright.sync_api import sync_playwright


import nest_asyncio; nest_asyncio.apply()  # This is needed to use sync API in repl
from playwright.sync_api import sync_playwright

# Fonctions utilitaires
def wait(pfDureeMin:int, pfDureeMax:int):
    duree = randint(pfDureeMin, pfDureeMax) * 0.001
    t.sleep(duree)

#Scrapper
class Scrapper:
    def __init__(self, pfuserdatadir:str= "data/real_real_real_user_data_trust/", pfnavigateur:str="chrome",
                 pfdelaimin:int=100, pfdelaimax:int=3000 ):
        """
        Prends en paramètre:
        - le chemin du dossier contenant l'historique de recherche, afin de crédibiliser le scrapper
        - le navigateur à utiliser (par défaut, chrome)
        - le délai min avant de se déplacer dans le site (en ms)
        - le délai max avant de se déplacer dans le site (en ms)

        Le délai sera randomisé, mais permet de moins se faire détecter.
        """
        self.pw = sync_playwright().start()
        self.dossier_historique = pfuserdatadir
        self.navigateur = pfnavigateur
        self.delaimin = pfdelaimin
        self.delaimax = pfdelaimax

    
    def scrap(self, siteURL:str):
        self.fausser_credibilite_navigateur()

        self.contexte = self.__launch()

        self.simuler_navigation(siteURL)
        

    def simuler_navigation(self, siteURL:str):
        page = self.contexte.new_page()

        page.goto(siteURL)
        print(siteURL.split("/"))
        t.sleep(10)
    
    def fausser_credibilite_navigateur(self):
        self.fill_user_data_dir()
         

        

    def fill_user_data_dir(self):
        pass

    def __launch(self):
        return self.pw.chromium.launch_persistent_context(
            user_data_dir=self.dossier_historique,
            channel="chrome",
            headless=False
        )

s = Scrapper()
s.scrap("https://www.leboncoin.fr/")
