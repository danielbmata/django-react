import React from 'react';
import './App.css';
import { Routes, Route } from 'react-router-dom';
import Home from './components/Home';
import Create from './components/Create';
import About from './components/About';
import NavBar from './components/NavBar';

function App() {
  const myWidth = 210 // largura do sidebar
  return (
    <div className="App">
      <NavBar
        drawerWidth={myWidth}
        content={

          <Routes>
            <Route path="" element={<Home />} />
            <Route path="/create" element={<Create />} />
            <Route path="/about" element={<About />} />
          </Routes>

        }

      />
    </div>
  );
}

export default App;
