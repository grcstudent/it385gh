#!/usr/bin/python3
# Dictionary
# Key - Value pair
# Keys are unique, Values need not be

carListProperties = ['color', 'fuel', 'brand']
carListValues = ['red','gas','kia']

myCar = {
    'color':'red',
    'fuel':'gas',
    'brand':'kia',
    'color':'blue'
}
print(myCar.keys())
print(myCar.values())
myCar.update({'model':'mustang'})
print(myCar)

nameservers = {
    "ip":"10.1.1.10",
    'prefix': 24,
    'name':'mercury.example.com'
}

adapter = {
    "ipaddress": "",
    'prefix': 24,
    'defgateway': "",
    'dns':[nameservers]
}
'''
<adapter>
    <ipaddress>10.1.1.10</ipaddress>
    <prefix>24</prefix>
    <defgatway>10.10.1.1</defgatway>
    <dns>nameserver1</dns>
    <dns>nameserver2</dns>
    <dns>nameserver3</dns>
</adapter>
'''
