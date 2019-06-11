from flask import Flask, jsonify, request
import time
import os

app = Flask(__name__)

@app.route('/stats', methods=['GET', 'POST'])
def get_info():

    command = 'docker run -it -v /var/run/docker.sock:/var/run/docker.sock docker stats --no-stream  --format "table #{{.Container}}#{{.Name}}#{{.CPUPerc}}#{{.MemUsage}}"'

    info = os.popen(command).read()

    info = info.split('#')[5:] #remove column names

    content = {
        'time': time.time(),
        'id_cont': info[0],
        'name': info[1],
        'CPU': info[2],
        'Mem': info[3]    }

    return jsonify(content)


if __name__ == "__main__":
    app.run('0.0.0.0', debug=True, port=80)