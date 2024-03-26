document.getElementById('dataForm').addEventListener('submit', function(event) {
    // Prevent form submission
    event.preventDefault(); 
    // Validate form data
    if (validateForm()) {
        // If validation passes, send data to server (using AJAX)
        sendDataToServer();
    }
});

function validateForm() {
    // Implement validation logic here
    // For example, check if all fields are filled and if telephone contains only numbers
    var name = document.getElementById('name').value;
    var surname = document.getElementById('surname').value;
    var telephone = document.getElementById('telephone').value;
    var address = document.getElementById('address').value;
    var age = document.getElementById('age').value;

    if (name === '' || surname === '' || telephone === '' || address === '' || age === '') {
        alert('Please fill in all fields.');
        return false;
    }

    if (!/^\d+$/.test(telephone) || telephone.length !== 8) {
        alert('Telephone number must contain only digits and be 8 characters long.');
        return false;
    }

    if (age <= 0) {
        alert('Age must be greater than zero.');
        return false;
    }

    // Return true if validation passes, false otherwise
    return true; 
}

function sendDataToServer() {
    console.log('sending AJAX request ...');
    
    // Construct a JSON object containing input values
    var jsonData = {
        name: document.getElementById('name').value,
        surname: document.getElementById('surname').value,
        telephone: document.getElementById('telephone').value,
        address: document.getElementById('address').value,
        age: document.getElementById('age').value
    };
    console.log("json form data : ", jsonData);

    // Send the JSON object to the server using AJAX
    var xhr = new XMLHttpRequest();
    xhr.open('POST', 'http://localhost:8000/submit', true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function() {
        if (xhr.readyState === XMLHttpRequest.DONE) {
            if (xhr.status === 200) {
                var response = JSON.parse(xhr.responseText);
                updateTable(response.data);
            } else {
                console.error('Error:', xhr.statusText);
            }
        }
    };
    xhr.send(JSON.stringify(jsonData));
}

// Function to update table with entered data
function updateTable(response_data) {
    console.log('updating the table ...');
    var tableBody = document.getElementById('dataTableBody');

    // Check if data is not null or undefined and is an array
    if (response_data && Array.isArray(response_data)) { 
        response_data.forEach(function(row) {
            var newRow = '<tr>';
            newRow += '<td>' + (row.name || '') + '</td>';
            newRow += '<td>' + (row.surname || '') + '</td>';
            newRow += '<td>' + (row.telephone || '') + '</td>';
            newRow += '<td>' + (row.address || '') + '</td>';
            newRow += '<td>' + (row.age || '') + '</td>';
            newRow += '</tr>';
            tableBody.innerHTML += newRow;
        });
        console.log("response data : ", response_data);
    } else {
        console.error('invalid response data received : ', response_data);
    }
}

// Fetch initial data from the server
window.addEventListener('DOMContentLoaded', function() {
    var xhr = new XMLHttpRequest();
    xhr.open('GET', 'http://localhost:8000/api', true);
    xhr.onreadystatechange = function() {
        if (xhr.readyState === XMLHttpRequest.DONE) {
            if (xhr.status === 200) {
                var response = JSON.parse(xhr.responseText);
                updateTable(response.data);
            } else {
                console.error('Error:', xhr.statusText);
            }
        }
    };
    xhr.send();
});

// adding example
updateTable([{name:"Nicholas", surname:"Szabó", telephone:"0123456789", address:"Washington DC, The USA.", age:"60"}])