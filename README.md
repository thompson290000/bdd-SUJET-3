# bdd-fulldatageneration

Ce dépôt est largement inspiré du dépôt ci-dessous :
https://github.com/jduran9987/generate-fake-dbdata

En fait, les modifications effectuées concernent quelques adaptations pour faire en sorte que l'on puisse peupler plusieurs tables en une commande et surtout pour se connecter à une base MariaDB au lieu de postgres.

## Prerequis

Une seule commande pour initialiser l'environnement :

```
sudo ./init.sh
```
S'il vous propose de redémarrer des services, faites comme il le souhaite (laissez les options par défaut). Si cela fait planter votre initialisation, pas de souci relancez-là, elle fonctionnera (mon record est de 3 relances).

Attention, si cela plante sans vous demander de redémarrer un service alors il vaut mieux que l'on voit ensemble. Vous pouvez m'envoyer un mail pour ça avec un screenshot indiquant l'erreur et la commande utilisée.

## Getting started

### Démarrage rapide

Modifier le fichier de configuration de connexion en suivant le schéma ci-dessous :
```
[SETTINGS]
User = root
Password = ensibs
Database = myDataBase
Port = 3306
```

Configurez le fichier populate_tables pour qu'il cible votre structure puis lancez ce script avec la commande ci-dessous :

```
python3 populate_tables.py
```

### Tester l'exemple

Si vous souhaitez tester la version d'exemple, il vous suffit de lancer la création des tables via la commande :
```
python3 create_tables_example.py
```
Puis :
```
python3 populate_tables.py
```

### Réinitialiser

Vous disposez de deux scripts pour la réinitialisation, un premier pour ne supprimer que les données sans toucher à vos tables :
```
python3 delete_all_data.py
```
et un autre qui supprime directement les tables :
```
python3 drop_all_tables_database.py
```
Les blocages liés à des dépendances n'ont pas été testés donc en cas de problème n'hésitez pas à me le signaler via l'adresse mail indiquée en contact.

### Contact

En cas de souci, n'hésitez pas à contacter :
- M. Philippe Charton : philippe.charton@univ-ubs.fr
