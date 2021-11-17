//Packages
import express from 'express';
import passport from 'passport';
import mongoose from 'mongoose';

//Config
import passportConfig from './config/passport';
import expressConfig from './config/express';

//Routes
import routes from './routes/index';

import { dbUrl } from './config/dotenv';

const app = express();

expressConfig(app);
passportConfig(passport);
app.use(passport.initialize());
routes(app);

mongoose
	.connect(dbUrl)
	.then(console.info('Data base online'))
	.catch(error => console.error(error));
module.exports = app;
