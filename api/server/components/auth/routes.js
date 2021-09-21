import { Router } from "express"
import passport from 'passport'
import authController from './controller'

const authRouter = Router();

authRouter.post('/auth/login',
    passport.authenticate('local', { session: true }),
    authController.login
)

authRouter.post('/auth/register', authController.register);