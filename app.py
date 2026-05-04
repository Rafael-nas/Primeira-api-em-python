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

@app.route('/livros/<int:id>', methods=['GET'])
def obter_livro_por_id(id):
    livro = next((livro for livro in livros if livro['id'] == id), None)
    if livro:
        return jsonify(livro)
    return jsonify({'mensagem': 'Livro não encontrado'}), 404

@app.route('/livros', methods=['POST'])
def adicionar_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify(novo_livro), 201

@app.route('/livros/<int:id>', methods=['PUT'])
def atualizar_livro(id):
    livro = next((livro for livro in livros if livro['id'] == id), None)
    if livro:
        dados_atualizados = request.get_json()
        livro.update(dados_atualizados)
        return jsonify(livro)
    return jsonify({'mensagem': 'Livro não encontrado'}), 404

app.run(port=5000, host='localhost', debug=True)
