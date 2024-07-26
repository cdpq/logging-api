from flask import Flask, jsonify, request

app = Flask(__name__)

#This is in the main app, normaly. I removed the whole datastruct.
projets = {}
elements = {}


@app.route('/projets', methods=['GET'])
def obtenir_projets():
    return jsonify(list(projets.keys()))


@app.route('/projets/<id_projet>', methods=['GET'])
def obtenir_elements_projet(id_projet):
    elements_projet = projets.get(id_projet, [])  #I removed the whole datastructure to keep it simple...
    return jsonify(elements_projet)


@app.route('/projets/<id_projet>/sousprojets', methods=['GET'])
def obtenir_sousprojets(id_projet):
    sousprojets = projets.get(id_projet, []) #I removed the whole datastructure to keep it simple...
    return jsonify(sousprojets)


@app.route('/projets', methods=['POST'])
def ajouter_projet():
    donnees = request.json
    id_projet = donnees.get('id_projet')   #I removed the whole datastructure to keep it simple...
    projets[id_projet] = []
    return "Fait"


@app.route('/projets/<id_projet>/elements', methods=['POST'])
def ajouter_element(id_projet):
    donnees = request.json
    id_element = donnees.get('id_element')  
    donnees_element = donnees.get('donnees_element')  

    projets[id_projet].append({'id_element': id_element, 'donnees_element': donnees_element}) #I removed the whole datastructure to keep it simple...
    return "Fait"


@app.route('/projets/<id_projet>/telecharger/<id_element>', methods=['GET'])
def telecharger_element(id_projet, id_element):
    elements_projet = projets[id_projet]
    element = next((e for e in elements_projet if e['id_element'] == id_element), None)  #I removed the whole datastructure to keep it simple...

    if element is None:
        return "Not Found", 404

    #File transfert removed to simplify code
    return "Fait"


@app.route('/projets/<id_projet>', methods=['PUT'])
def mettre_a_jour_projet(id_projet):
    donnees = request.json
    projets[id_projet] = donnees.get('donnees_projet')

    return "Fait"


if __name__ == '__main__':
    app.run(debug=True)
