import React, { useState } from 'react';
import classes from './MyDragDrop.module.css';
import uploadIcon from '../../assets/images/uploadIcon.svg';
import axios from 'axios';

const MyDragDrop = ({file, setFile}) => {
    const [drag, setDrag] = useState(false);

    function dragStartHandler(e) {
        e.preventDefault();
        setDrag(true)
    }

    function dragLeaveHandler(e) {
        e.preventDefault();
        setDrag(false)
    }

    function onDropHandler(e) {
        e.preventDefault();
        let files = [...e.dataTransfer.files]
        if (files[0]) setFile(files[0])
        setDrag(false)
    }

    return (
        <>
        
        <div className={classes.wrapper}>
            <div className={classes.dragArea}
                onDragStart={e => dragStartHandler(e)}
                onDragLeave={e => dragLeaveHandler(e)}
                onDragOver={e => dragStartHandler(e)}
                onDrop={e => onDropHandler(e)}
            ></div>
            <div className={classes.container}>
                <div className={classes.left}>
                    <img src={uploadIcon} alt="" />
                </div>
                {!drag 
                ?   <div className={classes.right}>
                        <span className={classes.title}>Перетащите файл</span>
                        <span className={classes.text}>
                            типы файлов <span className={classes.mark}>MP3</span>,<span className={classes.mark}>WAV</span>
                        </span>
                    </div>
                :   <div className={classes.right}>
                        <span className={classes.title}>Отпустите файл</span>
                    </div>
                }
            </div>
        </div>
        </>
    );
};

export default MyDragDrop;