import { port } from './config/dotenv';
const app = require('./app');

app.listen(port, () => {
	console.log(`Listen on port ${port}`);
});
