import React from 'react';
import map from './logo.png';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={map} className="App-logo" alt="logo"/>
        <p>
          <a href="http://45.32.220.47:8080/secure/Dashboard.jspa">LOGIN</a>
          <Link to="/dashboard">
              <button type="button">
                    LOGIN
              </button>
          </Link>
        </p>
      </header>
      
    </div>
  );
}

export default App;
//comment push test
