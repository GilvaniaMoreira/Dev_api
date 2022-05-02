from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from habilidades import Habilidades
import json


app = Flask(__name__)
api = Api(app)

desenvolvedores = [
    {
    'id':'0',
    'nome':'Rafael',
     'habilidades':['Python', 'Flask']
    },
    {
    'id':'1',
    'nome':'Galleani',
     'habilidades':['Python', 'Django']}
]

#devolve um desenvolvedor pelo ID, também altera e deleta e deleta um desenvolvedor
class desenvolvedor(Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = f'Desenvolvedor de ID {id} não existe'
            response = {'status':'erro', 'mensagem':mensagem}
            return jsonify(response)
        except Exception:
            mensagem = 'Erro desconhecido. Procure o administrador da API'
            response = {'status':'erro', 'mensagem':mensagem}
        return response

    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados
    
    def delete(self, id):
        desenvolvedores.pop(id)
        dados = json.loads(request.data)
        return jsonify({'status':'sucesso', 'mensagem':'Registro excluido'})

#Lista todos os desenvoldedor e permite registrar um novo desenvolvedor
class ListaDesenvolvedores(Resource):
    def get(self):
        return desenvolvedores
    
    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados[id] = posicao
        desenvolvedores.append(dados)
        return jsonify(desenvolvedores[posicao])

    
api.add_resource(desenvolvedor, '/dev/<int:id>/')
api.add_resource(ListaDesenvolvedores, '/dev/')
api.add_resource(Habilidades, '/habilidade/')
if __name__ == '__main__':
    app.run(debug=True)