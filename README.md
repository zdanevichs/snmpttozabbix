# snmpttozabbix
Install dependencies:
pip3 install docopt ZabbixSender  
Add to config /etc/snmp/snmptrapd.conf  patch to script.
Example:
traphandle default /usr/sbin/snmpttozabbix
disableAuthorization yes