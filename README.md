# Sistema de Recomendações - Livros  📚
Olá saudações !

Este projeto tem como finalidade boas práticas de programação, além de conhecimentos específicos na linguagem Python, onde utilizamos recursos e libs como Flask, sckit , pandas. Trabalho cujo está sendo ministrado na disciplina de Introdução a Inteligência Computacional no 6 º período do curso de Bacharelado de Sistemas de Informações no 2 º semestre letivo de 2023/2024 . com intuito de consolidar conhecimentos foi proposto por meio do nossa Professora elaborar uma aplicação utilizando microserviços com base nos algoritmos de classificação (Inteligência Artificial).

## 🚀 Começando

Essas instruções permitirão que você obtenha uma cópia do projeto em operação na sua máquina local para fins de desenvolvimento e teste.

Consulte **[Implantação](#-implanta%C3%A7%C3%A3o)** para saber como implantar o projeto.


### 📋 Pré-requisitos & 🔧 Instalação

De que coisas você precisa para instalar o software e como instalá-lo?

Independente do sistema operacional que esteja , verifique se possui o Python e sua versão instalada na sua máquina.


1 . Faça o Clone do Projeto



```
https://github.com/peulearning/system_recommendations.git

```

2 . Nas depedências do projeto rodar no terminal se estiver utilizando PYTHON

```
pip install -r requirements.txt

```

3 . Para inicializar deve está conectado a internet e fazer as configurações na pasta ``src``,e no arquivo  ``app.py``, os parâmetros a serem modificados estão comentados.

4 . Em seguida deve acessar no terminal os comandos abaixo

```
cd src

flask run app

```

5 . Faça o passo anterior para acessar sistema de recomendações !


### 🔩 Analise os testes de ponta a ponta

```
  Teste de funcionalidade básica:

Verificar se é possível inserir uma avaliação de livro no sistema.
Verificar se o sistema é capaz de recomendar os 10 melhores livros com base na avaliação inserida pelo usuário.
Verificar se os livros recomendados estão de acordo com a nota inserida pelo usuário.
Testar a capacidade do sistema em lidar com diferentes notas de avaliação (de 1 a 10).

Teste de integração com banco de dados:

Verificar se as avaliações dos usuários são armazenadas corretamente no banco de dados.
Testar se as informações dos livros e dos usuários são corretamente recuperadas do banco de dados durante o processo de recomendação.
Teste de segurança:

Verificar se o sistema tem proteção contra acessos não autorizados.
Testar se as informações dos usuários são armazenadas de forma segura no banco de dados.
Verificar se há proteção contra possíveis ataques de injeção de SQL.

Teste de usabilidade:

Avaliar a facilidade de uso do sistema para inserir uma avaliação de livro.
Verificar se a interface do usuário é intuitiva e fácil de entender.
Coletar feedback dos usuários sobre a experiência de usar o sistema de recomendação.

Teste de desempenho:

Avaliar o tempo de resposta do sistema ao recomendar os livros.
Testar a capacidade do sistema em lidar com um grande número de usuários simultaneamente.
Identificar possíveis gargalos de desempenho e otimizar o sistema conforme necessário.

Teste de integração com sistemas externos:

Verificar se o sistema pode se integrar com bancos de dados externos de livros para obter informações adicionais.
Testar a capacidade do sistema em se integrar com sistemas de pagamento para oferecer opções de compra dos livros recomendados.

Teste de compatibilidade:

Verificar se o sistema funciona corretamente em diferentes navegadores web.
Testar a compatibilidade do sistema com dispositivos móveis, tablets e computadores desktop.
```

## 🛠️ Construído com

Mencione as ferramentas que você usou para criar seu projeto

- [Python](https://docs.python.org/pt-br/3/tutorial/) - PYTHON
- [Flask](https://flask.palletsprojects.com/en/3.0.x/) - MicroFramework
- [Colab](https://colab.research.google.com/drive/1hbqJIyM84Md3CmC7Tean340j-b3eSGIW?authuser=1#scrollTo=-rOLpL87LRHT) - Notebook

## 🖇️ Colaborando

Por favor, leia o [COLABORACAO.md](https://gist.github.com/usuario/linkParaInfoSobreContribuicoes) para obter detalhes sobre o nosso código de conduta e o processo para nos enviar pedidos de solicitação.

## 📌 Versão

(Final) - 03-03-2024 (Versão_Final)


## ✒️ Autores

Mencione todos aqueles que ajudaram a levantar o projeto desde o seu início

- **Profª Cleiane Gonçalves** - _Ideia do Projeto Inicial_ - [Orientadora]()

- **Pedro Henrique (EU)** - _Dev_

Você também pode ver a lista de todos os [colaboradores](https://github.com/usuario/projeto/colaboradores) que participaram deste projeto.

## 📄 Licença

Este projeto está sob a licença (sua licença) - veja o arquivo [LICENSE.md](https://github.com/usuario/projeto/licenca) para detalhes.

---

⌨️ com ❤️ por [Pedrão Ribeiro](https://github.com/peulearning) 😊
