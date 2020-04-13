NAT = "ip nat inside source list ACL interface FastEthernet0/1 overload"
template = 'Gigabit'
 
result  = NAT[:NAT.find('Fast')]+template+NAT[NAT.find('Fast')+len('Fast'):]

print('Result my job is: \n {}'.format(result))
   
