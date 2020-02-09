import React from 'react';
import map from './logo.png';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={map} className="App-logo" alt="logo"/>
        <p>
          <form method="get" action="http://45.32.220.47:8080/secure/Dashboard.jspa">
            <button type="submit">LOGIN</button>
          </form>
        </p>
      </header>
      
    </div>
  );
}

export default App;