#!/usr/bin/env python3
from shutil import rmtree, copytree,  ignore_patterns
from zipfile import ZipFile
from datetime import datetime
from pathlib import Path
from threading import Thread
from progress.spinner import Spinner
import os
import logging
import click


@click.command()
@click.option('-v', '--verbose', type=click.BOOL, is_flag=False, help='Exibe os arquivos que estão sendo copiados.')
@click.option('-ig', '--ignore', multiple=True, help='ignora diretórios expecificos passados como parâmetro.')
@click.argument('source', required=True)
@click.argument('dest', required=True)
def init_app(source, dest, verbose, ignore):
    """ Use esse script para fazer backup do seu sistema linux.
    O script recebe dois respectivos argumentos. O primeiro é o caminho do diretório escolhido para backup.
    O segundo é o caminho do destinho do backup que será feito.
    Ao executar o script será ignorado as pastas: 'node_modules', '.git', 'venv', 'env', '.env', '.venv"""

    date = datetime.now()
    backup_folder = str(f'/backup_{date.strftime("%d_%B_%Y")}')
    backup_path = dest + backup_folder
    zip_dest = dest + f'/backup_{date.strftime("%d_%B_%Y.zip")}'
    directory = Path(backup_path)
    ignore_folders = ['node_modules', '.git', 'venv', 'env', '.env', '.venv']
    logging.basicConfig(filename='backup.log',
                        level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
    if ignore:
        [ignore_folders.append(v) for v in ignore]

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
                     ignore=ignore_patterns(*ignore_folders))

            with ZipFile(zip_dest, 'w') as zip:
                for file in directory.rglob("*"):
                    if verbose:
                        click.echo(f'Copiando {file} para {zip_dest}')
                    zip.write(file, arcname=file.relative_to(directory))
                rmtree(backup_path, ignore_errors=True)
                logging.info('Backup concluido')
        except Exception as e:
            logging.warning(e)

    backup_thread = Thread(target=backup)
    backup_thread.start()

    if not verbose:
        spinner = Spinner('Realizando backup ')
        while backup_thread.is_alive():

            spinner.next()


init_app()
