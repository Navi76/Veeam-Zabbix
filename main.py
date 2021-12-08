import requests
import json
from pyzabbix import ZabbixMetric, ZabbixSender

#Change this data by your own
#Data from veeam
veeamip="192.168.83.25"
veeamapiport="9419" #Default is 9419
username='Administrator'
password="Re123456"
#Data from zabbix
hostname="VeeamServer" #Host Name as registered in zabbix
itemkey="veeam.get.data"  #Do NOT change

if __name__=='__main__':

   urlaut = 'https://'+veeamip+':'+veeamapiport+'/api/oauth2/token'
   urlget = 'https://'+veeamip+':'+veeamapiport+'/api/v1/jobs/states'
   urlout = 'https://'+veeamip+':'+veeamapiport+'/api/oauth2/logout'
# Aunthenticating
   header1 = { 'accept':'application/json', 'x-api-version': '1.0-rev1', 'Content-Type': 'application/x-www-form-urlencoded' }
   data1 = {'code': '','grant_type': 'password', 'password': password, 'username': username }
#   header2 = { 'accept':'application/json', 'x-api-version': '1.0-rev1'}

   aut_response = requests.post(urlaut, headers=header1, data=data1, verify=False)

   if aut_response.status_code == 200:
        content1 = json.loads(aut_response.content)
        token = content1['access_token']
#Getting data
   header1['Authorization'] = 'Bearer ' + token

   get_response = requests.get(urlget, headers=header1, verify=False)
  
#   print (get_response.status_code)
   if get_response.status_code == 200:
       jobstatus = json.loads(get_response.content)
       tjobstatus = json.dumps(jobstatus["data"])
#       print (tjobstatus)
       metricas=[ZabbixMetric(hostname, itemkey, tjobstatus)]
       ZabbixSender(use_config=True).send(metricas)


# Logout
   
#   print(header1)
   data2={}
   out_response = requests.post(urlout, headers=header1, data=data2, verify=False)
   if out_response.status_code == 200:
       print('Logout OK')
