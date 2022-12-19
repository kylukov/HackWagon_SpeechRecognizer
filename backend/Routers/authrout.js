const Router = require('express');
const router = new Router()
const controller = require('../Controllers/authcon')
const {check} = require('express-validator')

router.post('/reg', [
    check('email', "Email invalid").isEmail(),
    check('password', "Password must be between 6 and 30 characters")
      .isLength({min: 6, max: 10})
], controller.registration)

router.post('/login', controller.login)

module.exports = router;