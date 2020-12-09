import React, { useEffect, useState } from 'react';
import './App.css';

function List() {

    useEffect(() => {
        fetchCars();
    }, []);

    const [cars, setCars] = useState([]);

    const fetchCars = async () => {
        const data = await fetch(
            'http://localhost:8000/car/'
        );
        const cars = await data.json();
        console.log(cars);
        setCars(cars);
    }

    return (
        <div>
            <div>
                <h1 className='PageLabel'>Car List</h1>
            </div>
            <div id='List' >
                <ul className='SideUl'>
                {cars.map(car => (
                    <li className='MainLi' key={car.id}>{car.brand} {car.model}</li>
                ))}
                </ul>
            </div>
        </div>
    );

}

export default List;
