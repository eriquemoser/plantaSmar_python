import pywintypes
import OpenOPC
import time

#CONEXÃO OPC
pywintypes.datetime = pywintypes.TimeType
opc = OpenOPC.client()
opc.connect('Smar.DfiOleServer.0', 'localhost')
tags = ['FB_MDI.OUT_D1.VALUE','FB_MDI.OUT_D2.VALUE','FB_MDI.OUT_D3.VALUE','FB_MDI.OUT_D4.VALUE',
        'FB_MDI.OUT_D5.VALUE','FB_MDI.OUT_D6.VALUE','FB_MDI.OUT_D7.VALUE','FB_MDI.OUT_D8.VALUE',

        'FFB_MDI.OUT_D1.VALUE','FFB_MDI.OUT_D2.VALUE','FFB_MDI.OUT_D3.VALUE','FFB_MDI.OUT_D4.VALUE',
        'FFB_MDI.OUT_D5.VALUE','FFB_MDI.OUT_D6.VALUE','FFB_MDI.OUT_D7.VALUE','FFB_MDI.OUT_D8.VALUE',

        'FFFB_MDI.OUT_D1.VALUE','FFFB_MDI.OUT_D2.VALUE'
        ] #lista ou tupla

#DECLARAÇÃO VARIAVEIS
cont = 0
init = []
pos = []
nomes= ['$$$$', 'd_lo', 'd_lo_lo', 'd_hi', 'd_sp', 'u_hi', 'u_hi_hi', 'u_lo', 'u_sp',
        'underflow', 'overflow', 'start', 'stop', 'bomba_liga', 'bomba_deslg', 'vfecha', 'vabre',
        'vregula']

#CAPTURA OS ESTADOS INICIAIS
alarmes = opc.read(tags, group='Group_1', update=1)
#print(alarmes)
for c in range(0,len(alarmes)):
    init.append(alarmes[c][1])
print(init)

#CAPTURA DOS DADOS
while True:

    alarmes = opc.read(tags, group='Group_1', update=1)
    time.sleep(0.1)
    for c in range(1, len(alarmes)):
        if alarmes[c][1] != init[c]:
            print(nomes[c])
            #print(alarmes[c][0])
            init[c]=alarmes[c][1]
            #print(init)
    opc.write(('FB_MDO.IN_D1.VALUE', 1))
    #time.sleep(0.5)
    opc.write(('FB_MDO.IN_D1.VALUE', 0))
    #time.sleep(1)

    #print(f'{cont} -------------------------------')
    #print(cont, '.')
    cont+=1


#time.sleep(0.1)
