import json
"""


    Parameters:

    ``success`` -- the status of the response.

    ``data`` -- the data that will be sent.

    ``message`` -- the message to identify the status of the http response.

    ``code`` -- the code of the http response.
    """


class Responses:

    """Class used to create the responses that will be sent through the http protocol"""

    def response(self, success: bool, data: dict, messages: str, code: int):
        '''Create a ``json`` for http responses

        Parameters
        ----------
        success: bool
            The status of the response
        data: dict
            The data that will be sent
        message: str
            The message to identify the status of the http response
        code: int
            The code of the http response

        Returns
        -------
        response
            A json response
        '''
        return json.dumps({
            "code": code,
            "data": {
                "success": success,
                "message": messages,
                ** data
            }
        })

    def bad_request(self, message='Bad request'):
        return self.response(
            False,
            {},
            message,
            400
        )

    def not_found(self, message='Not found'):
        return self.response(
            False,
            {},
            message,
            400
        )

    def created_response(self, data, message='Created'):
        return self.response(
            True,
            data,
            message,
            201
        )

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
