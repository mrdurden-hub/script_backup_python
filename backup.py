from shutil import rmtree, copytree,  ignore_patterns
from zipfile import ZipFile
from datetime import datetime
from pathlib import Path
import os
import sys
import re

date = datetime.now()
args = sys.argv
backup_folder = str(f'/backup_{date.strftime("%d_%B_%Y")}')


def init_app():
    # primeiro arg = caminho_para ler
    # segundo arg = caminho_para_criar_backup
    if args:
        del(args[0])
        if len(args) == 0 or len(args) == 1 or len(args) > 2:
            print('Erro: Você precisa passar 2 parâmetros')
            return

        for arg in args:
            if not re.search('/', arg):
                print('Você passou argumentos inválido')
                return

        src_path = args[0]
        backup_path = args[1] + backup_folder
        directory = Path(backup_path)

    if not os.path.exists(src_path):
        print('Erro: Caminho para backup não encontrado')
        return

    if not os.path.exists(args[1]):
        print('Erro: Caminho de destinho não encontrado')
        return

    if os.path.isdir(backup_path):
        rmtree(backup_path, ignore_errors=True)

    copytree(src_path, backup_path,
             ignore=ignore_patterns('node_modules', '.git', 'venv', 'env', '.env', '.venv'))
    print('arquivos copiados')

    with ZipFile(args[1] + f'/backup_{date.strftime("%d_%B_%Y.zip")}', 'w') as zip:
        for file in directory.rglob("*"):
            zip.write(file, arcname=file.relative_to(directory))

    rmtree(backup_path, ignore_errors=True)


init_app()
