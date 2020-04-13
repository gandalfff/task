NAT = "ip nat inside source list ACL interface FastEthernet0/1 overload"

New_NAT = NAT.replace('Fast','Gigabit')

print('Old string: \n  {}'.format(NAT))


print('String with replaced piece: \n  {} '.format(New_NAT))
