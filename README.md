# Boas-vindas ao repositório do projeto `Algorithms`!

Projeto invidual feito em python.

O projeto Algorithms visa resolver problemas e otimizar algoritmos e implementar soluções para os mais diversos problemas do dia a dia!

  ## 🚵 Habilidades exercitadas:
Lógica;

Capacidade de interpretação de problemas;

Capacidade de interpretação de um código legado;

Capacidade de otimizar a resolução de problemas e;

Resolver problemas/Otimizar algoritmos sob pressão.
## Stack utilizada

**Python3**


## Instalação

```bash
Clone o repositório:
Use o comando: git@github.com:lbseven7/algorithms.git

Entre na pasta do repositório que você acabou de clonar:
cd algorithms

Crie o ambiente virtual para o projeto:
python3 -m venv .venv && source .venv/bin/activate

Instale as dependências:
python3 -m pip install -r dev-requirements.txt
```

## Linter
Para garantir a qualidade do código, foi utilizado neste projeto o linter `Flake8`.
  Assim o código estará alinhado com as boas práticas de desenvolvimento, sendo mais legível
  e de fácil manutenção! Para rodá-lo localmente no projeto, execute o comando abaixo:

```bash
python3 -m flake8
```

## Ambiente Virtual
1 - Criar o ambiente virtual
```bash
python3 -m venv .venv
```
2 - Ative o ambiente virtual
```bash
source .venv/bin/activate
```
3 - Instale as dependências no ambiente virtual
```bash
$ python3 -m pip install -r dev-requirements.txt
```
Caso precise desativar o ambiente virtual, execute o comando "deactivate". ￼ Lembre-se de ativar novamente o ambiente virtual quando voltar a trabalhar no projeto.

O arquivo dev-requirements.txt contém todas as dependências que serão utilizadas no projeto, ele está agindo como se fosse um package.json de um projeto Node.js.


## Estrutura do Projeto

Este repositório é composto pela pasta `challenges` que contém todos os arquivos que você utilizará neste projeto.
129
​
130
  Cada arquivo `.py`, dentro da pasta `challenges` representa um desafio, ou seja, os arquivos não têm ligação uns com os outros.
131
  Logo, os problemas devem ser resolvidos de forma separada.
132
​
133
  Este repositório já contém um _template_ com a estrutura de diretórios e arquivos, tanto de código quanto de teste criados. Veja abaixo:

```
136
  .
137
  ├── challenges
138
  │   ├──🔹 challenge_anagrams.py
139
  │   ├──🔸 challenge_encrypt_message.py
140
  │   ├──🔹 challenge_find_the_duplicate.py
141
  │   ├──🔹 challenge_palindromes_iterative.py
142
  │   ├──🔹 challenge_palindromes_recursive.py
143
  │   └──🔹 challenge_study_schedule.py
144
  ├── tests
145
  │   ├── encrypt
146
  │   │   ├──🔸 __init__.py
147
  │   │   ├──🔸 conftest.py
148
  │   │   ├──🔸 mocks.py
149
  │   │   └──🔹 test_encrypt.py
150
  │   ├── resultados
151
  │   │   └──🔸 .gitignore
152
  │   ├──🔸 __init__.py
153
  │   ├──🔸 complexities.py
154
  │   ├──🔸 geradores.py
155
  │   ├──🔸 marker.py
156
  │   ├──🔸 test_anagrams.py
157
  │   ├──🔸 test_find_the_duplicate.py
158
  │   ├──🔸 test_palindromes_iterative.py
159
  │   ├──🔸 test_palindromes_recursive.py
160
  │   └──🔸 test_study_schedule.py
161
  ├──🔸 dev-requirements.txt
162
  ├──🔸 pyproject.toml
163
  ├──🔸 README.md
164
  ├──🔸 requirements.txt
165
  ├──🔸 setup.cfg
166
  ├──🔸 setup.py
167
  ├──🔸 trybe-filter-repo.sh
168
  └──🔸 trybe.yml
169
​
170
Legenda:
171
  🔸 Arquivos que não podem ser alterados.
172
  🔹 Arquivos a serem alterados para realizar os requisitos.
173
```
## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://portfolio-iota-azure-34.vercel.app/)

[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/leobarbosa-dev/)

[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/LBarbosaDev)

