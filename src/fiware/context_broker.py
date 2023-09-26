import json

from fiware.http import Client


class OrionCB(Client):
    def __init__(self,
                 orion_base_url,
                 ql_base_url
                 ):
        super(OrionCB, self).__init__()
        self.orion_base_url = orion_base_url
        self.ql_base_url = ql_base_url

    def construct_ql_cmd(
            self,
            id_pattern,
            description="Notify QuantumLeap of changes to any entity"
    ):
        orion_cmd = {
            "description": description,
            "subject": {
                "entities": [{
                    "idPattern": id_pattern
                }]
            },
            "notification": {
                "http": {
                    "url": self.ql_base_url
                }
            }
        }
        return orion_cmd

    def create_subscription(
            self,
            sub_cmd
    ):
        data = json.dumps(sub_cmd)
        response = self.post(
            url=f'{self.orion_base_url}/subscriptions/',
            headers={
                'Content-Type': 'application/json',
                'Content-Length': str(len(data))
            },
            data=data
        )
        return response
