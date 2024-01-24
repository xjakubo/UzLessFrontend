import requests
import json


class Backend_Request:
    @classmethod
    def loadConfig(cls) -> dict:
        with open("cfg.ini", "r") as file:
            content = file.read()
            config_vars = json.loads(content)
            return config_vars

    @classmethod
    def tryToConnectToEndpoint(cls, full_url):
        pass

    @classmethod
    def concatDataFromOtherTable(
        cls,
        rows_to_replace: dict,
        id_column_to_replace: str,
        fk_column_to_replace: str,
        data_endpoint: str,
    ):
        replaced_rows = rows_to_replace.copy()
        fk_entities_id = cls.getDataFromEndpoint(data_endpoint)
        for row in replaced_rows:
            id_to_search = row[id_column_to_replace]
            for fk_row in fk_entities_id:
                if id_to_search == fk_row[id_column_to_replace]:
                    row[id_column_to_replace] = fk_row[fk_column_to_replace]
        return replaced_rows

    @classmethod
    def getDataFromEndpoint(cls, endpoint: str):
        url = cls.loadConfig()["url"]
        full_url = f"{url}/{endpoint}"
        response = requests.get(full_url)
        return cls.getEntitiesList(response=response)

    @classmethod
    def postDataToEndpoint(cls, endpoint: str, data_to_send: dict):
        url = cls.loadConfig()["url"]
        full_url = f"{url}/{endpoint}"
        json_data_to_send = json.dumps(data_to_send)
        headers_to_send = {
            "Content-Type": "application/json",
        }
        response = requests.post(
            full_url, headers=headers_to_send, data=json_data_to_send
        )
        return cls.getEntitiesList(response=response)

    @classmethod
    def getEntitiesList(cls, response: requests.Response):
        if response.status_code != 200:
            return {"error": "error getting entities"}
        json_response = response.json()
        return json_response
