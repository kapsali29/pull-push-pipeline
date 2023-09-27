import json

import requests


class OrionCB(object):
    def __init__(self,
                 orion_base_url,
                 ql_base_url
                 ):
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
                "entities": [
                    {
                        "idPattern": id_pattern
                    }
                ]
            },
            "notification": {
                "http": {
                    "url": f"{self.ql_base_url}"
                }
            }
        }
        return orion_cmd

    def create_subscription(
            self,
            sub_cmd
    ):
        data = json.dumps(sub_cmd)
        headers = {'Content-Type': 'application/json'}
        response = requests.post(
            url=f'{self.orion_base_url}/subscriptions/',
            data=data,
            headers=headers
        )
        return response
