import { restResponse } from '../../utils/responses';
import { errorCallback } from '../../utils/functions/errorCallback';
import userService from './service';

const userController = {
	async getOneById(req, res) {
		try {
			const { id } = req.params;
			const response = await userService.getOneById(id);
			restResponse(response, res);
		} catch (e) {
			console.log(e);
			errorCallback(e, res);
		}
	},

	async createOne(req, res) {
		try {
			const user = req.body;
			const response = await userService.createOne(user);
			restResponse(response, res);
		} catch (e) {
			console.log(e);
			errorCallback(e, res);
		}
	},

	async updateOne(req, res) {
		try {
			const { id } = req.params;
			const user = req.body;
			const response = await userService.updateOne(id, user);
			restResponse(response, res);
		} catch (e) {
			console.log(e);
			errorCallback(e, res);
		}
	},

	async deleteOneById(req, res) {
		try {
			const { id } = req.params;
			ponse = await userService.deleteOneById(id);
			restResponse(response, res);
		} catch (e) {
			console.log(e);
			errorCallback(e, res);
		}
	},
};

export default userController;
