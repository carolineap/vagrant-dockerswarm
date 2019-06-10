from flask import Flask, jsonify, request

json_map = {}

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    global json_map

    if request.method == 'POST':

        request_json = request.get_json()
        json_map["time"] = request_json.get('time')
        json_map["name"] = request_json.get('name')
        json_map["id_cont"] = request_json.get('id_cont')
        json_map["id_img"] = request_json.get('id_img')
        json_map["CPU"] = request_json.get('CPU')
        json_map["Mem"] = request_json.get('Mem')

        return jsonify(json_map)

    else:

        return jsonify(json_map)

if __name__ == "__main__":

    app.run(host='0.0.0.0', port=80)