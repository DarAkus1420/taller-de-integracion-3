import { createdResponse, errorResponse, okResponse } from '../../utils/responses';
import ImageResults from './model';
import replaceAll from '../../utils/functions/replaceAll';
import { errorCallback } from '../../utils/functions/errorCallback';
import * as csv from 'fast-csv';

const imageResultsService = {
	async getAll() {
		const imageResults = await ImageResults.find({});
		return okResponse(`Obtanined ${imageResults.length} image results`, { imageResults });
	},

	async getOneById(id) {
		const foundedImageResults = await ImageResults.findById(id);
		return okResponse(`Obtained image result`, { foundedImageResults });
	},

	async createOne(data) {
		console.log(data, 'data');
		const imageResults = JSON.parse(replaceAll("'", '"', data));
		console.log(imageResults, 'imageres');
		ImageResults.create(imageResults);
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

	async generateCsv(res) {
		try {
			const imageResults = await ImageResults.find({});
			let images = [];
			imageResults.forEach(result => {
				if (result.blue_particles.length > 0) {
					result.blue_particles.forEach(blue => {
						images.push({ data: blue, color: 'blue', date: result.createdAt });
					});
				}
				if (result.red_particles.length > 0) {
					result.red_particles.forEach(red => {
						images.push({ data: red, color: 'red', date: result.createdAt });
					});
				}
				if (result.air_particles.length > 0) {
					result.air_particles.forEach(air => {
						images.push({ data: air, color: 'gray', date: result.createdAt });
					});
				}
			});
			const file = await csv.write(images, {
				headers: true,
				transform: function (row) {
					return {
						cX: row.data[0],
						cY: row.data[1],
						radius: row.data[2],
						color: row.color,
						date: row.date,
					};
				},
			});
			res.attachment('data.csv');
			file.pipe(res);
		} catch (e) {
			errorCallback(e, res, 'Error generando reporte csv');
		}
	},
};

export default imageResultsService;
