import platform
import cpuinfo
import socket
from flask import Flask, render_template

app = Flask(__name__)

#j'ai rien trouvé a recupere avec l'import os
# On recuperer les informations via la classe informations
class Informations:
    def __init__(self):
        self.os = platform.system()
        self.osversion = platform.version()
        self.cpu = cpuinfo.get_cpu_info()["brand_raw"]
        self.cpuheart = cpuinfo.get_cpu_info()['count']
        self.nom = socket.gethostname()
        self.ip = socket.gethostbyname(self.nom)

#sur la route / on recupere le info et on fait un render dans le template index.html prévu pour
@app.route('/')
def hello():
    system_info = Informations()
    return render_template('index.html',
        os=system_info.os,
        osversion=system_info.osversion,
        cpu=system_info.cpu,
        cpuheart=system_info.cpuheart,
        nom=system_info.nom,
        ip=system_info.ip)