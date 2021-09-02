import imageResultsRouter from '../components/imageResults/routes';

const apiVersion = '/api/v1';

export default app => {
	app.use(apiVersion, imageResultsRouter);
};
