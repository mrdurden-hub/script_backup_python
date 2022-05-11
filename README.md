# Script backup python

**Simples script desenvolvido em python para fazer backup de diretórios de projetos python e javascript.**

> Script desenvolvido para plataforma linux.

## Como funciona

_O script recebe dois caminhos como argumentos que são passados no momento em que o mesmo é executado._

_O primeiro argumento é o caminho onde o script vai ler os arquivos para fazer o backup. O segundo argumento é o caminho de destinho onde será gerado um arquivo zip do backup realizado._

_O script ignora as seguinte pastas: 'venv', 'env', '.venv','.env', 'node_modules' e '.git'_

_Ao executar o script é gerado um arquivo .log com as informações do status do backup._

## Como usar o script

_Para executar o script é só clonar o repositório:_

```
git clone https://github.com/mrdurden-hub/script_backup_python.git
```

_Entre no diretório do script:_

```
cd script_backup_python
```

_Você pode executar utilizando o python já instalado no seu sistema ou então utilizar um ambiente virtual._

_Esse projeto usa o poetry como gerenciador de dependecias. Caso você nao tenha, será necessario instala-lo para ativar o ambiente virtual._

_Para ativar o ambiente virtual use os seguintes comandos:_

```
poetry shell
```

_Agora é preciso instalar as dependencias:_

```sh
poetry install
```

_Agora é só executar o script com python e passar os argumentos:_

```sh
python backup.py /home/user/diretorio_backup ~/destinho
```

_Ao executar o comando acima o script vai fazer backup de tudo que estiver dentro de `/home/user/diretorio_backup` e gerar um arquivo .zip em `~/destinho`_.

## Usando opções

_O script pode receber duas opções como parâmetro:_

| opç            | Descrição                                                                           | Tipo    |
| -------------- | ----------------------------------------------------------------------------------- | ------- |
| -v / --verbose | Exibe os arquivos que estão sendo feito o backup. Por padrão é definido como false. | Boolean |
| -ig / --ignore | Recebe como parâmetro os diretório que serão ignorados.                             | String  |

## Exemplos

_Nesse exemplo vou fazer um backup usando as duas opções que descrevi acima._

```
./backup.py /home/user/backup_folder ~/dest -v true -ig node_modules
```

_Primeiro executei o arquivo `./backup.py`, depois passei o primeiro parâmetro que é a pasta escolhida para o backup `/home/user/backup_folder`, em seguida passei o segundo parâmetro que é o destino do backup (o caminho onde será criado o backup) `~/dest` e depois usei as duas opções. Primeiro estou usando a opção`-v` para `true` indicando que quero ver os arquivos sendo copiados e depois estou utilizando a opção `-ig` para indicar quais diretórios eu quero que o script ignore. Nesse exemplo usei `node_modules` como você viu acima, mas você pode passar qualquer outro valor, sem limites de quantidades._
<br />
_Você também pode usar a opção `--help` no terminal caso ainda tenha alguma dúvida._

_Voce terá uma saída como essa:_

```
(.venv) ➜  script_backup_python git:(main) ✗ ./backup.py --h
elp
Usage: backup.py [OPTIONS] SOURCE DEST

  Use esse script para fazer backup do seu sistema linux.
  O script recebe dois respectivos argumentos. O primeiro
  é o caminho do diretório escolhido para backup. O
  segundo é o caminho do destinho do backup que será
  feito. Ao executar o script será ignorado as pastas:
  'node_modules', '.git', 'venv', 'env', '.env', '.venv

Options:
  -v, --verbose BOOLEAN  Exibe os arquivos que estão sendo
                         copiados.
  -ig, --ignore TEXT     ignora diretórios expecificos
                         passados como parâmetro.
  --help                 Show this message and exit.
```

### Autor

- [mrdurden-hub](https://github.com/mrdurden-hub)
