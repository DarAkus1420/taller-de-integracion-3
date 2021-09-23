import requests
from requests.api import request
from utils.responses import Responses


class Http:

    """Class used to send data to a specific server"""

    @staticmethod
    def send_to_server(url: str, data: dict) -> any:
        '''Send the data to a url using the request library

        Parameters
        ----------
        url: string
            The server url
        data: dict
            The data that will be sent to the server

        Returns
        -------
        response
            The server response
        '''

        formatted_data = Responses.response(data)
        response = requests.post(url, data=formatted_data)
        return response

    @staticmethod
    def send_data(url: str, data: dict, request_counter: int = 0) -> None:
        '''Execute the send_to_server, using a typical try/catch and
        recuersion to limit up to 3 request if it finds any errors 

        Parameters
        ----------
        url: string
            The server url
        data: dict
            The data that will be sent to the server
        request_counter: int
            The request counter to stop the recursivity function

        Returns
        -------
        None
        '''
        try:
            if(request_counter < 3):
                response = Http.send_to_server(url, data)
                print(response.status_code)
                if(response.status_code < 200 or response.status_code >= 300):
                    raise Exception('Request failed')
        except Exception as e:
            Http.send_data(url, data, request_counter + 1)
