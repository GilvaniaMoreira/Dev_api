from flask import Flask, jsonify, request
import json

app = Flask(__name__)

desenvolvedores = [
    {'nome':'Rafael',
    'habilidades':['Python', 'Flask']
    },
    {'nome':'Gilvânia',
    'habilidades':['Python', 'Django']}
]

@app.route('/api_rest<int:id>/', methods=['GET', 'PUT'])
def desenvolvedor(id):
    if request.method == 'GET':
        desenvolvedor = desenvolvedores(id)
        print(desenvolvedor)
        return jsonify({desenvolvedor})
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedor[id] = dados
        return jsonify(dados)


if __name__ == '__main__':
    app.run(debug=True)