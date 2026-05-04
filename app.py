from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'título': 'O Senhor dos Anéis - A Sociedade do Anel',
        'autor': 'J.R.R Tolkien'
    },
    {
        'id': 2,
        'título': 'O Senhor dos Anéis - As Duas Torres',
        'autor': 'J.R.R Tolkien'
    },
    {
        'id': 3,
        'título': 'O Senhor dos Anéis - O Retorno do Rei',
        'autor': 'J.R.R Tolkien'
    },
    {
        'id': 4,
        'título': 'O Hobbit',
        'autor': 'J.R.R Tolkien'
    }
]


@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)

app.run(port=5000, host='localhost', debug=True)
