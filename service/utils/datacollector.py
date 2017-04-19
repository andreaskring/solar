import requests, datetime, time, psycopg2, random
random.seed()

PANEL_IDS = {1: 36976, 11: 37392}
CURRENT_PRODUCTION_URL = 'https://evishine.dk/data/json_data/17249/%s'


def parse_json(res):
    """
    Parse JSON response from HTTP GET request

    :param res: Response from HTTP GET request to evishine.dk for current data
    :type res: requests.models.Response
    :return: Status and current power (W)
    :type: Tuple of unicode, int

    """

    json = res.json()['currentData'][0]
    if u'status' in json.keys():
        return json['status'], json['currentData']
    else:
        return 'NORMAL', json['currentData']


def upload_to_database(timestamp, apartment, status, power):
    data = {'timestamp': timestamp, 'apartment_id': apartment, 'status': status, 'power': power}
    cursor.execute(
        """
        INSERT INTO monitor_panelstatus (timestamp, apartment_id, status, power)
        VALUES (%(timestamp)s, %(apartment_id)s, %(status)s, %(power)s);
        """,
        data)
    connection.commit()


# Establish DB connection
try:
    connection = psycopg2.connect("dbname='solar' user='solar' host='localhost' password='solar'")
    print 'Connected to DB...'
except:
    print "Could not connect to the DB"
cursor = connection.cursor()


# Setup HTTP client
client = requests.session()


try:
    while True:
        timestamp = datetime.datetime.now()
        res_ref = client.get(CURRENT_PRODUCTION_URL % PANEL_IDS[1])
        res = client.get(CURRENT_PRODUCTION_URL % PANEL_IDS[11])

        ref_status, ref_power = parse_json(res_ref)
        status, power = parse_json(res)
        print timestamp, '  Apartment 01: status = %s, power = %s' % (ref_status, ref_power)
        print timestamp, '  Apartment 11: status = %s, power = %s' % (status, power), '(delay =',

        if not 'ERROR' == ref_status:
            upload_to_database(timestamp, 1, ref_status, ref_power)
            upload_to_database(timestamp, 11, status, power)

        delay = random.randint(30, 90)
        print str(delay) + ' s)'
        time.sleep(delay)

except KeyboardInterrupt:
    print 'Closing connection'
    cursor.close()
    connection.close()
    print 'Connection closed'


