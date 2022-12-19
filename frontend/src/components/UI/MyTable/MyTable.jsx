import React from 'react';
import classes from './MyTable.module.css'
const MyTable = ({items}) => {
    return (
        <table className={classes.table}>
            <thead>
                <tr>
                    <th>#</th>
                    <th>Код тс</th>
                    <th>Статус</th>
                    <th>Ответ</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>1</td>
                    <td>123</td>
                    <td>44</td>
                    <td>1</td>
                </tr>
            </tbody>
        </table>
    );
};

export default MyTable;