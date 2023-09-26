# ACES Perception Component
## Installation

### Docker & docker-compose

+ `cd /config/compose`
+ `docker-compose up -d`

#### Create Orion Subscription
The link between Orion and QuantumLeap is established through a subscription you need to create. In order to do so execute the following
curl command. After the execution of this step every data inserted to Orion CB will be recorded to CrateDB.

```shell
curl --location 'http://localhost:1026/v2/subscriptions/' \
--header 'Content-Type: application/json' \
--data '{  "description": "Notify QuantumLeap of changes to any entity.",
    "subject": {
        "entities": [
            {
                "idPattern": ".*"
            }
        ]
    },
    "notification": {
        "http": {
            "url": "http://quantumleap:8668/v2/notify"
        }
    }
}'
```
The table bellow includes base URL of the involved components

| Component Name |            Base URL            | 
|----------------|:------------------------------:|
| ORION CB       |  [orion-cb / localhost]:1026   |
| Quantumleap    | [quantumleap / localhost]:8668 |
| CRATEDB        |  [crate-db / localhost]:4200   |