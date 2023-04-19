import pywintypes

import OpenOPC

import time



pywintypes.datetime = pywintypes.TimeType

opc = OpenOPC.client()

opc.connect('Smar.DfiOleServer.0', 'localhost')

tags = ['LT_1_AI.OUT.VALUE','FB_MDI.OUT_D3.VALUE'] #lista ou tupla

while True:

    alarmes = opc.read(tags, group='Group_1', update=1)

    #print(alarmes)
    #print(type(alarmes))
    #print(alarmes[0][1])
    #print(alarmes[1])
    print(f'nível: {alarmes[0][1]:.2f}')
    print(f'chave: {alarmes[1][1]}')

    time.sleep(1)
