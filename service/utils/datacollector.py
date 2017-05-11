import requests, datetime, time, psycopg2, random
import evishine_html_parser
random.seed()

parser = evishine_html_parser.EvishineHTMLParser()

PANEL_IDS = parser.get_panel_ids()
CURRENT_PRODUCTION_URL = 'https://evishine.dk/data/json_data/17249/%s'


def parse_json(res):
    """
    Parse JSON response from HTTP GET request

    :param res: Response from HTTP GET request to evishine.dk for current data
    :type res: requests.models.Response
    :return: Status and current power (W)
    :type: Tuple of unicode, int

    """

    try:
        json = res.json()['currentData'][0]
    except:
        return 'NO DATA', None

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
        delay = random.randint(30, 90)
        # res_ref = client.get(CURRENT_PRODUCTION_URL % PANEL_IDS[1])
        # res = client.get(CURRENT_PRODUCTION_URL % PANEL_IDS[11])

        ref_status = 'ERROR'
        for apartment, panel_id in PANEL_IDS:
            r = client.get(CURRENT_PRODUCTION_URL % panel_id)
            if r.status_code == 200:
                status, power = parse_json(r)
                if apartment == 1:
                    ref_status = status
                print timestamp, '  Apartment %s: status = %s, power = %s' % (apartment, status, power)

                if not 'ERROR' == ref_status:
                    upload_to_database(timestamp, apartment, status, power)

                print str(delay) + ' s)'
            else:
                print timestamp, r.status_code
        time.sleep(delay)

except KeyboardInterrupt:
    print 'Closing connection'
    cursor.close()
    connection.close()
    print 'Connection closed'


