import requests
import base64
from typing import Optional

MCSTATUS_JAVA = "https://api.mcstatus.io/v2/status/java"
MCSTATUS_BEDROCK = "https://api.mcstatus.io/v2/status/bedrock"


class Java:
    def __init__(self, server: str, query: bool = False):
        self.server = server
        self.query = query

        self.version = self.__Version__(self)
        self.players = self.__Players__(self)
        self.motd = self.__MOTD__(self)

        FULL_ENDPOINT = f"{MCSTATUS_JAVA}/{self.server}"
        self.info = requests.get(FULL_ENDPOINT, params={"query": self.query}).json()

    def getResponse(self) -> dict:
        FULL_ENDPOINT = f"{MCSTATUS_JAVA}/{self.server}"
        self.info = requests.get(
            FULL_ENDPOINT, params={"query": self.query}
        ).json()  # TODO: Add someway to check if returns nothing, then stop everything
        return self.info

    def getStatus(self) -> bool:
        online = self.info["online"]
        return online

    def getHost(self) -> str:
        host = self.info["host"]
        return host

    def getIP(self) -> str:
        ip = self.info["ip_address"]
        return ip

    def getEulaBlocked(self) -> bool:
        eulablocked = self.info["eula_blocked"]
        return eulablocked

    class __Version__:
        def __init__(self, outer):
            self.outer = outer

        def getNameRaw(self) -> str:
            nameraw = self.outer.info["version"]["name_raw"]
            return nameraw

        def getNameClean(self) -> str:
            nameclean = self.outer.info["version"]["name_clean"]
            return nameclean

        def getNameHtml(self) -> str:
            namehtml = self.outer.info["version"]["name_html"]
            return namehtml

        def getProtocol(self) -> str:
            protocol = self.outer.info["version"]["protocol"]
            return protocol

    class __Players__:
        def __init__(self, outer):
            self.outer = outer

        def getOnline(self) -> dict:
            online = self.outer.info["players"]["online"]
            return online

        def getMax(self) -> int:
            max = self.outer.info["players"]["max"]
            return max

        def getPlayers(self) -> list:
            players = self.outer.info["players"]["list"]
            return players

    class __MOTD__:
        def __init__(self, outer):
            self.outer = outer

        def getRaw(self) -> str:
            raw = self.outer.info["motd"]["raw"]
            return raw

        def getClean(self) -> str:
            clean = self.outer.info["motd"]["clean"]
            return clean

        def getHtml(self) -> str:
            html = self.outer.info["motd"]["html"]
            return html

    def getIcon(self) -> Optional[bytes]:
        iconRaw = self.info["icon"]
        if not iconRaw: return None
        iconData = base64.b64decode(str(iconRaw).split(",", 1)[1])
        return iconData

    def getIconRaw(self) -> str:
        iconRaw = self.info["icon"]
        return iconRaw

    # TODO: getMods may return empty list if the server is not forge, or no mods or if query was not turned on
    def getMods(self) -> list:
        mods = self.info["mods"]
        return mods

    # TODO: getSoftware may return None if query was not turned on
    def getSoftware(self) -> str:
        software = self.info["software"]

    # TODO: getPlugins may return an empty list if no plugins on server
    def getPlugins(self) -> list:
        plugins = self.info["plugins"]
        return plugins

    # TODO: getSrvHost may return None if no srv record could be found
    def getSrvHost(self) -> Optional[str]:
        srv = self.info["srv_record"]
        if not srv: return None
        host = srv["host"]
        return host

    # TODO: getSrvPort may return None if no srv record could be found
    def getSrvPort(self) -> Optional[int]:
        srv = self.info["srv_record"]
        if not srv: return None
        port = srv["port"]
        return port
