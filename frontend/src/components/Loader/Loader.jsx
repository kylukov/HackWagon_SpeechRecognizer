import React from 'react';
import classes from './Loader.module.css';

const Loader = ({...props}) => {
    return <div {...props}>

        <div class={classes.ldsDefault}><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div></div>

    </div>
};

export default Loader;