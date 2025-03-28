from . import Java
java = Java("demo.mcstatus.io")
if java.getStatus():
    print(java.getStatus())
    print(java.getHost())
    print(java.getPort())
    print(java.getIP())
    print(java.getEulaBlocked())
    print(java.getUnixRetrievedAt())
    print(java.getUnixExpiresAt())
    print(java.version.getNameRaw())
    print(java.version.getNameClean())
    print(java.version.getNameHtml())
    print(java.version.getProtocol())
    print(java.players.getOnline())
    print(java.players.getMax())
    print(java.players.getPlayers())
    print(java.motd.getRaw())
    print(java.motd.getClean())
    print(java.motd.getHtml())
    print(java.getIcon())
    print(java.getIconRaw())
    print(java.getMods())
    print(java.getSoftware())
    print(java.getPlugins())
    print(java.getSrvHost())
    print(java.getSrvPort())