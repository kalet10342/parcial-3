import os, shutil
extenciones = {
    "Fotos": ['.jpg', '.jpeg', 'png'],
    "Videos": ['.mp4', '.avi', '.wav'],
    "Audio": ['.mp3'],
    "Documentos": ['.pdf', '.docx', '.dotx', ".xlsx", ".xlsm", ".xlsb", ".xltx", ".pptx", ".pptm", ".ppt"   ],
    "Ejecutables": ['.exe']
}   

def crearcarpetas(path):
    exts = obtenerextenciones(path)
    for i in extenciones.keys():
        for k in exts: 
            if k in extenciones[i] and not os.path.exists(path+i):
                os.mkdir(path+i)


def ordenar(path, archivo, ext):
    for i in extenciones.keys():
        if ext in extenciones[i]:
            try:
                shutil.move(path+archivo, path+i)
            except:
                print(f"ocurrio un error, no se pudo mover el archivo{archivo}")

def obtenerextenciones(path):
    exts = []
    for i in os.listdir(path):
        ext = os.path.splitext(i)[1]
        if ext not in extenciones and ext !="":
            exts.append(ext)

    return exts
            



def proceso(path):
    crearcarpetas(path)
    for archivo in os.listdir(path):
        ext = os.path.splitext(archivo)[1]
        ordenar(path, archivo, ext)

while True:
    path = input("Ingrese la direección de la carpeta a ordenar:")
    if os.path.exists(path):
        path += "/"
        break
    else:
        print("Error, el path ingresado no existe")

proceso(path)
print("Proceso finalizado")