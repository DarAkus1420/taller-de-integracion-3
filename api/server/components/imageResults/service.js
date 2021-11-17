import { createdResponse, errorResponse, okResponse } from '../../utils/responses';
import ImageResults from './model';

const imageResultsService = {
	async getAll() {
		const imageResults = await ImageResults.find({});
		return okResponse(`Obtanined ${imageResults.length} image results`, { imageResults });
	},

	async getOneById(id) {
		const foundedImageResults = await ImageResults.findById(id);
		return okResponse(`Obtained image result`, { foundedImageResults });
	},

	async createOne(body) {
		console.log(body, 'body');
		// const newImageResults = await ImageResults.create(imageResults);
		console.log('Creando nuevo registro');
		return createdResponse('Se ha ingresado correctamente el resultado de la imagen');
	},

	async updateOne(id, imageResults) {
		//TODO
		// const foundedImageResults = await ImageResults.updateOne({_id: id}, {$set: {}})
		return okResponse(`Image result update`);
	},

	async deleteOneById(id) {
		//TODO
		// return okResponse(`Image result with id ${id} deleted`);
		return okResponse('image deleted');
	},
};

export default imageResultsService;
