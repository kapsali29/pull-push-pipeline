import os

ORION_HOST = os.environ.get('ORION_HOST', 'orion')
ORION_EXT_HOST = os.environ.get('ORION_EXT_HOST', 'localhost')
ORION_PORT = os.environ.get('ORION_PORT', 1026)

QL_HOST = os.environ.get('QL_HOST', 'quantumleap')
QL_EXT_HOST = os.environ.get('QL_EXT_HOST', 'localhost')
QL_PORT = os.environ.get('QL_PORT', 8668)
QL_ID_PATTERN = ".*"
