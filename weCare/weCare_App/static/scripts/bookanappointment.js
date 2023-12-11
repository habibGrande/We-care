const removeDuplicates = (arr) => {

    console.log('arr::', arr);
    const tmpArray = [];
    const seenDates = {};
    for(const date of arr) {
       console.log('seenDates::', seenDates);
        if(!seenDates[date.fields.date]) {

            seenDates[date.fields.date] = true
            tmpArray.push(date);
        }
    }
    return tmpArray;
  }

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
    let doctorId;
    document.querySelector('#doctorField').addEventListener('change', (event) => {
            doctorId = event.currentTarget.value;
    
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
            const hospitalsArray = JSON.parse(data.hospitals);
            const hospitalSelect = document.querySelector('#hospitalField');
            hospitalSelect.innerHTML = '';
            const defaultOption = document.createElement('option');
            defaultOption.value = '';
            defaultOption.text = '---Select a Hospital---';
            hospitalSelect.add(defaultOption);
            if (Array.isArray(hospitalsArray)) {
                hospitalsArray.forEach(hospital => {
                    const option = document.createElement('option');
                    option.value = hospital.pk;
                    option.text = hospital.fields.name;
                    hospitalSelect.add(option);
                });
            } else {
                console.error('Data.hospitals is not an array:', hospitalsArray);
            }
        })
        .catch(error => console.error('Fetch error:', error));
    });

    document.querySelector('#hospitalField').addEventListener('change', (event) => {
        const selectedHospitalId = event.currentTarget.value;
        console.log('selectedHospitalId::', selectedHospitalId);
        if (doctorId !== undefined && selectedHospitalId !== undefined) {
            fetch(`/api/fetch-dates/${doctorId}/${selectedHospitalId}?v=${Math.random() * 100000}`)
                .then(response => {
                    if (!response.ok) {
                        throw new Error(`HTTP error! Status: ${response.status}`);
                    }
                    return response.json();
                })
                .then(data => {
                    const datesArray = JSON.parse(data.available_dates);
                    const dateSelect = document.querySelector('#dateField');
                    dateSelect.innerHTML = '';
                    const defaultOption = document.createElement('option');
                    defaultOption.value = '';
                    defaultOption.text = '---Select a Date---';
                    dateSelect.add(defaultOption);
                    const filteredDates = removeDuplicates(datesArray)
                    if (filteredDates.length) {
                        filteredDates.forEach(date => {
                            const option = document.createElement('option');
                            option.value = date.pk;
                            option.text = date.fields.date;
                            dateSelect.add(option);
                        });
                    } else {
                        console.error('Data.available_dates is not an array:', datesArray);
                    }
                })
                .catch(error => console.error('Fetch error:', error));
        }
    });

    document.querySelector('#dateField').addEventListener('change', (event) => {
        const slectedDateId = event.currentTarget.value;
        console.log('slectedDateId::', slectedDateId);
        if (slectedDateId !== undefined) {
            fetch(`/api/fetch-times/${slectedDateId}?v=${Math.random() * 100000}`)
                .then(response => {
                    if (!response.ok) {
                        throw new Error(`HTTP error! Status: ${response.status}`);
                    }
                    return response.json();
                })
                .then(data => {

                    const timeArray = JSON.parse(data.available_times);
                    console.log('timeArray::', timeArray);
    
                    const timeSelect = document.querySelector('#timeField');
    
                    // Clear existing options
                    timeSelect.innerHTML = '';
    
                    // Add a default hidden option
                    const defaultOption = document.createElement('option');
                    defaultOption.value = '';
                    defaultOption.text = '---Select a Date---';
                    timeSelect.add(defaultOption);
    
                    // Check if hospitalsArray is an array
                    if (Array.isArray(timeArray)) {
                        // Iterate through the hospitals and add options to the select element
                        timeArray.forEach(date => {
                            const option = document.createElement('option');
                            option.value = date.pk;
                            option.text = date.fields.time;
                            timeSelect.add(option);
                        });
                    } else {
                        console.error('data.available_times is not an array:', timeArray);
                        // Handle other data structures as needed
                    }
                })
                .catch(error => console.error('Fetch error:', error));
        }
    });
    
});
