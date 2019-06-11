# vagrant-dockerswarm


#Execute em três terminais (um para o client, um para o server e um para capturar as informações do client com o docker stats) os seguintes comandos:

$ cd ~
$ git clone https://github.com/dcomp-leris/slice-enablers.git
$ cd slice-enablers
$ chmod 400 arquivos/cloud_ufscar_rsa.dms 
$ ssh -i cloud_ufscar_rsa.dms ubuntu@200.136.252.136
$ cd slice-enablers/arquivos
$ sh acessar.sh 5
$ cd tp1/

No primeiro terminal:

$vagrant ssh server

No segundo terminal:

$vagrant ssh client

No terceiro terminal:

$sudo python3 get_info.py

No terminal do client, execute:

$sudo docker run -ti client_app
