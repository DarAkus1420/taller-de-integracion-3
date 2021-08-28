import json


class Responses:

    """Class used to create the responses that will be sent through the http protocol"""

    @staticmethod
    def response(success: bool, data: dict, messages: str):
        '''Create a ``json`` for http responses

        Parameters
        ----------
        success: bool
            The status of the response
        data: dict
            The data that will be sent
        message: str
            The message to identify the status of the http response

        Returns
        -------
        response
            A json response
        '''
        return json.dumps({
            "data": {
                "success": success,
                "message": messages,
                ** data
            }
        })

    @staticmethod
    def ok_response(data, message='Ok'):
        return Responses.response(
            True,
            data,
            message,
        )


if __name__ == '__main__':
    response = Responses()
    print(response.ok_response({'test': 21}))
