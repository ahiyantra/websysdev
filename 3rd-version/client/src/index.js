import React from 'react';
import ReactDOM from 'react-dom';
import App from './app';
import './components/person_form.css';

const rootElement = document.getElementById('root');

if (!rootElement) {
  const newRootElement = document.createElement('div');
  newRootElement.id = 'root';
  document.body.appendChild(newRootElement);
  ReactDOM.render(
    <React.StrictMode>
      <App />
    </React.StrictMode>,
    newRootElement
  );
} else {
  ReactDOM.render(
    <React.StrictMode>
      <App />
    </React.StrictMode>,
    rootElement
  );
}