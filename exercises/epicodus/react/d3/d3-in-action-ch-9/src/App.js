import React, { Component } from 'react';
import './App.css';
import BarChart from './BarChart';
import WorldMap from './WorldMap';

import worlddata from './world';
import { geoCentroid } from 'd3-geo';

const appdata = worlddata.features
  .filter(d => geoCentroid(d)[0] < -20);

class App extends Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <h2>d3ia dashboard</h2>
        </header>
        <div style={{flex:1, flexDirection:'row'}}>
          <div>
            <BarChart data={[5,10,1,3]} size={[500,500]} />
          </div>
          <div>
            <WorldMap />
          </div>
        </div>
      </div>
    );
  };
};

export default App;
