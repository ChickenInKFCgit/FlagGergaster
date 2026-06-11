# FlagGergaster

Ce projet met en place un bot discord, qui affiche un dashboard du résultat de son scrapping.
Le scrapping en question permet de récupérer des annonces postées sur des sites tels que leboncoin, vinted etc.

- Le résultat d'un scrapping est découpé et envoyé dans une base de données "maison" (en tsv)
- L'utilisateur choisit des filtres qu'il applique via le chatbot sur discord
- Le résultat du scrapping est actualisé ponctuellement, ex 24h
- Le résultat du scrapping est affiché via un dashboard, qui montre les candidats potentiels. L'utilisateur peut choisir de les refuser ce qui va les "shadow-ban".

# Note Personelle
https://scrape.do/blog/how-to-scrape-javascript-rendered-web-pages-with-python/