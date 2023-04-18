import pywintypes

import OpenOPC

import time



pywintypes.datetime = pywintypes.TimeType

opc = OpenOPC.client()

opc.connect('Smar.DfiOleServer.0', 'localhost')

tags = ['LT_1_AI.OUT.VALUE'] #lista ou tupla

while True:

    alarmes = opc.read(tags, group='Group_1', update=1)

    print(alarmes)

    time.sleep(1)
