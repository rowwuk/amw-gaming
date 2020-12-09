import React from 'react';
import './App.css';
import { Link } from 'react-router-dom';

function Nav() {

  const navStyle = {
    color: '#f05454',
    textDecoration: 'none'
  };

  return (
    <nav>
      <h1 id='Logo'>Cars</h1>
      <ul className='SideUl'>
        <Link to="/" style={navStyle}>
          <li className='SideLi'>Car List</li>
        </Link>
        <Link to="/detail" style={navStyle}>
          <li className='SideLi'>Car Details</li>
        </Link>
      </ul>
    </nav>
  );
}

export default Nav;
