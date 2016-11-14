import paramiko, time


pynet_rtr2 = paramiko.SSHClient()
pynet_rtr2.set_missing_host_key_policy(paramiko.AutoAddPolicy())
pynet_rtr2.connect('184.105.247.71', username='pyclass', password='88newclass')

pynet_rtr2_shell = pynet_rtr2.invoke_shell()
pynet_rtr2_shell.send('config t\n')
time.sleep(.5)
pynet_rtr2_shell.send('logging buffered 19999\n')
time.sleep(.5)
pynet_rtr2_shell.send('end\n')
time.sleep(.5)
pynet_rtr2_shell.send('sh run | i logging\n')
time.sleep(.5)
output = pynet_rtr2_shell.recv(6000)
print output

