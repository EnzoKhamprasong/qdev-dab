# DAB

Distributeur automatique de billets.

## Acquisition

Vous pouvez obtenir une copie de ce programme en clonant ce dépôt.

## Utilisation

L'objectif de ce programme est de simuler le comportement d'un distributeur automatique de billets. C'est un programme interactif. Pour l'utiliser, placez-vous à l'intérieur de votre clone local de ce dépôt et lancez :

- dans Invite de commandes / PowerShell sur Windows,
```bash
python.exe -m dab
```
- dans Terminal sur Linux / macOS.
```bash
python3 -m dab
```

Le programme repose sur le module `dab`. Son script principal dans `dab/__main__.py` initialise une base de données de comptes bancaires (identifiés par des numéros de compte) qu'il est ensuite possible de manipuler (déposer de l'argent ou retirer de l'argent). Les comptes bancaires sont modélisés par la classe `Account` définie dans le fichier `dab/account.py`. 

## Tests

Le script `tests/unit_tests.py` implémente une suite de tests unitaires (grâce au module `unittest` de Python) du programme DAB. Vous pouvez lancer ces tests en exécutant :

- dans Invite de commandes / PowerShell sur Windows,
```bash
python.exe -m unittest tests/unit_tests.py
```
- dans Terminal sur Linux / macOS.
```bash
python3 -m unittest tests/unit_tests.py
```
