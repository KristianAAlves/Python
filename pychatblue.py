import simplepyble 

adapters = simplepyble.Adapter.get_adapters()
adapter_name = adapters[0]

if len(adapters) == 0:
    print("error 1")

adapter_name.scan_for(7000)
devices = adapter_name.scan_get_results()


for i, device in enumerate(devices):
    
    if not device.is_connectable():
        print(f"not possible to connect [{device.identifier()} {device.address()}]")
        adapter_name.scan_for(4000)
    if device.is_connectable():   
        print(f"{i}: {device.identifier()} : [{device.address()}] ")


print("select one")

choice = int(input("Enter choice "))
device = devices[choice]

if not device.connect():
    device.connect()

services = device.services()
services_charateristic = []

for service in services:
    for characteristic in service.characteristics():
        services_charateristic.append((service.uuid(), characteristic.uuid()))

for i, (service_uuid, characteristic) in enumerate(services_charateristic):
    print(f"{i}: {service_uuid} {characteristic}")




