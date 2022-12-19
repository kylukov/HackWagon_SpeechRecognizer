import axios from 'axios';
import React, { useEffect, useState } from 'react';
import MyTable from '../UI/MyTable/MyTable';

const Download = () => {

    const [files, setFiles] = useState([]);
    async function getList() {
        const res = await axios.post(process.env.REACT_APP_REQUESTS_IP + process.env.REACT_APP_ROUTE_GETLIST, {}) 
        setFiles(res.data);
    }
    useEffect(() => {
        getList()
    }, [])
    return (
        <div>
            <MyTable />
        </div>
    );
};

export default Download;