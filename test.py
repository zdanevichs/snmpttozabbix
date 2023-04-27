# from ZabbixSender import ZabbixSender, ZabbixPacket
from pyzabbix import ZabbixMetric, ZabbixSender

zabbix = ZabbixSender('10.77.0.7', 10051)
packet = []
packet.append(ZabbixMetric('10.77.7.5', 'zeroDotZero.0.0.1', 1)) 
print(zabbix.__dict__)
print(packet)
zabbix.send(packet)
print(zabbix.__dict__)