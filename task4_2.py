mac = 'AAAA:BBBB:CCCC'


result_first  = '.'.join(mac.split(':'))

result_second = mac.replace(':','.')

print('My first verion result: \n \t{}'.format(result_first))

print('My second version result \n \t{}'.format(result_second))




