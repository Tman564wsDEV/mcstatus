import requests

MCSTATUS_JAVA = "https://api.mcstatus.io/v2/status/java"
MCSTATUS_BEDROCK = "https://api.mcstatus.io/v2/status/bedrock"

class Java():
    def __init__(self, server: str, query: bool=False):
        self.server = server
        self.query = query
    
    def getResponse(self) -> dict:
        FULL_ENDPOINT = f"{MCSTATUS_JAVA}/{self.server}"
        response = requests.get(FULL_ENDPOINT, params={"query": self.query}).json()
        return response

