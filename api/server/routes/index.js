import imageResultRouter from '../components/imageResult/routes';

const apiVersion = '/api/v1';

export default app => {
	app.use(apiVersion, imageResultRouter);
};
