//Packages
import express from 'express';
import passport from 'passport';

//Config
import passportConfig from './config/passport';
import expressConfig from './config/express';

//Routes
import routes from './routes/index';

const app = express();

expressConfig(app);
passportConfig(passport);
app.use(passport.initialize());
routes(app);

module.exports = app;
