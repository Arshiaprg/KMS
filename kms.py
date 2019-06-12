import os
import builtwith
import requests
from ig import *
from hash import *
from list import *
from colorama import Fore
from page_inspect import *

def find_admin_php(address):
    a = []
    for i in list_admin_finder_php:
        b = requests.get(address + "/" + i)
        if b.status_code == 200:
            a.append(address + "/" + i)
    return a

def find_admin_asp(address):
    a = []
    for i in list_admin_finder_asp:
        b = requests.get(address + "/" + i)
        if b.status_code == 200:
            a.append(address + "/" + i)
    return a

def find_cms(address):
    return builtwith.builtwith(address)