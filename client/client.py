import requests
import os
import time

def get_info():

    command = 'docker run -it -v /var/run/docker.sock:/var/run/docker.sock docker stats --no-stream  --format "table #{{.Container}}#{{.Name}}#{{.CPUPerc}}#{{.MemUsage}}"'

    info = os.popen(command).read()

    info = info.split('#')[5:] #remove column names

    content = {
        'time': time.time(),
        'id_cont': info[0],
        'name': info[1],
        'CPU': info[2],
        'Mem': info[3]
    }

    return content

def run():

    while(1):

        print('''
            1. Enviar POST
            2. Enviar GET
            3. Finalizar processo
        ''')

        option = input("Digite a opcao: ")

        if(option == '1'):
            response = requests.post('http://http://192.168.33.10:5001', json=get_info())
            print(response.status_code)
            print(response.content)

        elif(option == '2'):
            response = requests.get('http://192.168.33.10:5001')
            print(response.status_code)
            print(response.content)

        else:
            exit()


if __name__ == "__main__": 
    run()

