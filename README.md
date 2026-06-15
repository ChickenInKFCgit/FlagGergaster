# FlagGergaster

Ce projet permet de se relier au bot discord, et d'y afficher un dashboard, depuis lequel on peut accéder aux fonctionnalités suivantes :

* Demander le scrapping d'une page selon des filtres très précis
* Observer le résultat du scrapping, parmis les résultats qui n'étaient pas dans la base de données maison
* Paramétrer le scrapping selon : la durée avant rafraîchissement, les filtres appliqués, le délai minimal et maximal, etc.
* Supprimer, Modifier ou Accéder aux résultats stockés
* Actualiser les annonces, afin de vérifier qu'elles sont toujours disponibles

Le scrapping en question permet de récupérer des annonces postées sur des sites tels que leboncoin, vinted etc.

- Le résultat d'un scrapping est découpé et envoyé dans une base de données "maison" (en tsv)
- L'utilisateur choisit des filtres qu'il applique via le chatbot sur discord
- Le résultat du scrapping est actualisé ponctuellement, ex 24h
- Le résultat du scrapping est affiché via un dashboard, qui montre les candidats potentiels. L'utilisateur peut choisir de les refuser ce qui va les "shadow-ban".

# Documentations utilisées lors du projet

* https://scrape.do/blog/how-to-scrape-javascript-rendered-web-pages-with-python/
* https://scrapfly.io/blog/posts/web-scraping-with-playwright-and-python