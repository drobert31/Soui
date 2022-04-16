
Soui
=======
- Utilitaire pour visualiser les mac adresses sous différent format et obtenir des informations du constructeur.

Current methods supported
=======
usage: soui.py [-h] [-v] [-u] [-p] [-w] [-c] [-b] [-a] [-s] mac

Affichage des informations contructeur, en fonction de l'adresse mac.

positional arguments:
  mac            Spécifier l'adresse mac à rechercher.

options:
  -h, --help     show this help message and exit
  -v, --version  show program's version number and exit
  -u, --unix     Affiche l'adresse mac au format Unix.
  -p, --hp       Affiche l'adresse mac au format HP.
  -w, --huawei   Affiche l'adresse mac au format Huawei.
  -c, --cisco    Affiche l'adresse mac au format Cisco.
  -b, --bare     Affiche l'adresse mac au format bare.
  -a, --all      Affiche tous les formats d'adresse mac.
  -s, --sobre    Affiche l'adresse mac seule.

Currently Testing [not publicly available]
=======
- soui -h

Roapmapped
=======
- Ajout de nouveau format

Requirements
=======
netaddr

Authors
=======
 * Dominique Robert ([drobert@free.fr](mailto:drobert@free.fr))
