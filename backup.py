#!/usr/bin/env python3
from pydoc import cli
from shutil import rmtree, copytree,  ignore_patterns
from zipfile import ZipFile
from datetime import datetime
from pathlib import Path
import os
import sys
import re
import logging
import click
from threading import Thread
from progress.spinner import Spinner


@click.argument('source', required=True)
@click.argument('dest', required=True)
@click.command()
def init_app(source, dest):
    """ Use esse script para fazer backup do seu sistema linux.
    O script recebe dois respectivos argumentos. O primeiro é o caminho do diretório escolhido para backup.
    O segundo é o caminho do destinho do backup que será feito.
    Ao executar o script será ignorado as pastas: 'node_modules', '.git', 'venv', 'env', '.env', '.venv"""

    spinner = Spinner('Realizando backup ')
    date = datetime.now()
    args = sys.argv
    backup_folder = str(f'/backup_{date.strftime("%d_%B_%Y")}')
    logging.basicConfig(filename='backup.log',
                        level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
    if args:
        del(args[0])
        if len(args) == 0 or len(args) == 1 or len(args) > 2:
            logging.warning('Você precisa passar 2 parâmetros')
            click.echo(
                'Você precisa indicar o caminho de backup e o caminho de destinho.')
            return

        for arg in args:
            if not re.search('/', arg):
                logging.warning('Você passou argumentos inválido')
                click.echo('Você passou argumentos inválido')
                return

        src_path = args[0]
        backup_path = args[1] + backup_folder
        directory = Path(backup_path)

    if not os.path.exists(src_path):
        logging.warning('Caminho para backup não encontrado')
        click.echo('Caminho para backup não encontrado')
        return

    if not os.path.exists(args[1]):
        logging.warning('Caminho de destinho não encontrado')
        click.echo('Caminho de destinho não encontrado')
        return

    if os.path.isdir(backup_path):
        rmtree(backup_path, ignore_errors=True)

    def backup():
        try:
            copytree(src_path, backup_path,
                     ignore=ignore_patterns('node_modules', '.git', 'venv', 'env', '.env', '.venv'))

            with ZipFile(args[1] + f'/backup_{date.strftime("%d_%B_%Y.zip")}', 'w') as zip:
                for file in directory.rglob("*"):
                    zip.write(file, arcname=file.relative_to(directory))
                logging.info('Backup concluido')
        except Exception as e:
            logging.warning(e)

    backup_thread = Thread(target=backup)
    backup_thread.start()

    while backup_thread.is_alive():

        spinner.next()

    rmtree(backup_path, ignore_errors=True)

    click.echo('\nBackup concluido.')


init_app()
