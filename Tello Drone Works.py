import threading,socket,sys,time,platform
from time import sleep

commands=(
    'takeoff','land','forward 20','back 20','left 20',
    'right 20','up 20','down 20','cw 360','ccw 360',
    'flip l','flip r','flip f','flip b','flip lb',
    'flip rb','flip lf','flip rf','speed 20'
   )

host = ''
port = 9000
locaddr = (host,port)
address = ('192.168.10.1', 8889)
asci=('utf-8')
com=('command')

strap = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
strap.bind(locaddr)

strap.sendto(com.encode(encoding=asci),address)
sleep(5)

strap.sendto(commands[0].encode(encoding=asci),address)
sleep(3)

strap.sendto(commands[10].encode(encoding=asci),address)
sleep(3)

strap.sendto(commands[11].encode(encoding=asci),address)
sleep(3)

strap.sendto(commands[12].encode(encoding=asci),address)
sleep(3)

strap.sendto(commands[13].encode(encoding=asci),address)
sleep(3)

strap.sendto(commands[1].encode(encoding=asci),address)
strap.close()
