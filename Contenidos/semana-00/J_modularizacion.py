## Path relativo

path_relativo = 'data/archivo.txt'

with open(path_relativo, 'rt') as archivo:
    lineas = archivo.readlines()

print(lineas)