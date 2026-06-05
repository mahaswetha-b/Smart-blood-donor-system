# Smart Blood Donor Finder

## Project Overview

Smart Blood Donor Finder is a web-based application developed using Python Flask. The system helps manage blood donor information efficiently by allowing users to add, search, view, and delete donor records through a simple and user-friendly interface.

The project is designed to support blood donation management and make it easier to find donors based on blood groups. Donor information is stored in a CSV file, making the application lightweight and easy to use.

## Objectives

- Maintain donor information digitally
- Reduce manual record keeping
- Quickly search donors by blood group
- Provide an easy-to-use web interface
- Improve donor data management

## Features

### Add Donor
Users can add donor details including:
- Name
- Blood Group
- Phone Number
- City

### Search Donor
Users can search donors based on blood groups.

### View Donors
Displays all donor records in a structured table format.

### Delete Donor
Allows removal of donor records from the system.

## Technologies Used

- Python
- Flask
- HTML
- CSS
- CSV File Storage

## Project Structure

```text
Smart-Blood-Donor-Finder/
│
├── app.py
├── donors.csv
└── templates/
    └── index.html
```

## Installation

1. Install Flask

```bash
pip install flask
```

2. Run the application

```bash
py app.py
```

3. Open the browser and visit:

```text
http://127.0.0.1:5000
```

## Future Enhancements

- MySQL Database Integration
- User Authentication
- Update Donor Information
- Email Notifications
- Responsive User Interface

## Academic Purpose

This project was developed to learn Flask web development, CRUD operations, and basic data management techniques.

## Author

Mahaswetha
