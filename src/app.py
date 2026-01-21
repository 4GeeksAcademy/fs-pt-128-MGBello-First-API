from flask import Flask, jsonify, request

app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]



@app.route('/todos', methods=['GET'])
def hello_world(): 
    json_text = jsonify(todos)
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    data = request.get_json()
    requiered_field = ['label']
    missing = [field for field in requiered_field if field not in data]
    if missing : 
        return jsonify('Error: label is missing'), 404
    data['done'] = False
    todos.append(data)
    return jsonify(todos), 200

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    if len(todos) > position:
        todos.pop(position)
        return jsonify(todos), 200
    return jsonify(f'Error: la posicion {position}, no existe '), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)

