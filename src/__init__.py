import requests

MCSTATUS_JAVA = "https://api.mcstatus.io/v2/status/java"
MCSTATUS_BEDROCK = "https://api.mcstatus.io/v2/status/bedrock"


class Java:
    def __init__(self, server: str, query: bool = False):
        self.server = server
        self.query = query

        self.version = self.Version(self)

    def getResponse(self) -> dict:
        FULL_ENDPOINT = f"{MCSTATUS_JAVA}/{self.server}"
        response = requests.get(FULL_ENDPOINT, params={"query": self.query}).json() # TODO: Add someway to check if returns nothing, then stop everything
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

        def nameRaw(self) -> str:
            nameraw = Java(self.outer.server).getResponse()["version"]["name_raw"]
            return nameraw
        
        def nameClean(self) -> str:
            nameclean = Java(self.outer.server).getResponse()["version"]["name_clean"]
            return nameclean
        
        def nameHtml(self) -> str:
            namehtml = Java(self.outer.server).getResponse()["version"]["name_html"]
            return namehtml
        
        def protocol(self) -> str:
            protocol = Java(self.outer.server).getResponse()["version"]["protocol"]
            return protocol
    
