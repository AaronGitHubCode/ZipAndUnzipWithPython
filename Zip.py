def contenidoZip(path_zip: str) -> None:
    from zipfile import Path

    try:
        zipDir: Path = Path(path_zip)
    except(FileNotFoundError):
        print('ERROR: Archivo ZIP inválido o corrupto')
        return

    print('-- Contenido Zip --')
    for i in zipDir.iterdir():
        for j in i.iterdir():
            if j.is_dir():
                print('\n' + str(j))
                for k in j.iterdir():
                    print(f'|\n------>{str(k)}')
            else:
                print(j)


def descomprimirZip(zip_file: str, extract_dir: str) -> None:
    from zipfile import ZipFile

    dirZip: ZipFile = ZipFile(zip_file, 'r')

    dirZip.extractall(path=extract_dir)



def comprimirFichero(zip_file: str, directory: str) -> None:
    from zipfile import ZipFile, ZIP_BZIP2, ZIP_DEFLATED, Path
    import os

    try:
        fileZip: ZipFile = ZipFile(file=zip_file, mode='w', compression=ZIP_BZIP2, allowZip64=True)
    
        if Path(fileZip).exists() == False:
            fileZip.filename = zip_file
            for folder, subfolders, files in os.walk(directory):
                for subfolder in subfolders:
                    fileZip.write(os.path.join(folder,subfolder), os.path.relpath(os.path.join(folder,subfolder), directory))
                for file in files:
                    fileZip.write(os.path.join(folder,file), os.path.relpath(os.path.join(folder,file), directory))



    except IOError as io:
        print('Error: ' + io.strerror)
    finally:
        fileZip.close()

