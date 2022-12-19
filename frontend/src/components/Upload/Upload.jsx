import React from 'react';
import '../../assets/resetter.css';
import MyInput from '../UI/MyInput/MyInput';
import classes from './Upload.module.css';
import MyDragDrop from '../MyDragDrop/MyDragDrop';
import MyIconButton from '../UI/MyIconButton/MyIconButton';
import folderOpen from '../../assets/images/folderOpen.svg'
import sendIcon from '../../assets/images/sendIcon.svg'
import axios from 'axios';

const Upload = () => {
    const [file, setFile] = React.useState('');

    function sendFile(file) {
        const form = new FormData();
        form.append('file', file);
        const url = process.env.REACT_APP_REQUESTS_IP + process.env.REACT_APP_ROUTE_UPLOAD;
        axios.post(url, form) //, options
        setFile('');
    }

    return (
        <div className={classes.wrapper}>
            <div className={classes.input}>
                <MyInput placeholder="Ничего не выбрано" value={file.name || ''} disabled={true}/>
                <MyIconButton style={{'min-width': 70}} file={file} setFile={setFile} type="file" icon={folderOpen}/>
                <MyIconButton onClick={() => sendFile(file)} style={{'min-width': 200}} icon={sendIcon}>Отправить</MyIconButton>
            </div>
            <MyDragDrop file={file} setFile={setFile}/>
        </div>
    );
};

export default Upload;
