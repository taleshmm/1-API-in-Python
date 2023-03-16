from flask import Flask, jsonify, request

app = Flask(__name__)

#Create an empty list and open the file by adding its id and in the dictionary
books = []
with open("books.txt", "r") as file:
  id = 1
  for line in file:
    values = line.strip().split(', ')
    book = {"id": id, "titulo": values[0], "autor": values[1], "ano": values[2]}
    books.append(book)
    id += 1

#Consult 
@app.route('/books', methods=['GET'])
def obtain_books():
  return jsonify(books)

#Consult by ID
@app.route('/books/<int:id>', methods=['GET'])
def obtain_books_id(id):
  for book in books:
    if book.get('id') == id:
      return jsonify(book)

#Edit
@app.route('/books/<int:id>', methods=['PUT'])
def edit_book_id(id):
  edit_book = request.get_json()
  for indice,book in enumerate(books):
    if book.get('id') == id:
      books[indice].update(edit_book)
      return jsonify(books[indice])

#Create
@app.route('/books/add', methods=['POST'])
def add_book():
  new_book = request.get_json()
  books.append(new_book)

  return jsonify(books)

# Delete
@app.route('/books/<int:id>', methods=['DELETE'])
def delet_book(id):
  for indice,book in enumerate(books):
    if book.get('id') == id:
      del books[indice]
    
  return jsonify(books)

app.run(port=5000, host='localhost', debug=True)