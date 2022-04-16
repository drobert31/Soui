
# Soui
- Utilitaire pour visualiser les mac adresses sous différent format et obtenir des informations du constructeur.

## Les différentes options :
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

<details>
    <summary>
        <strong> Utilisation : </strong>
    </summary>

## Utilisation :
- Liste les différents formats
<code>
soui.py -a 0012ff</br>
---------------------------------------------</br>
Format Unix     : 00:12:ff:00:00:00</br>
---------------------------------------------</br>
Format Cisco    : 0012.ff00.0000</br>
---------------------------------------------</br>
Format HP       : 0012FF-000000</br>
---------------------------------------------</br>
Format Huawei   : 0012-FF00-0000</br>
---------------------------------------------</br>
Format Bare     : 0012FF000000</br>
---------------------------------------------</br>
Format Normal   : 00-12-FF-00-00-00</br>
---------------------------------------------</br>
</code>

- Affiche un format et les informations du constructeur.

<code>
soui.py -c 0012ff</br>
---------------------------------------------
Format Cisco    : 0012.ff00.0000
Cette @mac appartient à : Lely Industries N.V.

Son adresse postale est :
	Weverskade 110
	Maassluis  Zuid-Holland  3147PA
	NL

---------------------------------------------
</code>
</details>

## Roapmapped
- Ajout de nouveau format

## Requirements
netaddr

## Authors
 * Dominique Robert ([drobert@free.fr](mailto:drobert@free.fr))
