import json


class Responses:

    """Class used to create the responses that will be sent through the http protocol"""

    @staticmethod
    def response(data: dict):
        '''Create a ``json`` for http responses

        Parameters
        ----------
        data: dict
            The data that will be sent

        Returns
        -------
        response
            A json response
        '''
        return json.dumps({
            "data": {
                ** data
            }
        })


if __name__ == '__main__':
    response = Responses()
    print(response.ok_response({'test': 21}))
