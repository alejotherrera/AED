import os
import pickle
from Parcial_4_CET_Registro_Profesionales import *

def cargar_archivo(fd,v,importe_base):
    n = len(v)
    m = open(fd,"wb")
    for i in range(n):
        if v[i].tipo_trabajo == 3 or v[i].tipo_trabajo == 4 or v[i].tipo_trabajo == 5:
            if v[i].importe > importe_base:
                pickle.dump(v[i], m)
    print("Archivo generado con exito!")
    m.close()

def mostrar_archivo(fd):
    m = open(fd,"rb")
    size = os.path.getsize(fd)
    print("Datos del archivo:\n")
    while m.tell() < size:
        a = pickle.load(m)
        to_string(a)
    m.close()
