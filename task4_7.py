mac = 'AAAA:BBBB:CCCC'


mac_l = mac.split(':')
number = []
number.append(int(mac_l.pop(),16))
number.append(int(mac_l.pop(),16))
number.append(int(mac_l.pop(),16))

number[0]=bin(number[0])
number[1]=bin(number[1])
number[2]=bin(number[2])

print(''.join(number))

