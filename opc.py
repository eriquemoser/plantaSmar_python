import pywintypes
import OpenOPC
import time

pywintypes.datetime = pywintypes.TimeType
opc = OpenOPC.client()
opc.connect('Smar.DfiOleServer.0', 'localhost')
tags = ['FB_MDI.OUT_D1.VALUE','FB_MDI.OUT_D2.VALUE','FB_MDI.OUT_D3.VALUE','FB_MDI.OUT_D4.VALUE',
        'FB_MDI.OUT_D5.VALUE','FB_MDI.OUT_D6.VALUE','FB_MDI.OUT_D7.VALUE','FB_MDI.OUT_D8.VALUE',

        'FFB_MDI.OUT_D1.VALUE','FFB_MDI.OUT_D2.VALUE','FFB_MDI.OUT_D3.VALUE','FFB_MDI.OUT_D4.VALUE',
        'FFB_MDI.OUT_D5.VALUE','FFB_MDI.OUT_D6.VALUE','FFB_MDI.OUT_D7.VALUE','FFB_MDI.OUT_D8.VALUE',

        'FFFB_MDI.OUT_D1.VALUE','FFFB_MDI.OUT_D2.VALUE'
        ] #lista ou tupla

#INICIALIZAÇÃO
cont = 0
init = []
nomes= ['$$$$', 'c_d_lo', 'chave2', 'c_d_hi', 'c_d_sp', 'c_u_hi', 'c_u_hi_hi', 'c_u_lo', 'c_u_sp',
        'c_underflow', 'c_overflow', 'start', 'stop', 'bligada', 'bdesligada', 'vfecha', 'vabre',
        'vregula']

#CAPTURA OS ESTADOS INICIAIS
alarmes = opc.read(tags, group='Group_1', update=1)
for c in range(0,len(alarmes)):
    init.append(alarmes[c][1])
print(init)

#CAPTURA DOS DADOS
while True:
    alarmes = opc.read(tags, group='Group_1', update=1)
    for c in range(0, len(alarmes)):
        if alarmes[c][1] != init[c]:
            print(nomes[c])
            #print(alarmes[c][0])
            init[c]=alarmes[c][1]

    print(f'{cont} -------------------------------')
    cont+=1


time.sleep(0.1)
