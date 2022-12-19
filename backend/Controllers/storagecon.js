const Storage = require('../Models/Storage')

class storagecon {

    async uploadFile(req, res) {
        try {
            if (!req.file) throw new Error('Can\'t get file from body');
            // const {email} 
            console.log('FILE:', req.file)
            const storage = new Storage({name: req.file.filename, status: 0, create_date: new Date().toISOString()})
            await storage.save()
            res.status(200).json({message: "Uploaded. Name: " + req.file.filename})

        } catch(e) {console.log(e);res.status(400).json({message: "Upload error"})}
    }

    async getByName(req, res) {
        try {
            console.log(req)

            const {name} = req.body;
            const file = await Storage.findByOne({"name": name})
            
            if (!file) {
                return res.status(400).json({message: 'There is no file with that name'})
            }
            return res.json(file)
        } catch(e) {console.log(e);res.status(400).json({message: "Registration error"})}
    }

    async getList(req, res) {
        try {
            const all = await Storage.find();
            console.log(all)
            res.status(200).json(all)

        } catch(e) {console.log(e);res.status(400).json({message: "Login error"})}
    }
}

module.exports = new storagecon();