import os
from time import sleep
import time as tempo
import logging
import strip
#os.system('query user')
#import csv

pastaCorrente= os.getcwd()

#Creating and Configuring Logger
'''Log_Format = "%(levelname)s %(asctime)s - %(message)s"

logging.basicConfig(filename = "logfile.log",
                    filemode = "w",
                    format = Log_Format, 
                    level = logging.DEBUG)

logger = logging.getLogger()

#Testing our Logger
logger.debug("++++++++++++++ inicio")'''

arquivo = open('sleepTimeSeconds.txt','r')
tempoSleep = arquivo.readline()
horaFim = arquivo.readline()
arquivo.close()

hora = tempo.strftime('%H%M%S', tempo.localtime())

while True:
    #logger.debug("while")

    pipe = os.popen('query user')
    tabela = pipe.read()

    with open('tabelaUser.txt', 'w') as w:
        w.write(tabela)

    w.close

    with open('Usuarios.txt', 'w') as u:
        with open ('tabelaUser.txt', 'r') as f:
            for line in f:
                #logger.debug("for line")

                print (line[1:23])
                print (line[46:52])
                print (line[41:44])
                u.write(line[1:23] + ' - ' + line[46:52] + '\n')
                estado = line[46:52]
                estado = estado.strip()
                id = line[41:44]
                id = id.strip()

                #logger.debug("if estado")

                jairo= str(line[1:6])
                administrator= str(line[1:14])

                if (jairo != 'jairo') and (administrator != 'Administrator'):
                    if estado == 'Disco':
                        os.system('logoff ' + id)
                        u.write('logoff em: ' + line[1:23] + ' - ' + 'logoff ' + id + '\n')
                    else:
                        if estado == 'Disc':
                            os.system('logoff ' + id)
                            u.write('logoff em: ' + line[1:23] + ' - ' + 'logoff ' + id + '\n')

    u.close
    f.close 

    print('hora: ' + str(hora))
    print('horaFim: ' + str(horaFim))
    print('sleep: ' + str(tempoSleep))

    sleep(int(tempoSleep)) 
    hora = tempo.strftime('%H%M%S', tempo.localtime())

    #logger.debug('hora: ' + str(hora) + ' - horaFim: ' + str(horaFim) + ' - sleep: ' + str(tempoSleep))

    if hora > horaFim:
        exit()