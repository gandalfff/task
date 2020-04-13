ip = '192.168.3.1'

de =  ip.split('.')

print ('''\n{0:<10}{1:<10}{2:<10}{3:<10}\n
{0:08b}{1:08b}{2:08b}{3:08b}'''.format(int(de[0]),int(de[1]),int(de[2]),int(de[3])))
