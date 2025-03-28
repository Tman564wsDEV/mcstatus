from . import Java

if Java("demo.mcstatus.io").getStatus():
    print(Java("demo.mcstatus.io").version.protocol())