import requests
import time
import json

def get_info():
    
    try:
        response = requests.get('http://192.168.33.11/stats')
        info = json.loads(response.content)    
        return info
    except:
        pass

def run():

    while(1):

        print('''
            1. Enviar POST
            2. Enviar GET
            3. Finalizar processo
        ''')

        option = input("Digite a opcao: ")

        if(option == '1'):
            response = requests.post('http://192.168.33.10:5001', json=get_info())
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
