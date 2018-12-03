from errbot import BotPlugin, botcmd, botmatch
from pymongo import MongoClient

class ConsultaBot(BotPlugin):
    'Mensagem'

    @botcmd
    def consulta(self, msg, args):
        yield "Agora, iremos coletar alguns dados seus para que possamos mostrar a voce as melhores opcoes de consultas na sua regiao, por favor informe os dados a seguir"
        yield "Por favor, informe a localizacao:"

    @botmatch(r'^[A-Z].*$', flow_only=True)
    def localizacao(self, msg, match):
        'Localizacao'
        msg.ctx['localizacao'] = match.string
        yield "Qual opcao deseja?"
        cliente = MongoClient().consulta.agendamento
        especialidades = set()
        for item in cliente.find({"local": msg.ctx['localizacao'] }):
            especialidades.add(item['especialidade'])
        for especialidade in especialidades:
            yield "/" + especialidade

    @botmatch(r'^[a-z].*$', flow_only=True)
    def especialidade(self, msg, match):
        'Especialidade'
        msg.ctx['especialidade'] = match.string
        cliente = MongoClient().consulta.agendamento
        disponibilidade = set()
        for item in cliente.find({'especialidade': match.string, "local": msg.ctx['localizacao'], "reservado": "nao"}):
            disponibilidade.add(item['datahora'])
        if len(disponibilidade) == 0:
            msg.ctx['fim'] = True
            yield "Nada disponivel"
        else:
            for item in disponibilidade:
                yield "/" + item

    @botmatch(r'^[0-9].*$', flow_only=True)
    def horario(self, msg, match):
        'Horario'
        msg.ctx['horario'] = match.string
        yield msg.ctx['horario']
        yield msg.ctx['localizacao']
        yield msg.ctx['especialidade']
        consulta_ao_banco = {"especialidade": msg.ctx['especialidade'], "local": msg.ctx['localizacao'], "datahora": msg.ctx['horario'] }
        valor_a_atualizar = { "$set": { "reservado": "sim"} }
        cliente = MongoClient().consulta.agendamento
        cliente.update(consulta_ao_banco, valor_a_atualizar)
