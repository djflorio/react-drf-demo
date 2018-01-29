import React, { Component } from 'react';
import FontAwesome from 'react-fontawesome';
import './TopBar.css';

class TopBar extends Component {
  render() {
    return (
      <div className="top-bar">
        <h3>TEST</h3>
        <FontAwesome name='shopping-cart' />
      </div>
    );
  }
}

export default TopBar;