from flask import Flask
app = Flask(__name__)



@app.route('/todos', methods=['GET'])
# def hello_world():
#     return "<h1>Hello!</h1>"

def hello_world():
    # supongamos que tienes some_data (cierta información) en una variable json
    todos = { "name": "Bobby", "lastname": "Rixer" }

    # puedes convertir esa variable en un string json así
    json_text = flask.jsonify(some_data)

    # y luego puedes retornarla (return) en el response body así:
    return json_text


todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]





# Estas dos líneas siempre seben estar al final de tu archivo app.py.

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)