import { errorResponse } from '../responses';

export const errorCallback = (err, res, description) => {
	if (err.code === 'uniqueValidation') return res.status(409).json({ message: err.message });
	console.log(err);
	if (description) {
		err.description = description;
	}
	errorResponse(err, res);
};
