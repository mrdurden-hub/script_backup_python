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
