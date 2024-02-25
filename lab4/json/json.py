import json

with open('sample-data.json') as f:
    data = json.load(f)

interfaces = data['imdata']

print("Interface Status")
print("=" * 80)
print("{:<50} {:<20} {:<8} {:<6}".format("DN", "Description", "Speed", "MTU"))
print("-" * 80)

for interface in interfaces:
    dn = interface['l1PhysIf']['attributes']['dn']
    description = interface['l1PhysIf']['attributes'].get('descr', '')
    speed = interface['l1PhysIf']['attributes'].get('speed', 'inherit')
    mtu = interface['l1PhysIf']['attributes'].get('mtu', '')

    print("{:<50} {:<20} {:<8} {:<6}".format(dn, description, speed, mtu))