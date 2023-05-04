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


alarmes = opc.read(tags, group='Group_1', update=1)
opc.write(('FB_MDO.IN_D1.VALUE', 1))
time.sleep(1)
opc.write(('FB_MDO.IN_D1.VALUE', 0))
time.sleep(1)
