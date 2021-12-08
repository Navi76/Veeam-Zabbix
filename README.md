# Veeam-Zabbix
Veeam Template for Zabbix using Veeam BR API

Very Basic Zabbix Template to monitor Veeam Backup and Replication V. 11 Jobs


Instalation:
You need Python V.3 installed on Zabbix Server
Includyn json, request and pyzabbix libraries


Modify the pyton script to match credentials (They are identified as #Data from Zabbix and #Data from Veeam
Use crontab to shedule the script to execute periodically.

Import Template to Zabbix
Assign template host form veeam Server
