#!/usr/bin/python
# -*- coding: utf-8 -*-

# soui.py

"""
    Docs :
        https://netaddr.readthedocs.io/en/latest/tutorial_02.html
        https://www.redelijkheid.com/blog/2019/5/10/update-python-netaddr-oui-database

A qui appartient cette OUI? IEEE.

Mise à jour de la Base IEEE.
    cd /usr/lib/python3.7/site-packages/netaddr/eui
    curl http://standards-oui.ieee.org/oui.txt --output oui.txt
    python3 ieee.py
"""
"""Example Google style docstrings.

This module demonstrates documentation as specified by the `Google
Python Style Guide`_. Docstrings may extend over multiple lines.
Sections are created with a section header and a colon followed by a
block of indented text.

Example:
    Examples can be given using either the ``Example`` or ``Examples``
    sections. Sections support any reStructuredText formatting, including
    literal blocks::

        $ python example_google.py

Section breaks are created by resuming unindented text. Section breaks
are also implicitly created anytime a new section starts.

Attributes:
    module_level_variable1 (int): Module level variables may be documented in
        either the ``Attributes`` section of the module docstring, or in an
        inline docstring immediately following the variable.

        Either form is acceptable, but the two should not be mixed. Choose
        one convention to document module level variables and be consistent
        with it.

Todo:
    * For module TODOs
    * You have to also use ``sphinx.ext.todo`` extension

.. _Google Python Style Guide:
http://google.github.io/styleguide/pyguide.html

"""
__version__ = "1.0.0"

from netaddr import *
import regex
from termcolor import colored
from colorama import Back, Fore, Style, deinit, init

import sys

def test_mac(user_input):
    """
    Test @ Mac
    """
    try:
        # Bloc à essayer
        l_input = regex.sub("[^a-zA-Z,0-9]","", user_input)
        l_input = l_input.ljust(12, '0')
        #print(f"MAC : {l_input}")
        mac = EUI(l_input)
        oui = mac.oui
        return mac
    except (NotRegisteredError, AddrFormatError):
        # Erreur adresse Mac non enregistrée !
        # Bloc qui sera exécuté en cas d'erreur
        oui = ""
        return oui
    else:
        # Erreur adresse Mac incorrecte !
        # Bloc qui sera exécuté en cas d'erreur
        oui = ""
        return oui


def process_args(oui):
    """
    Print organisation et adresse
    """
    print()
    print(Fore.BLUE + "Cette @mac appartient à : " + Style.BRIGHT + Fore.GREEN + oui.registration().org + "\n" + Style.NORMAL)
    print(Fore.BLUE + "Son adresse postale est : " + Style.NORMAL)
    for add in oui.registration().address:
        print("\t" + add)

    print(Style.RESET_ALL)

def afficheFormat(format_mac, Mac):
    print("---" *15)
    tmp = f"{format_mac:15} : "
    print(Fore.BLUE + tmp + Style.BRIGHT + Fore.GREEN + Mac + Style.RESET_ALL)

def macFormat(macF):
    mac_options = {
        'CISCO': mac_cisco,
        'UNIXE': mac_unix_expanded,
        'BARE': mac_bare,
        'NORMAL': mac_eui48,
        'UNIX': mac_unix,
        'PGSQL': mac_pgsql
    }
    if macF.upper() in mac_options:
        return mac_options[macF.upper()]
    else:
        return mac_unix_expanded

def getFormatMac(mac, FormatMac='unix'):
    """Format la mac adresse avec le format passé en argument."""
    _mac = EUI(mac)
    _mac.dialect = macFormat(FormatMac)

    return _mac

class mac_custom(mac_unix): pass

"""
    mac_custom.word_fmt = '%.2X'
    mac = EUI('00-1B-77-49-54-FD', dialect=mac_custom)
"""

if __name__ == "__main__":
    import argparse

    init()

    # Set up command line arguments
    parser = argparse.ArgumentParser(
        description="Affichage des informations contructeur, en fonction de l'adresse mac."
    )
    parser.add_argument(
        "-v", "--version", action="version", version="\n%(prog)s version : " + __version__ + "\n"
    )
    parser.add_argument(
        "-u", "--unix", action='store_true', help="Affiche l'adresse mac au format Unix."
    )
    parser.add_argument(
        "-p", "--hp", action='store_true', help="Affiche l'adresse mac au format HP."
    )
    parser.add_argument(
        "-w", "--huawei", action='store_true', help="Affiche l'adresse mac au format Huawei."
    )
    parser.add_argument(
        "-c", "--cisco", action='store_true', help="Affiche l'adresse mac au format Cisco."
    )
    parser.add_argument(
        "-b", "--bare", action='store_true', help="Affiche l'adresse mac au format bare."
    )
    parser.add_argument(
        "-a", "--all", action='store_true', help="Affiche tous les formats d'adresse mac."
    )
    parser.add_argument(
        "-s", "--sobre", action='store_true', help="Affiche l'adresse mac seule."
    )
    parser.add_argument("mac", type=str, help="Spécifier l'adresse mac à rechercher.")

    args = parser.parse_args()

    # Test de la mac
    #print(args.mac)
    #print(test_mac(args.mac))
    oui = test_mac(args.mac)
    # Si n exite pas => Arret
    if oui == "":
        #print("Attention, @Mac incorrecte !")
        sys.exit()

    mac = oui
    # Formats Hp / Huawei
    f_bare = str(getFormatMac(mac, 'bare'))
    f_hp = f_bare[0:6] + "-" + f_bare[6:]
    f_huawei = f_bare[0:4] + "-" + f_bare[4:8] + "-" + f_bare[8:]

    if args.sobre:
        if args.unix:
            mac.dialect = mac_unix_expanded
            print("{}".format(mac))
        elif args.cisco:
            mac.dialect = mac_cisco
            print("{}".format(mac))
        elif args.bare:
            mac.dialect = mac_bare
            print("{}".format(mac))
        elif args.hp:
            print(f_hp)
        elif args.huawei:
            print(f_huawei)

    elif args.all:
        afficheFormat("Format Unix", str(getFormatMac(mac, "unixe")))
        afficheFormat("Format Cisco", str(getFormatMac(mac, "cisco")))
        afficheFormat("Format HP", f_hp)
        afficheFormat("Format Huawei", f_huawei)
        afficheFormat("Format Bare", str(getFormatMac(mac, "bare")))
        afficheFormat("Format Normal",  str(getFormatMac(mac, "normal")))
        print("---" *15)
    elif args.unix:
        afficheFormat("Format Cisco", str(getFormatMac(mac, "unixe")))
        process_args(mac.oui)
        print("---" *15)
    elif args.hp:
        afficheFormat("Format HP", f_hp)
        process_args(mac.oui)
        print("---" *15)
    elif args.huawei:
        afficheFormat("Format Huawei", f_huawei)
        process_args(mac.oui)
        print("---" *15)
    elif args.cisco:
        afficheFormat("Format Cisco", str(getFormatMac(mac, "cisco")))
        process_args(mac.oui)
        print("---" *15)
    elif args.bare:
        afficheFormat("Format Cisco", str(getFormatMac(mac, "bare")))
        process_args(oui)
        print("---" *15)
    else:
        afficheFormat("Format Normal",  str(getFormatMac(mac, "normal")))
        process_args(mac.oui)
        print("---" *15)
