const Router = require('express');
const router = new Router()
const controller = require('../Controllers/storagecon')
const {check} = require('express-validator')
const path = require('path');

const multer = require("multer")
const storage = multer.diskStorage({
    destination: function (req, file, cb) {
        cb(null, path.join(appRoot, '/storage/'))
    },
    filename: function (req, file, cb) {
        console.log(file)
        cb(null, file.originalname + '-' + new Date().toISOString().replace(/[:\.]/g, '-'));
    }
})

const upload = multer({ storage: storage })

// const upload = multer.diskStorage({
//     destination: function (req, file, cb) {
//         cb(null, 'storage/')
//     },
//     filename: function (req, file, cb) {
//         cb(null, file.originalname)
//     }
// })

router.post('/getByName', controller.getByName)
router.post('/getList', controller.getList)
router.post('/upload', upload.single("file"), controller.uploadFile)



module.exports = router;