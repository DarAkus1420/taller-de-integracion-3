export const restResponse = (response, res) => res.status(response.code).json(response);

export const badRequestResponse = message => ({
	success: false,
	data: {
		message,
	},
	messages: 'bad request',
	code: 400,
});

export const notFoundResponse = message => ({
	success: false,
	data: {
		message,
	},
	messages: 'resource not found',
	code: 404,
});

export const okResponse = (message, data) => ({
	success: true,
	data: {
		message,
		...data,
	},
	messages: 'ok response',
	code: 200,
});

export const createdResponse = (message, data) => ({
	success: true,
	data: {
		message,
		...data,
	},
	messages: 'created response',
	code: 201,
});

export const noContentResponse = (message, data) => ({
	success: true,
	data: {
		message,
		...data,
	},
	messages: 'no content response',
	code: 204,
});

export const conflictResponse = message => ({
	success: false,
	data: {
		message,
	},
	messages: 'conflict response',
	code: 409,
});

export const errorResponse = message => ({
	success: false,
	data: { message },
	messages: 'error response',
	code: 400,
});
