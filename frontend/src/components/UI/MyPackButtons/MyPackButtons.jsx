import React from 'react';
import { Link } from 'react-router-dom';
import classes from './MyPackButtons.module.css';

const MyPackButtons = ({items}) => {
    console.log(items)
    return (
        <div className={classes.wrapper}>
            {
                items.map((item) => {
                    console.log(item)
                    return <Link className={classes.button} key={item.name} to={item.route}>{item.name}</Link>
                })
            }
        </div>
    );
};

export default MyPackButtons;