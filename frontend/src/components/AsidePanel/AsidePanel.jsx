import React from 'react';
import classes from './AsidePanel.module.css';
import logo from '../../assets/images/logo.svg';
import MyPackButtons from '../UI/MyPackButtons/MyPackButtons';

const AsidePanel = ({packButtons}) => {
    return (
        <aside className={classes.aside}>
            <div className={classes.logo}>
                <img src={logo} alt="Грузовая Компания" />
            </div>
            <MyPackButtons items={packButtons}/>
        </aside>
    );
};

export default AsidePanel;
