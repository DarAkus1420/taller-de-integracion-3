import { Router } from 'express';
import imageResultsController from './controller';

const imageResultsRouter = Router();

imageResultsRouter.get('/imageResults', imageResultsController.getAll);

imageResultsRouter.get('/imageResults/:id', imageResultsController.getOneById);

imageResultsRouter.post('/imageResults', imageResultsController.createOne);

imageResultsRouter.put('/imageResults/:id', imageResultsController.updateOne);

imageResultsRouter.delete('/imageResults/:id', imageResultsController.deleteOneById);

export default imageResultsRouter;
