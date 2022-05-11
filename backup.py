#!/usr/bin/env python3
from shutil import rmtree, copytree,  ignore_patterns
from zipfile import ZipFile
from datetime import datetime
from pathlib import Path
import os
import logging
import click
from threading import Thread
from progress.spinner import Spinner


@click.command()
@click.option('--v', is_flag=False)
@click.argument('source', required=True)
@click.argument('dest', required=True)
def init_app(source, dest, v):
    """ Use esse script para fazer backup do seu sistema linux.
    O script recebe dois respectivos argumentos. O primeiro é o caminho do diretório escolhido para backup.
    O segundo é o caminho do destinho do backup que será feito.
    Ao executar o script será ignorado as pastas: 'node_modules', '.git', 'venv', 'env', '.env', '.venv"""

    date = datetime.now()
    backup_folder = str(f'/backup_{date.strftime("%d_%B_%Y")}')
    backup_path = dest + backup_folder
    zip_dest = dest + f'/backup_{date.strftime("%d_%B_%Y.zip")}'
    directory = Path(backup_path)
    logging.basicConfig(filename='backup.log',
                        level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

    if not os.path.exists(source):
        logging.warning('Caminho para backup não encontrado')
        click.echo('Caminho para backup não encontrado')
        return

    if not os.path.exists(dest):
        logging.warning('Caminho de destinho não encontrado')
        click.echo('Caminho de destinho não encontrado')
        return

    if os.path.isdir(backup_path):
        rmtree(backup_path, ignore_errors=True)

    def backup():
        try:
            copytree(source, backup_path,
                     ignore=ignore_patterns('node_modules', '.git', 'venv', 'env', '.env', '.venv'))

            with ZipFile(zip_dest, 'w') as zip:
                for file in directory.rglob("*"):
                    if v:
                        click.echo(f'Copiando {file} para {zip_dest}')
                    zip.write(file, arcname=file.relative_to(directory))
                logging.info('Backup concluido')
        except Exception as e:
            logging.warning(e)

    backup_thread = Thread(target=backup)
    backup_thread.start()

    if not v:
        spinner = Spinner('Realizando backup ')
        while backup_thread.is_alive():

            spinner.next()

        rmtree(backup_path, ignore_errors=True)

        click.echo('\nBackup concluido.')


init_app()
