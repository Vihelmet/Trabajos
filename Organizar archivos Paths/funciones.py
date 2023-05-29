import os
import shutil


def organizar_archivos():
    directorio_descargas = os.path.expanduser('~/Descargas') 
    directorio_imagenes = os.path.join(directorio_descargas, 'Imagenes') 
    directorio_documentos = os.path.join(directorio_descargas, 'Documentos') 
    directorio_software = os.path.join(directorio_descargas, 'Software') 
    directorio_otros = os.path.join(directorio_descargas, 'Otros') 
    
    
    for directorio in [directorio_imagenes, directorio_documentos, directorio_software, directorio_otros]:
        if not os.path.exists(directorio):
            os.makedirs(directorio)
    
    
    for archivo in os.listdir(directorio_descargas):
        origen = os.path.join(directorio_descargas, archivo) 
        if os.path.isfile(origen):
            extension = os.path.splitext(archivo)[1].lower() 
            if extension in ['.jpg', '.jpeg', '.png', '.svg', '.gif', '.tif', '.tiff']:
                destino = os.path.join(directorio_imagenes, archivo) 
            elif extension in ['.doc', '.docx', '.txt', '.pdf', '.xls', '.ppt', '.xlsx', '.pptx']:
                destino = os.path.join(directorio_documentos, archivo) 
            elif extension in ['.exe', '.pkg', '.dmg']:
                destino = os.path.join(directorio_software, archivo) 
            else:
                destino = os.path.join(directorio_otros, archivo) 
            shutil.move(origen, destino)

