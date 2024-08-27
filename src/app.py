from flask import Flask, jsonify, request
app = Flask(__name__)

some_data = { "name": "Bobby", "lastname": "Rixer" }
todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

@app.route('/myroute', methods=['GET'])
def hello_world():
    # return 'Hello World!'

    # You can convert that variable into a json string like this
    json_text = jsonify(some_data)

    # And then you can return it to the front end in the response body like this
    return json_text

@app.route('/todos', methods=['GET'])
def hello_todos():
    response = jsonify(todos)
    return response

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.get_json(force = True)
    todos.append(request_body)
    response = jsonify(todos)
    return response

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete:", position)
    todos.pop(position)
    response = jsonify(todos)
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)