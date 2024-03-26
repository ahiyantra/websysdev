import React, { useState, useEffect } from 'react';
import axios from 'axios';

const PersonForm = () => {
  const [formData, setFormData] = useState({
    name: '',
    surname: '',
    phone: '',
    address: '',
    age: '',
  });
  const [message, setMessage] = useState('');
  const [persons, setPersons] = useState([]);

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
    setMessage(''); // Clear the message when form data changes
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    let isValid = true;
    let errorMessage = '';

    // Client-side validation
    if (!formData.name || !formData.surname || !formData.phone || !formData.address || !formData.age) {
      errorMessage = 'Please fill in all fields.';
      isValid = false;
    } else if (!/^\d{8}$/.test(formData.phone)) {
      errorMessage = 'Phone number must be 8 digits long and contain only numbers.';
      isValid = false;
    } else if (formData.age <= 0) {
      errorMessage = 'Age must be greater than zero.';
      isValid = false;
    }

    if (!isValid) {
      setMessage(errorMessage);
      return;
    }

    try {
      const response = await axios.post('/api/people', formData);
      console.log("post:\n"+JSON.stringify(response.data)); // debug
      const newPerson = response.data;
      setPersons([...persons, newPerson]);
      setMessage('Data saved successfully!');
      setFormData({ name: '', surname: '', phone: '', address: '', age: '' });
    } catch (error) {
      if (error.response && error.response.data && error.response.data.errors) {
        const validationErrors = error.response.data.errors;
        const ageError = validationErrors.age;
        const phoneError = validationErrors.phone;
        if (ageError) {
          setMessage(`Age error: ${ageError[0]}`);
        } else if (phoneError) {
          setMessage(`Phone error: ${phoneError[0]}`);
        } else {
          setMessage('Error saving data. Please try again.');
        }
      } else {
        setMessage('Error saving data. Please try again.');
      }
    }
  };

  useEffect(() => {
    const fetchPersons = async () => {
      try {
        const response = await axios.get('/api/people');
        console.log("get:\n"+JSON.stringify(response.data)); // debug
        setPersons(response.data);
      } catch (error) {
        console.error('Error fetching persons:', error);
      }
    };

    fetchPersons();
  }, []);

  return (
    <div className="container">
      {message && <div className={`message ${message.includes('successfully') ? 'success' : 'error'}`}>{message}</div>}
      <form onSubmit={handleSubmit}>
        <label>
          Name:
          <input type="text" name="name" value={formData.name} onChange={handleChange} />
        </label>
        <label>
          Surname:
          <input type="text" name="surname" value={formData.surname} onChange={handleChange} />
        </label>
        <label>
          Telephone:
          <input type="text" name="phone" value={formData.phone} onChange={handleChange} />
        </label>
        <label>
          Address:
          <input type="text" name="address" value={formData.address} onChange={handleChange} />
        </label>
        <label>
          Age:
          <input type="number" name="age" value={formData.age} onChange={handleChange} />
        </label>
        <button type="submit">Submit</button>
      </form>
      <h2>Entered Data</h2>
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Surname</th>
            <th>Phone</th>
            <th>Address</th>
            <th>Age</th>
          </tr>
        </thead>
        <tbody>
          {persons.map((person) => (
            <tr key={person.id}>
              <td>{person.id}</td>
              <td>{person.name}</td>
              <td>{person.surname}</td>
              <td>{person.phone}</td>
              <td>{person.address}</td>
              <td>{person.age}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default PersonForm;