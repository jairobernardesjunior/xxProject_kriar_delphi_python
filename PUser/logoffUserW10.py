import csv
import os
#os.system('query user')

pipe = os.popen('query user')
tabela = pipe.read()

with open('tabelaUser.txt', 'w') as w:
    w.write(tabela)

w.close

with open('Usuarios.txt', 'w') as u:
    with open ('tabelaUser.txt', 'r') as f:
        for line in f:
            print (line[1:23])
            print (line[46:52])
            print (line[41:44])
            u.write(line[1:23] + ' - ' + line[46:52] + '\n')
            estado = line[46:52]
            estado = estado.strip()
            id = line[41:44]
            id = id.strip()

            if estado == 'Disco':
                os.system('logoff ' + id)
                u.write('logoff em: ' + line[1:23] + ' - ' + 'logoff ' + id + '\n')
            else:
                if estado == 'Disc':
                    os.system('logoff ' + id)
                    u.write('logoff em: ' + line[1:23] + ' - ' + 'logoff ' + id + '\n')

u.close
f.close            