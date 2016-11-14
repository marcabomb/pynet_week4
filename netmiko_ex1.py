from netmiko import ConnectHandler
from getpass import getpass
password = getpass()

pynet_rtr1 = {
    'device_type': 'cisco_ios',
    'ip': '184.105.247.70',
    'username': 'pyclass',
    'password': password,
}
pynet_rtr2 = {
    'device_type': 'cisco_ios',
    'ip': '184.105.247.71',
    'username': 'pyclass',
    'password': password,
}
pynet_jnpr_srx1 = {
    'device_type': 'cisco_ios',
    'ip': '184.105.247.76',
    'username': 'pyclass',
    'password': password,
}

net_connect1 = ConnectHandler(**pynet_rtr1)

output = net_connect1.send_command('show ip int brief')
print output

device_list = [pynet_rtr1, pynet_rtr2, pynet_jnpr_srx1]

for i in device_list:
    net_connect2 = ConnectHandler(**i)
    output = net_connect2.send_command('show arp')
    print output

net_connect3 = ConnectHandler(**pynet_rtr2)
net_connect3.config_mode()

if net_connect3.check_config_mode() == True:
    print 'You are in configuration mode for {}'.format('pynet_rtr2')
    net_connect3.send_command('logging buffered 19999')
    net_connect3.exit_config_mode()

outp = net_connect3.send_command('show run | sec logging')
print outp

net_connect3.send_config_from_file(config_file='config_commands.txt')

outp = net_connect3.send_command('show run | sec log')
print outp
