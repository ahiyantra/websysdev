import React, { useEffect } from 'react';
import PersonForm from './components/person_form';

function App() {
  useEffect(() => {
    document.title = 'Personal Data Entry Form - v1.2';
  }, []);

  return (
    <div>
      <h1>Personal Data Entry Form - v1.2</h1>
      <PersonForm />
    </div>
  );
}

export default App;