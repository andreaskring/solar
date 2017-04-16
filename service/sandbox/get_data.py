# NOTE: run this file from the commandline with
# $ cd /path/to/toplevel/solar
# $ python -i -m service.sandbox.get_data

from service.datacollector import DataCollector
import requests

URL = 'https://evishine.dk/data/json_data/17249/37392?now=%s'
DAILY_PRODUCTION_URL = 'https://evishine.dk/data/statistics_list/17249/37392?timestamp=%s'

collector = DataCollector()
client = requests.session()

# res = client.get(URL % collector.get_millis(2017, 4, 7, 12 , 0, 30))
res = client.get(DAILY_PRODUCTION_URL % collector.get_millis(2017, 4, 7, 12 , 0, 30))
print res.json()

