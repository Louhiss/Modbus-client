from pyModbusTCP.client import ModbusClient

client = ModbusClient()

client.host = "127.0.0.1"
client.port = 12345
client.open()

if client.is_open:

    data = client.read_holding_registers(0, 7)
    if data:
        print("Pump registers 1-2 and Tank registers 3-5:", data)

    # Pumput 1 ja 2 = registerit 0 ja 1 eli kaksi enimmäistä
    result = client.write_multiple_registers(0, [125, 126])
    print("Write pump results in register:", result)
    # Tankit 1-5 = registerit 3-8
    result = client.write_multiple_registers(2, [60, 62, 46, 55, 53])
    print("Write Tank results in register:", result)
    client.close()
else:
    print("Could not connect to the Modbus server")