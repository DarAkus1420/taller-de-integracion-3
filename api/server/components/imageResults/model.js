const mongoose = require('mongoose');
const { Model, Schema } = mongoose;

const particles = new Schema({
	contourX: { type: Number },
	contourY: { type: Number },
	radius: { type: Number },
});

const imageResultsSchema = new Schema(
	{
		blueParticles: [particles],
		redParticles: [particles],
		airParticles: [particles],
	},
	{ timestamps: true }
);

export default mongoose.model('ImageResults', imageResultsSchema);
