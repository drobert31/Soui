
# Soui
- Utilitaire pour vérifier le format d'une adresse mac,
- Visualiser les mac adresses sous différent format,
- Obtenir des informations du constructeur.

## Les différentes options :
<strong> usage : </strong> soui.py [-h] [-v] [-u] [-p] [-w] [-c] [-b] [-a] [-s] mac

Affichage des informations contructeur, en fonction de l'adresse mac.

positional arguments:

  mac            Spécifier l'adresse mac à rechercher.

options:
+  -h, --help     show this help message and exit
+  -v, --version  show program's version number and exit
+  -u, --unix     Affiche l'adresse mac au format Unix.
+  -p, --hp       Affiche l'adresse mac au format HP.
+  -w, --huawei   Affiche l'adresse mac au format Huawei.
+  -c, --cisco    Affiche l'adresse mac au format Cisco.
+  -b, --bare     Affiche l'adresse mac au format bare.
+  -a, --all      Affiche tous les formats d'adresse mac.
+  -s, --sobre    Affiche l'adresse mac seule.

<details>
    <summary>
        <strong> Utilisation : </strong>
    </summary>

## Utilisation :
- Liste les différents formats

<strong>soui.py -a 0012ff</strong>

| Format | Mac |
| :------------ |   :---:       |
| Format Unix     : | 00:12:ff:00:00:00 |
| Format Cisco    : | 0012.ff00.0000 |
| Format HP       : | 0012FF-000000 |
| Format Huawei   : | 0012-FF00-0000 |
| Format Bare     : | 0012FF000000 |
| Format Normal   : | 00-12-FF-00-00-00 |

- Affiche un format et les informations du constructeur.

<strong>soui.py -c 0012ff</strong>
```
Format Cisco    : 0012.ff00.0000

Cette @mac appartient à : Lely Industries N.V.

Son adresse postale est :
  Weverskade 110
  Maassluis  Zuid-Holland  3147PA
  NL
```
</details>

## Roapmapped
- Ajout de nouveau format,
- Sauver dans un fichier csv.

## Requirements
[netaddr](https://pypi.org/project/netaddr/)

## Installation
***
Un petit tuto pour l'installation.
```
$ git clone https://github.com/drobert31/Soui.git
$ cd Soui
$ python setup.py install
$ sudo cp soui/soui.py /usr/sbin/soui
$ sudo chmod +x /usr/sbin/soui
```
L'utilisation de sudo est nécessaire si l'utilisateur n'a pas les droits adéquats.

## Authors
 * Dominique Robert ([drobert@free.fr](mailto:drobert@free.fr))
