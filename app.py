# API - É um lugar para disponibilizar recursos e/ou funcionalidades
# Para criarmos uma API temos que ter em Mente
# 1 Objetivo - Criar uma API que disponibiliza a consulta, criação, edição e exclusão de livros.
# 2 URL base - no caso será localhost, mas geralmente é tipo google.com/api/serviços
# 3 Endpoints - 
  # - localhost/livros (GET)
  # - localhost/livros (POST)
  # - localhost/livros/ id (GET)
  # - localhost/livros/ id (PUT)
  # - localhost/livros (DELETE)
# 4 Quais recursos - Livros

from flask import Flask, jsonify, request

app = Flask(__name__)