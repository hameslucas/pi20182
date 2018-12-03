from errbot import botflow, FlowRoot, BotFlow, FLOW_END


class ConsultaFlow(BotFlow):
    'Agendamento de consulta'


    @botflow
    def agendamento(self, flow: FlowRoot):
        'Consulta'
        etapa1 = flow.connect('consulta', auto_trigger=True)
        etapa2 = etapa1.connect('localizacao')
        etapa3 = etapa2.connect('especialidade')
        etapa4 = etapa3.connect('horario')

        etapa2.connect(FLOW_END, predicate=lambda ctx: ctx['fim'] == True)
        etapa3.connect(FLOW_END, predicate=lambda ctx: ctx['fim'] == True)
        etapa4.connect(FLOW_END, predicate=lambda ctx: ctx['fim'] == True)
