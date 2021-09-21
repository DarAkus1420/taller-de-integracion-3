import localStrategy from '../middleware/strategies/local';

const passportConfig = passport => {
	passport.use('local', localStrategy);
	passport.serializeUser((user, done) => {
		done(null, user);
	});
	passport.deserializeUser((user, done) => {
		done(null, user);
	});
};

export default passportConfig;
