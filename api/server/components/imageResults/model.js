const mongoose = require('mongoose');
const { Model, Schema } = mongoose;

const particles = new Schema({
	contourX: { type: Number },
	contourY: { type: Number },
	radius: { type: Number },
});

const imageResultsSchema = new Schema(
	{
		blue_particles: { type: Array },
		red_particles: { type: Array },
		air_particles: { type: Array },
	},
	{ timestamps: true }
);

export default mongoose.model('ImageResults', imageResultsSchema);
