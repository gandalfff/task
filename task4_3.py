config = 'switchport trunk allowed vlan 1,3,10,20,30,100'

result_f = (config.split()[-1]).split(',')

print ('My first version result: \n \t{}'.format(result_f))


