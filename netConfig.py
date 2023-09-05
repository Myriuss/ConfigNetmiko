from netmiko import ConnectHandler

sw1= {
    'device_type': 'cisco_ios',
    'ip': '192.168.129.11',
    'username': 'sw',
    'password': 'password',
}

sw2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.2.22',
    'username': 'sw',
    'password': 'password',
}

sw3 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.5.33',
    'username': 'sw',
    'password': 'password',
}

sw4 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.111.10',
    'username': 'sw',
    'password': 'password',
}
#f0/0
r5 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.111.2',
    'username': 'r5',
    'password': 'password',
}
#f0/0
r2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.129.22',
    'username': 'r2',
    'password': 'password',
}
#f1/0
r3 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.111.4',
    'username': 'r3',
    'password': 'password',
}
#f1/0
r1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.111.1',
    'username': 'r1',
    'password': 'passwo rd',
}


#with open('commands_file_switch') as f:
#    lines = f.read().splitlines()
#print (lines)




all_devices = [sw1, sw2, sw3, sw4]
for n, devices in enumerate(all_devices, start=1):
    with open('commands_sw'+str(n)) as f:
        lines = f.read().splitlines()
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print (output)


#with open('commands_file_switch') as f:
#    lines = f.read().splitlines()
#print (lines)

#la config du routeur5 est : commands_router4
#config router4: commands_router5

all_devices = [r1, r2, r3, r5]

for n, devices in enumerate(all_devices, start=1):
    with open('commands_router'+str(n)) as f:
        lines = f.read().splitlines()
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print (output)
