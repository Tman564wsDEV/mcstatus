import requests
import base64
from typing import Optional

MCSTATUS_JAVA = "https://api.mcstatus.io/v2/status/java"
MCSTATUS_BEDROCK = "https://api.mcstatus.io/v2/status/bedrock"


class Java:
    def __init__(self, server: str, query: bool = False):
        self.server = server
        self.query = query

        self.version = self.Version(self)
        self.players = self.Players(self)
        self.motd = self.MOTD(self)

    def getResponse(self) -> dict:
        FULL_ENDPOINT = f"{MCSTATUS_JAVA}/{self.server}"
        response = requests.get(
            FULL_ENDPOINT, params={"query": self.query}
        ).json()  # TODO: Add someway to check if returns nothing, then stop everything
        return response

    def getStatus(self) -> bool:
        online = Java(self.server).getResponse()["online"]
        return online

    def getHost(self) -> str:
        host = Java(self.server).getResponse()["host"]
        return host

    def getIP(self) -> str:
        ip = Java(self.server).getResponse()["ip_address"]
        return ip

    def getEulaBlocked(self) -> bool:
        eulablocked = Java(self.server).getResponse()["eula_blocked"]
        return eulablocked

    class Version:
        def __init__(self, outer):
            self.outer = outer

        def getNameRaw(self) -> str:
            nameraw = Java(self.outer.server).getResponse()["version"]["name_raw"]
            return nameraw

        def getNameClean(self) -> str:
            nameclean = Java(self.outer.server).getResponse()["version"]["name_clean"]
            return nameclean

        def getNameHtml(self) -> str:
            namehtml = Java(self.outer.server).getResponse()["version"]["name_html"]
            return namehtml

        def getProtocol(self) -> str:
            protocol = Java(self.outer.server).getResponse()["version"]["protocol"]
            return protocol

    class Players:
        def __init__(self, outer):
            self.outer = outer

        def getOnline(self) -> dict:
            online = Java(self.outer.server).getResponse()["players"]["online"]
            return online

        def getMax(self) -> int:
            max = Java(self.outer.server).getResponse()["players"]["max"]
            return max

        def getPlayers(self) -> list:
            players = Java(self.outer.server).getResponse()["players"]["list"]
            return players

    class MOTD:
        def __init__(self, outer):
            self.outer = outer

        def getRaw(self) -> str:
            raw = Java(self.outer.server).getResponse()["motd"]["raw"]
            return raw

        def getClean(self) -> str:
            clean = Java(self.outer.server).getResponse()["motd"]["clean"]
            return clean

        def getHtml(self) -> str:
            html = Java(self.outer.server).getResponse()["motd"]["html"]
            return html

    def getIcon(self) -> Optional[bytes]:
        iconRaw = Java(self.server).getResponse()["icon"]
        if not iconRaw: return None
        iconData = base64.b64decode(str(iconRaw).split(",", 1)[1])
        return iconData

    def getIconRaw(self) -> str:
        iconRaw = Java(self.server).getResponse()["icon"]
        return iconRaw

    # TODO: getMods may return empty list if the server is not forge, or no mods or if query was not turned on
    def getMods(self) -> list:
        mods = Java(self.server).getResponse()["mods"]
        return mods

    # TODO: getSoftware may return None if query was not turned on
    def getSoftware(self) -> str:
        software = Java(self.server).getResponse()["software"]

    # TODO: getPlugins may return an empty list if no plugins on server
    def getPlugins(self) -> list:
        plugins = Java(self.server).getResponse()["plugins"]
        return plugins

    # TODO: getSrvHost may return None if no srv record could be found
    def getSrvHost(self) -> Optional[str]:
        srv = Java(self.server).getResponse()["srv_record"]
        if not srv: return None
        host = srv["host"]
        return host

    # TODO: getSrvPort may return None if no srv record could be found
    def getSrvPort(self) -> Optional[int]:
        srv = Java(self.server).getResponse()["srv_record"]
        if not srv: return None
        port = srv["port"]
        return port
