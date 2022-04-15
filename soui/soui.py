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
from termcolor import colored
from colorama import Back, Fore, Style, deinit, init

import sys

def test_mac(user_input):
    """
    Test @ Mac
    """
    try:
        # Bloc à essayer
        mac = EUI(user_input)
        oui = mac.oui
        return oui
    except (NotRegisteredError, AddrFormatError):
        print(Style.BRIGHT + Fore.RED + 'Erreur adresse Mac non enregistrée !')
        # Bloc qui sera exécuté en cas d'erreur
        oui = ""
        return oui
    else:
        print(Style.BRIGHT + Fore.RED + 'Erreur adresse Mac incorrecte !')
        # Bloc qui sera exécuté en cas d'erreur
        oui = ""
        return oui

def process_args(oui):
    """
    Print organisation et adresse
    """
    print(Fore.BLUE + "Cette @mac appartient à : " + Style.BRIGHT + Fore.GREEN + oui.registration().org + "\n" + Style.NORMAL)
    print(Fore.BLUE + "Son adresse postale est : " + Style.NORMAL)
    for add in oui.registration().address:
        print("\t" + add)

def afficheFormat(format_mac):
    print("---" *15)
    tmp = f"{format_mac:15} : "
    print(Fore.BLUE + tmp + Style.BRIGHT + Fore.GREEN + str(mac) + Style.NORMAL)
    print("---" *15)

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
        "-u", "--unix", action='store_true', help="Affiche l'adresse mac au format unix."
    )
    parser.add_argument(
        "-c", "--cisco", action='store_true', help="Affiche l'adresse mac au format cisco."
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

    mac = EUI(args.mac)

    if args.sobre:
        if args.unix:
            mac.dialect = mac_unix_expanded
        elif args.cisco:
            mac.dialect = mac_cisco
        elif args.bare:
            mac.dialect = mac_bare

        print("{}".format(mac))
    elif args.all:
        mac.dialect = mac_unix_expanded
        afficheFormat("Format Unix")
        mac.dialect = mac_cisco
        afficheFormat("Format Cisco")
        mac.dialect = mac_bare
        afficheFormat("Format Bare")
        mac = EUI(args.mac)
        afficheFormat("Format Normal")
    elif args.unix:
        mac.dialect = mac_unix_expanded
        _form = "Format Unix"
        afficheFormat(_form)
        process_args(oui)
        print("---" *15)
    elif args.cisco:
        mac.dialect = mac_cisco
        _form = "Format Cisco"
        afficheFormat(_form)
        process_args(oui)
        print("---" *15)
    elif args.bare:
        mac.dialect = mac_bare
        _form = "Format Bare"
        afficheFormat(_form)
        process_args(oui)
        print("---" *15)
    else:
        mac = EUI(args.mac)
        _form = "Format Normal"
        afficheFormat(_form)
        process_args(oui)
        print("---" *15)
