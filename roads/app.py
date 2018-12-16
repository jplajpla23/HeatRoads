from flask import Flask, Response, render_template
from contamehistorias.datasources.webarchive import ArquivoPT
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('home.html')

@app.route('/heat')
def  teste():
    domains = [ 'http://publico.pt/','https://www.dn.pt/']
    params = { 'domains':domains, 
            'from':datetime(year=2016, month=1, day=20), 
            'to':datetime(year=2017, month=12, day=10) }
    query = 'Acidente viação'
    apt =  ArquivoPT()
    search_result = apt.getResult(query=query, **params)
    return str(len(search_result))

    #var =" "
    #import spacy
    #nlp = spacy.load('pt_core_news_sm')
    #text = "Fonte do Comando Territorial de Coimbra da GNR tinha inicialmente dito à Lusa que o acidente tinha provocado duas vítimas mortais, corrigindo posteriormente a informação e esclarecendo que a colisão seguida de despiste provocou um morto.O acidente ocorreu por volta das 18:45, na zona de Oliveira do Mondego, concelho de Penacova (distrito de Coimbra), numa zona do IP3 sem separador central, disse à agência Lusa fonte da GNR.Registam-se ainda dois feridos graves e dois feridos ligeiros, acrescentou a mesma fonte, corrigindo também o número de viaturas envolvidas no acidente, sendo que a informação de um embate num quarto veículo acabou por não se confirmar.Segundo a mesma fonte, na sequência da primeira colisão, os ocupantes dos carros terão saído das viaturas, no momento em que um pesado de mercadorias se despistou e acabou por atropelá-los e por abalroar os dois veículos envolvidos no acidente inicial.Na sequência do acidente, o trânsito foi cortado nos dois sentidos no IP3, o que se mantinha pelas 21:25. A alternativa é a Estrada Nacional 2.Fonte do Comando Distrital de Operações de Socorro (CDOS) de Coimbra referiu que no local estão meios da GNR e do Instituto Nacional de Emergência Médica (INEM).O CDOS não tinha o registo dos bombeiros mobilizados para o terreno."
    #doc = nlp(text)
    #for token in doc.ents:
#       var+= str(token.text)+" "+ str(token.label_)+"\n"
#   return Response(var, mimetype="text/text")

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
    #app.run(host='0.0.0.0')
