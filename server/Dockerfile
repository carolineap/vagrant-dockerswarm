from flask import Flask, jsonify, request
import time
import os

app = Flask(__name__)

@app.route('/stats', methods=['GET'])
def service_post(container_id):

    try:
        client = docker.from_env()
        container_id = client.containers.list()[0].id
        response = {}
        info = client.containers.get(container_id).stats(stream=False)
        response['id'] = info['id']
        response['image'] = client.containers.get(container_id).image.tags[0]
        response['name'] = info['name']
        response['timestamp'] = info['read']
        response['memory_usage'] = float(info['memory_stats']['usage']) / (1024.0 ** 2) # in MB
        cpu_delta = float(info['cpu_stats']['cpu_usage']['total_usage']) - float(info['precpu_stats']['cpu_usage']['total_usage'])
        system_delta = float(info['cpu_stats']['system_cpu_usage']) - float(info['precpu_stats']['system_cpu_usage'])
        response['cpu_usage'] = cpu_delta / system_delta
        return json.dumps(response)
    except:
        return ('An error ocurred')


run(host='0.0.0.0',port=80,debug=True)