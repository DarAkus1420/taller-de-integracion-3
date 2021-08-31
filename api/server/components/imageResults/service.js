import { createdResponse, errorResponse, okResponse } from '../../utils/responses';

const imageResultsService = {
	async getAll() {
		const imageResults = await ImageResults.findAll();
		return okResponse(`Obtanined ${imageResults.length} image results`, { imageResults });
	},

	async getOneById(id) {
		return okResponse(`Obtained image result`);
	},

	async updateOne(id, imageResults) {
		return okResponse(`Image result update`);
	},

	async deleteOneById(id) {
		return okResponse(`Image result with id ${id} deleted`);
	},
};

export default imageResultsService;
