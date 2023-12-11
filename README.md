# We Care Healthcare Platform (For Learning Purposes Only)

"We Care" is a revolutionary healthcare platform dedicated to transforming traditional health services into a seamless digital experience in Palestine.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Setting Up Django](#setting-up-django)
  - [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Introduction

"We Care" is a comprehensive healthcare platform designed to streamline hospital visits and doctor consultations in Palestine. Our mission is to enhance the quality and affordability of healthcare, ensuring accessibility for every patient through integrated clinical practices.

## Features

- **Digital Transformation:** We Care facilitates the digital transformation of traditional health services, bringing efficiency and convenience to the healthcare experience in Palestine.
- **Appointment Booking:** Patients can easily schedule appointments with doctors of their choice, specifying the desired specialty and treatment.
- **Doctor and Hospital Directory:** A comprehensive directory provides information on doctors and hospitals across different cities in Palestine, allowing users to make informed choices.
- **User Registration and Profiles:** Patients can create accounts on our website and make appointments.
- **Feedback and Reviews:** The platform encourages patients to provide feedback about their appointments, helping build trust and continuous improvement of services.

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:

- Python (version 3.12)
- Django (version 5.0)

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/your-repo.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd your-project-directory
    ```

3. **Create a virtual environment:**

    ```bash
    python -m venv venv
    ```

4. **Activate the virtual environment:**

    - On Windows:

      ```bash
      .\venv\Scripts\activate
      ```

    - On macOS/Linux:

      ```bash
      source venv/bin/activate
      ```

5. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

6. **Apply migrations:**

    ```bash
    python manage.py migrate
    ```

7. **Create a superuser:**

    ```bash
    python manage.py createsuperuser
    ```

8. **Start the development server:**

    ```bash
    python manage.py runserver
    ```

9. **Access the admin panel:**

   Visit `http://127.0.0.1:8000/admin/` and use the superuser credentials.

10. **Explore the healthcare platform:**

    Visit `http://127.0.0.1:8000/` to explore the healthcare platform.


