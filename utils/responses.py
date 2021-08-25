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

    def ok_response(self, data, message='Ok'):
        return self.response(
            True,
            data,
            message,
            200
        )


if __name__ == '__main__':
    response = Responses()
    print(response.ok_response({'test': 21}))
