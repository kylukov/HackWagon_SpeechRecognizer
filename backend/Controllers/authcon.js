const User = require('../Models/User')

const bcrypt = require('bcrypt');
const saltRounds = 7;

const validatotionResult = require('express-validator').validationResult;

const jwt = require('jsonwebtoken')
const {secret} = require('../config.js')

const generateToken = (id, email) => {
    const payLoad = {id, email}
    return jwt.sign(payLoad, secret, {expiresIn: "12H"})
}

class authcon {
    async registration(req, res) {
        try {
            console.log(req)
            const err = validatotionResult(req.body)
            if (!err.isEmpty()) {
                return res.status(400).json({message: 'Validation error'})
            }

            const {email, name, password} = req.body;
            const candidate = await User.findOne({email: email})
            if (candidate) {
                return res.status(400).json({message: 'User with that email already exists'})
            }
            const passwordHash = bcrypt.hashSync(password, saltRounds);
            const user = new User({email, name, password: passwordHash, create_date: new Date().toISOString()})
            await user.save()
            return res.json({message: 'User had been registered!'})
        } catch(e) {console.log(e);res.status(400).json({message: "Registration error"})}
    }

    async login(req, res) {
        try {
            const {email, password} = req.body;
            const user = await User.findOne({email})
            if (!user) return res.status(400).json({message: 'User with E-MAIL ' + email + ' dont exists'})
            const isPasswordValid = bcrypt.compareSync(password, user.password)
            if (!isPasswordValid) return res.status(400).json({message: 'Invalid password'})
            const token = generateToken(user._id, email)
            return res.json({token: token, email: email})

        } catch(e) {console.log(e);res.status(400).json({message: "Login error"})}
    }

    async check(req, res) {
        try {
            const token = jwt.verify(req.headers.authorization.split(' ')[1], secret)
            return res.json({token})
        } catch(e) {console.log(e);res.status(400).json({message: "Check error"})}
    }
}

module.exports = new authcon();