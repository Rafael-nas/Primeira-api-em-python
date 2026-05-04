# Primeira API em Python

API simples de livros feita com Flask. O projeto expõe operações básicas de CRUD para uma lista em memória.

## Requisitos

- Python 3
- Flask

## URL base

```text
http://localhost:5000
```

## Endpoints

### Listar livros

- Método: `GET`
- Rota: `/livros`

### Buscar livro por ID

- Método: `GET`
- Rota: `/livros/<id>`

### Adicionar livro

- Método: `POST`
- Rota: `/livros`
- Exemplo de corpo JSON:

```json
{
	"id": 5,
	"título": "Silmarillion",
	"autor": "J.R.R Tolkien"
}
```

### Atualizar livro

- Método: `PUT`
- Rota: `/livros/<id>`

### Remover livro

- Método: `DELETE`
- Rota: `/livros/<id>`

## Observações

- Os dados ficam armazenados apenas em memória.
- Ao reiniciar a aplicação, a lista volta ao estado inicial definido em `app.py`.
