const jwt = require('jsonwebtoken')
const {secret} = require('../config')

module.exports = (req, res, next) => {
    if (req.method == 'OPTIONS') {
        next()
    }

    try {
        if (!req.headers.authorization) {
            return res.status(400).json({message: "No authorization header"})
        }
        // "Beaver token"
        const token = req.headers.authorization.split(' ')[1]
        if (!token) {
            return res.status(400).json({message: "User isn't logged"})
        }
        const decoded = jwt.verify(token, secret)
        req.user = decoded
        next()
    } catch(e) {
        return res.status(400).json({message: "User isn't logged"})
    }
}