"""
In una grande raccolta di file possono esserci più copie dello stesso file,
messi in cartelle diverse o con nomi differenti. 
Lo scopo di questo esercizio è di cercare i duplicati.

1. Scrivete un programma che cerchi in una cartella e, ricorsivamente, nelle sue sottocartelle,
e restituisca un elenco dei percorsi completi di tutti i file con una stessa estensione (come .txt).

2. Per riconoscere i duplicati, potete usare md5sum per calcolare la "checksum" di ogni file.
Se due file hanno la stessa checksum, significa che con ogni probabilità hanno lo stesso contenuto.

3.Per effettuare un doppio controllo, usate il comando Uix diff.
"""  

import os
import hashlib

def find_duplicates(folder, extension):
    # Cerca i duplicati nella cartella e sottocartelle, con estensione specificata.
    # Restituisce due liste: una con i percorsi completi dei file con la stessa estensione e una con quelli con la stessa checksum.
    extensions = {}
    checksums = {}
    for dirpath, dirnames, filenames in os.walk(folder):
        for filename in filenames:
            if filename.endswith(extension):
                filepath = os.path.join(dirpath, filename)
                with open(filepath, 'rb') as f:
                    checksum = hashlib.md5(f.read()).hexdigest()
                if checksum in checksums:
                    checksums[checksum].append(filepath)
                else:
                    checksums[checksum] = [filepath]
                if extension in extensions:
                    extensions[extension].append(filepath)
                else:
                    extensions[extension] = [filepath]
    duplicates = [filepath for extension, paths in extensions.items() for filepath in paths if len(paths) > 1]
    return duplicates, checksums

folder = 'Files'
extension = '.txt'
duplicates, checksums = find_duplicates(folder, extension)

print(f'File con la stessa estensione ({extension}):')
for filepath in duplicates:
    print(f'  {filepath}')

print(f'File duplicati:')
for checksum, paths in checksums.items():
    if len(paths) > 1:
        print(f'  {paths}')
