from config import NAMES
from funcs import parse_names, parse_inst
from tor_connection import new_connection, get_tor_session

# new_connection()
# session = get_tor_session()
to_xlsx = parse_inst(NAMES, 'session')
print(to_xlsx)
