import { errorCallback } from '../../utils/functions/errorCallback';
import { restResponse } from '../../utils/responses';
import authService from './service';

const authController = {
	async register(req, res) {
		try {
			const { body } = req;
			const { data, code } = await authService.register(body.payload);
			restResponse(data, code, res);
		} catch (e) {
			errorCallback(e, res);
		}
	},
};

export default authController;
