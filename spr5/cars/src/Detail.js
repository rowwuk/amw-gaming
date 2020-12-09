import React, { useEffect, useState } from 'react';
import './App.css';

function Detail() {

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
        <h1 className='PageLabel'>Car Details</h1>
      </div>
      <div id='List' >

        {cars.map(car => (
          <ul className='SideUl' key={car.id}>
            <li className='MainLi'>Model: {car.model}</li>
            <li className='MainLi'>Brand: {car.brand}</li>
            <li className='MainLi'>Date: {car.year}</li>
            <li className='MainLi'>Door Count: {car.doors}</li>
          </ul>
        ))}

      </div>
    </div>
  );

}

export default Detail;
