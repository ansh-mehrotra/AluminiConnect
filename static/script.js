
document.getElementById('updateForm').addEventListener('submit', function(event) {
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
                const details = data.details;

                document.getElementById('enrollment_no').innerText = details['ENROLLMENTNO'] || '';
                document.getElementById('student_name').innerText = details['STUDENTNAME'] || '';
                document.getElementById('father_name').innerText = details['FATHERNAME'] || '';
                document.getElementById('program').innerText = details['PROGRAM'] || '';
                document.getElementById('branch').innerText = details['BRANCH'] || '';
                document.getElementById('passout_year').innerText = details['PASSOUT YEAR'] || '';
                document.getElementById('birth_date').innerText = details['BIRTH DATE'] || '';
                document.getElementById('email_id1').innerText = details['EMAIL ID1'] || '';
                document.getElementById('email_id2').innerText = details['EMAIL ID2'] || '';
                document.getElementById('contact_no').innerText = details['CONTACT NO.'] || '';
                document.getElementById('whatsapp_no').innerText = details['WHATSAPP NO.'] || '';
                document.getElementById('home_state').innerText = details['HOME STATE'] || '';
                document.getElementById('linkedin_page').innerText = details['LINKEDIN PAGE'] || '';
                document.getElementById('last_update_date').innerText = details['LAST UPDATE DATE'] || '';
                document.getElementById('current_designation').innerText = details['CURRENT DESIGNATION'] || '';
                document.getElementById('company').innerText = details['COMPANY'] || '';
                document.getElementById('city').innerText = details['CITY'] || '';
                document.getElementById('country').innerText = details['COUNTRY'] || '';
                document.getElementById('degree_name').innerText = details['DEGREE NAME'] || '';
                document.getElementById('branch_specialization').innerText = details['BRANCH/SPECIALIZATION'] || '';
                document.getElementById('institute_name').innerText = details['INSTITUTE NAME'] || '';
                document.getElementById('institute_city').innerText = details['CITY'] || '';
                document.getElementById('institute_country').innerText = details['COUNTRY'] || '';
                document.getElementById('joining_year').innerText = details['JOINING YEAR'] || '';
                document.getElementById('completion_year').innerText = details['COMPLETION YEAR'] || '';
                document.getElementById('highest_degree_name').innerText = details['HIGHEST DEGREE NAME'] || '';
                document.getElementById('hd_branch_specialization').innerText = details['HD BRANCH/SPECIALIZATION'] || '';
                document.getElementById('hd_institute_name').innerText = details['HD INSTITUTE NAME'] || '';
                document.getElementById('hd_city').innerText = details['HD CITY'] || '';
                document.getElementById('hd_country').innerText = details['HD COUNTRY'] || '';
                document.getElementById('hd_joining_year').innerText = details['HD JOINING YEAR'] || '';
                document.getElementById('hd_completion_year').innerText = details['HD COMPLETION YEAR'] || '';
            }
        })
        .catch(error => {
            console.error('Error fetching details:', error);
        });
});

document.getElementById('updateForm').addEventListener('submit', function(event) {
    event.preventDefault();

    document.getElementById('updateForm').addEventListener('submit', function(event) {
        event.preventDefault();
    
        const formData = new FormData();
    
        formData.append('ENROLLMENTNO', document.getElementById('enrollment_no').innerText);
        formData.append('STUDENTNAME', document.getElementById('student_name').innerText);
        formData.append('FATHERNAME', document.getElementById('father_name').innerText);
        formData.append('PROGRAM', document.getElementById('program').innerText);
        formData.append('BRANCH', document.getElementById('branch').innerText);
        formData.append('PASSOUT YEAR', document.getElementById('passout_year').innerText);
        formData.append('BIRTH DATE', document.getElementById('birth_date').innerText);
        formData.append('EMAIL ID1', document.getElementById('email_id1').innerText);
        formData.append('EMAIL ID2', document.getElementById('email_id2').innerText);
        formData.append('CONTACT NO.', document.getElementById('contact_no').innerText);
        formData.append('WHATSAPP NO.', document.getElementById('whatsapp_no').innerText);
        formData.append('HOME STATE', document.getElementById('home_state').innerText);
        formData.append('LINKEDIN PAGE', document.getElementById('linkedin_page').innerText);
        formData.append('LAST UPDATE DATE', document.getElementById('last_update_date').innerText);
        formData.append('CURRENT DESIGNATION', document.getElementById('current_designation').innerText);
        formData.append('COMPANY', document.getElementById('company').innerText);
        formData.append('CITY', document.getElementById('city').innerText);
        formData.append('COUNTRY', document.getElementById('country').innerText);
        formData.append('DEGREE NAME', document.getElementById('degree_name').innerText);
        formData.append('BRANCH/SPECIALIZATION', document.getElementById('branch_specialization').innerText);
        formData.append('INSTITUTE NAME', document.getElementById('institute_name').innerText);
        formData.append('INSTITUTE CITY', document.getElementById('institute_city').innerText);
        formData.append('INSTITUTE COUNTRY', document.getElementById('institute_country').innerText);
        formData.append('JOINING YEAR', document.getElementById('joining_year').innerText);
        formData.append('COMPLETION YEAR', document.getElementById('completion_year').innerText);
        formData.append('HIGHEST DEGREE NAME', document.getElementById('highest_degree_name').innerText);
        formData.append('HD BRANCH/SPECIALIZATION', document.getElementById('hd_branch_specialization').innerText);
        formData.append('HD INSTITUTE NAME', document.getElementById('hd_institute_name').innerText);
        formData.append('HD CITY', document.getElementById('hd_city').innerText);
        formData.append('HD COUNTRY', document.getElementById('hd_country').innerText);
        formData.append('HD JOINING YEAR', document.getElementById('hd_joining_year').innerText);
        formData.append('HD COMPLETION YEAR', document.getElementById('hd_completion_year').innerText);
    
        fetch('/update-details', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert('Details updated successfully.');
            } else {
                alert('Error updating details.');
            }
        })
        .catch(error => {
            console.error('Error updating details:', error);
        });
    });
});

