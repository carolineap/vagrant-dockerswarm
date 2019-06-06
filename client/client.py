import requests

content = { 'time':'10:20',
            'name':'teste',
            'id_cont':'1',
            'id_img':'21',
            'CPU':'1',
            'Mem':'2048'}

def run():
    while(1):

        print('''
            1. Enviar POST
            2. Enviar GET
            3. Finalizar processo
        ''')
        option = input("Digite a opcao: ")

        if(option == '1'):
            r = requests.post('http://localhost:8080', json=content)
            print(r.status_code)
            print(r.content)

        elif(option == '2'):
            response = requests.get('http://localhost:8080')
            print(response.status_code)
            print(response.content)

        else:
            exit()

if __name__ == "__main__":

    run()