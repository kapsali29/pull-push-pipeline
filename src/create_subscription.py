import settings
from fiware.context_broker import OrionCB

orion_cb = OrionCB(
    orion_base_url=f'http://{settings.ORION_EXT_HOST}:{settings.ORION_PORT}/v2',
    ql_base_url=f'http://{settings.QL_HOST}:{settings.QL_PORT}/v2/notify'
)

cmd = orion_cb.construct_ql_cmd(
    id_pattern=settings.QL_ID_PATTERN
)
response = orion_cb.create_subscription(cmd)
print(cmd)
print(vars(response))
