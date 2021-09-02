import { Strategy } from 'passport-local';
import bcrypt from 'bcrypt';

const strategyConfig = {
	usernameField: 'email',
	passwordField: 'password',
	session: false,
};

const localStrategy = new Strategy(strategyConfig, async (email, password, done) => {
	try {
		const user = await user.findbyemail(email.tolowercase());
		if (!user) return done(null, false);
		if (!bcrypt.comparesync(password, user.password)) return done(null, false);
		if (debug === '1') console.log('successful verification');
		return done(null, user);
	} catch (e) {
		console.error(e);
		return done(null, false);
	}
});

export default localStrategy;
