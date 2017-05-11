import HTMLParser
import requests


class EvishineHTMLParser(HTMLParser.HTMLParser):
    """Get the panel IDs for Skovfyrvej"""

    def __init__(self):
        HTMLParser.HTMLParser.__init__(self)
        self.current_tag = None
        self.current_attrs = None
        self.panel_ids = []

    def handle_starttag(self, tag, attrs):
        self.current_tag = tag
        self.current_attrs = attrs

    def handle_data(self, data):
        if self.current_tag == 'a':
            if data[:10] == 'Skovfyrvej' and not 'Nedlagt' in data:
                self.panel_ids.append(self.current_attrs[0][1].split('&')[0].split('id=')[1])

    def handle_endtag(self, tag):
        pass

    def _get_raw_HTML(self):
        client = requests.Session()
        r = client.get('http://evishine.dk/17249?id=17329')
        if r.status_code == 200:
            self.raw_data = r.text
        else:
            raise 'Error connecting to evishine!'
        client.close()

    def get_panel_ids(self):
        self._get_raw_HTML()
        self.feed(self.raw_data)
        return self.panel_ids

if __name__ == '__main__':
    parser = EvishineHTMLParser()
    l = parser.get_panel_ids()
