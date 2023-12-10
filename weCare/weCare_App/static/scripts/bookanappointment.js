document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('#specialityField').addEventListener('change', (event) => {
        console.log('value', event.currentTarget.value);

        // Corrected variable name: doctotSpeciality to doctorSpeciality
        const allDoctorsOptions = document.querySelectorAll('#doctorField option');
        for (const doctor of allDoctorsOptions) {
            const doctorSpeciality = doctor.getAttribute('data-speciality');
            if (doctorSpeciality === event.currentTarget.value) {
                doctor.classList.remove('hidden');
            } else {
                doctor.classList.add('hidden');
            }
        }
    });

    document.querySelector('#doctorField').addEventListener('change', (event) => {
        const doctorId = event.currentTarget.value;
    
        fetch(`/api/fetch-hospitals/${doctorId}?v=${Math.random() * 100000}`, {
            method: 'get',
            headers: {
                'Content-Type': 'application/json',
                // Add other headers if needed
            },
        })
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            console.log(typeof data);
    
            // Parse the string into a JavaScript array
            const hospitalsArray = JSON.parse(data.hospitals);
    
            // Assuming hospitalsArray is an array
            const hospitalSelect = document.querySelector('#hospitalField');
    
            // Clear existing options
            hospitalSelect.innerHTML = '';
    
            // Add a default hidden option
            const defaultOption = document.createElement('option');
            defaultOption.value = '';
            defaultOption.text = '---Select a Hospital---';
            hospitalSelect.add(defaultOption);
    
            // Check if hospitalsArray is an array
            if (Array.isArray(hospitalsArray)) {
                // Iterate through the hospitals and add options to the select element
                hospitalsArray.forEach(hospital => {
                    const option = document.createElement('option');
                    option.value = hospital.fields.id;
                    option.text = hospital.fields.name;
                    hospitalSelect.add(option);
                });
            } else {
                console.error('Data.hospitals is not an array:', hospitalsArray);
                // Handle other data structures as needed
            }
        })
        .catch(error => console.error('Fetch error:', error));
    });





    var enabledDates = ['2023-12-30', '2023-12-28', '2023-12-29'];


    // Function to check if a date is enabled
    function isDateEnabled(date) {
      return enabledDates.includes(date);
    }

    // Event listener to enable specific dates
    document.querySelector('#dateField').addEventListener('input', function() {
      var selectedDate = this.value;
      if (!isDateEnabled(selectedDate)) {
        alert('This date is not enabled. Please choose another date.');
        this.value = ''; // Reset the input value
      }
    });
    
});
