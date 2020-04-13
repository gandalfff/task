command1 = 'switchport trunk allowed vlan 1,2,3,5,8'
command2 = 'switchport trunk allowed vlan 1,3,8,9'


command1 = (command1.split()[-1]).split(',')
command2 = (command2.split()[-1]).split(',')

result = sorted(((set(command1))&(set(command2))))

print('Intersection option result: \n {}'.format(result))

