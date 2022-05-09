from shutil import rmtree, copytree,  ignore_patterns
from zipfile import ZipFile
from datetime import datetime
from pathlib import Path
import os
import sys
import re
import logging

# primeiro arg = caminho_para ler
# segundo arg = caminho_para_criar_backup


def init_app():
    date = datetime.now()
    args = sys.argv
    backup_folder = str(f'/backup_{date.strftime("%d_%B_%Y")}')
    logging.basicConfig(filename='example.log',
                        level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

    if args:
        del(args[0])
        if len(args) == 0 or len(args) == 1 or len(args) > 2:
            logging.warning('Você precisa passar 2 parâmetros')
            return

        for arg in args:
            if not re.search('/', arg):
                logging.warning('Você passou argumentos inválido')
                return

        src_path = args[0]
        backup_path = args[1] + backup_folder
        directory = Path(backup_path)

    if not os.path.exists(src_path):
        logging.warning('Caminho para backup não encontrado')
        return

    if not os.path.exists(args[1]):
        logging.warning('Caminho de destinho não encontrado')
        return

    if os.path.isdir(backup_path):
        rmtree(backup_path, ignore_errors=True)

    try:
        copytree(src_path, backup_path,
                 ignore=ignore_patterns('node_modules', '.git', 'venv', 'env', '.env', '.venv'))

        with ZipFile(args[1] + f'/backup_{date.strftime("%d_%B_%Y.zip")}', 'w') as zip:
            for file in directory.rglob("*"):
                zip.write(file, arcname=file.relative_to(directory))
            logging.info('Backup concluido')
    except Exception as e:
        logging.warning(e)

    rmtree(backup_path, ignore_errors=True)


init_app()
