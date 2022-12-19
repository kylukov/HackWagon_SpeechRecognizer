import React, {useRef} from 'react';
import classes from './MyIconButton.module.css';
const MyIconButton = ({children, icon, type, file, setFile, ...props}) => {
    const fileRef = React.useRef();
    const handleChange = (e) => {
        if (e.target.files[0]) setFile(e.target.files[0]);
    };
    if (type == 'file') {
        return (
            <button className={classes.button} onClick={() => fileRef.current.click()} {...props}>
                <input id="upload" name="upload" type="file" ref={fileRef} hidden
                onChange={(e) => handleChange(e)} />
                <img src={icon} alt="" />
            </button>
        );
    }
    return (
        <button className={classes.button} {...props}>
            <span>{children}</span>
            <img src={icon} alt="" />
        </button>
    );
};

export default MyIconButton;