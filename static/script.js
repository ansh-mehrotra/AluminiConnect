
document.getElementById('emailForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const email = document.getElementById('email').value;
    const dob = document.getElementById('dob').value;
    const fathers_name = document.getElementById('fathers_name').value;

    const queryParams = new URLSearchParams();
    if (email) queryParams.append('email', email);
    if (dob && fathers_name) {
        queryParams.append('dob', dob);
        queryParams.append('fathers_name', fathers_name);
    }

    fetch(`/get-details?${queryParams.toString()}`)
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                document.getElementById('details').style.display = 'block';
                document.getElementById('name').innerText = data.details.Name || '';
                document.getElementById('batch').innerText = data.details.Batch || '';
                document.getElementById('roll_number').innerText = data.details['Roll Number'] || '';
                document.getElementById('program_name').innerText = data.details['Program Name'] || '';
                document.getElementById('branch').innerText = data.details['Branch'] || '';
                document.getElementById('passout_year').innerText = data.details['Passout Year'] || '';
                document.getElementById('dob_display').innerText = data.details['DOB'] || '';
                document.getElementById('email_display').innerText = data.details.Email || '';
                document.getElementById('phone_number').innerText = data.details['Phone Number'] || '';
                document.getElementById('whatsapp_number').innerText = data.details['WhatsApp Number'] || '';
                document.getElementById('current_designation').innerText = data.details['Current Designation'] || '';
                document.getElementById('current_company').innerText = data.details['Current Company'] || '';
                document.getElementById('current_city').innerText = data.details['Current City'] || '';
                document.getElementById('current_country').innerText = data.details['Current Country'] || '';
                document.getElementById('linkedin').innerText = data.details.LinkedIn || '';
                document.getElementById('linkedin').href = data.details.LinkedIn || '#';
                document.getElementById('fathers_name_display').innerText = data.details['Father Name'] || '';
                document.getElementById('home_state').innerText = data.details['Home State'] || '';
            } else {
                alert('No matching records found!');
            }
        })
        .catch(error => {
            console.error('Error fetching data:', error);
        });
});

document.getElementById('updateForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const formData = new FormData();

    formData.append('name', document.getElementById('name').innerText);
    formData.append('batch', document.getElementById('batch').innerText);
    formData.append('roll_number', document.getElementById('roll_number').innerText);
    formData.append('program_name', document.getElementById('program_name').innerText);
    formData.append('branch', document.getElementById('branch').innerText);
    formData.append('passout_year', document.getElementById('passout_year').innerText);
    formData.append('dob', document.getElementById('dob_display').innerText);
    formData.append('email', document.getElementById('email_display').innerText);
    formData.append('phone_number', document.getElementById('phone_number').innerText);
    formData.append('whatsapp_number', document.getElementById('whatsapp_number').innerText);
    formData.append('current_designation', document.getElementById('current_designation').innerText);
    formData.append('current_company', document.getElementById('current_company').innerText);
    formData.append('current_city', document.getElementById('current_city').innerText);
    formData.append('current_country', document.getElementById('current_country').innerText);
    formData.append('linkedin', document.getElementById('linkedin').innerText);
    formData.append('fathers_name', document.getElementById('fathers_name_display').innerText);
    formData.append('home_state', document.getElementById('home_state').innerText);

    fetch('/update-details', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert('Record updated successfully!');
        } else {
            alert('Failed to update the record: ' + data.message);
        }
    })
    .catch(error => {
        console.error('Error updating data:', error);
    });
});
