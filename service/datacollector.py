import datetime
import requests


class DataCollector(object):

    URL = 'https://evishine.dk/data/json_data/17249/37392?now=1491641575180'

    @staticmethod
    def get_millis(year, month, day, hour, minute, second):
        """
        Convert date and time to milliseconds
            
        :param year: 
        :param month: 
        :param day: 
        :param hour: 
        :param minute: 
        :param second: 
        :return: 
        """

        return datetime.datetime(year, month, day, hour, minute, second).strftime('%s') + '000'


    def get_panel_status(self, apartment_number):
        """
        Get the panel status from evishine.dk
        
        :param apartment_number: the apartment number to get the status from
        :type apartment_number: int
        :return: 
        """

