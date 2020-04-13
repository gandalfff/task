ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
pr,ip,met,trash,next,tim,inter = ospf_route.split()

print(pr,ip,met,next,tim,inter)

template = f'''Protocol :{pr:50}\n
Prefix :{ip:50}\n
AD/Metric :{met:50}\n
Next-Hop :{next:50}\n
Last update :{tim:50}\n
Outbound Interface :{inter:50}'''

print(template)

 


