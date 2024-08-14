document.getElementById('emailForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const email = document.getElementById('email').value;

    fetch(`/get-details?email=${email}`)
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                document.getElementById('details').style.display = 'block';
                document.getElementById('name').value = data.details.name;
                document.getElementById('roll_number').value = data.details.roll_number;
                document.getElementById('batch').value = data.details.batch;
                document.getElementById('phone_number').value = data.details.phone_number;
            } else {
                alert('Email not found!');
            }
        });
});

document.getElementById('detailsForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const updatedDetails = {
        name: document.getElementById('name').value,
        roll_number: document.getElementById('roll_number').value,
        batch: document.getElementById('batch').value,
        phone_number: document.getElementById('phone_number').value,
    };

    fetch('/verify-details', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(updatedDetails)
    }).then(response => response.json())
    .then(data => {
        if (data.success) {
            alert('Details verified and updated successfully!');
        } else {
            alert('Failed to update details!');
        }
    });
});

document.getElementById('updateButton').addEventListener('click', function() {
    document.getElementById('detailsForm').submit();
});
