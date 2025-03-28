from . import Java

server = Java("demo.mcstatus.io")
print(server.getResponse()["online"])