import { restResponse } from '../../utils/responses';
import { errorCallback } from '../../utils/functions/errorCallback';
import imageResultsService from './service';

const imageResultsController = {
	async getAll(req, res) {
		try {
			const response = await imageResultsService.getAll();
			restResponse(response, res);
		} catch (e) {
			console.log(e);
			errorCallback(e, res);
		}
	},

	async getOneById(req, res) {
		try {
			const { id } = req.params;
			const response = await imageResultsService.getOneById(id);
			restResponse(response, res);
		} catch (e) {
			console.log(e);
			errorCallback(e, res);
		}
	},

	async createOne(req, res) {
		try {
			const response = await imageResultsService.createOne(req.body);
			restResponse(response, res);
		} catch (e) {
			console.log(e);
			errorCallback(e, res);
		}
	},

	async updateOne(req, res) {
		try {
			const { id } = req.params;
			const imageResults = req.body;
			const response = await imageResultsService.updateOne(id, imageResults);
			restResponse(response, res);
		} catch (e) {
			console.log(e);
			errorCallback(e, res);
		}
	},

	async deleteOneById(req, res) {
		try {
			const { id } = req.params;
			ponse = await imageResultsService.deleteOneById(id);
			restResponse(response, res);
		} catch (e) {
			console.log(e);
			errorCallback(e, res);
		}
	},
};

export default imageResultsController;
