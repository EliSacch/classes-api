# classes-api
Fitness studio API to create classes and manage bookings


## User Stories

1. Story - Create classes
    
    As a __studio owner__ i want to __create classes__ for my studio so that my members can attend classes

    Acceptance Criteria
    - Implement an API to create classes(`/classes`). Assume this api doesn't need to have any
    authentication to start with.
    - Few bare minimum details we need to create classes are - class name, start_date, end_date,
    capacity. For now, assume that there will be only one class per given day. Ex: If a class by
    name pilates starts on 1st Dec and ends on 20th Dec, with capacity 10, that means Pilates
    has 20 classes and for each class the maximum capacity of attendance is 10.
    - No need to save the details in any database. Maintain an in memory array or a file to save the
    info. (If you want to use the database, that's fine as well).
    - Use Restful standards and create the api endpoint with proper success and error responses.
    
2. Story - Book for a class

    As a __member of a studio__, I can __book for a class__, so that I can attend a class.
    
    Acceptance Criteria
    - Implement an API endpoint (`/bookings`). Assume this api doesn't need to have any
    authentication to start with.
    - Few bare minimum details we need for reserving a class are - name(name of the member
    who is booking the class), date(date for which the member wants to book a class)
    - No need to save the details in DB. If you can maintain the state in an in memory array or a file
    is good to start with. But no constraints if you want to use a database to save the state.
    - Use REST standards and think through basic api responses for success and failure.
    - No need to consider the scenario of overbooking for a given date. Ex: 14th Dec having a
    capacity of 20 , but the number of bookings can be greater than 20.

## Project Planning

### Models

1. __GymClass__
    - id - Integer, PrimaryKey
    - class_name - String, Required
    - capacity - Integer, Required
    - start_date - Date, Required
    - end_date - Date, Required

    Note: I decided to call this model GymClass, instead of "Class" because __"class"__ is a reserved keyword in python and using "Class" could have created confusion.


2. __Booking__
    - id - Integer, PrimaryKey
    - client_name - String, Required
    - booked_date - Date, Required


### Endpoints

1. Classes

    Methods:
    - GET   /classes - Return all classes
    - POST  /classes - Create new class
    - GET   /classes/{id} - Return class with id of {id}
    - PUT   /classes/{id} - Edit class with id of {id}
    - DELETE    /classes/{id} - Delete class with id of {id}

2. Bookings

    Methods:
    - POST  /bookings
    - GET   /bookings/{id} - Return booking with id of {id}
    - DELETE    /bookings/{id} - Delete booking with id of {id}


## Local deployment

### 1. Clone the repo

### 2. Create and start virtual environment (reccommended)

### 3. Install dependencies from requirements.txt

In the terminal run the following code

        pip install -r requirements.txt

### 4. Run the app

In the terminal run the following code

        // Windows
        python main.py

        // Mac or Linux
        python3 main.py

### 5. Run test

In the rerminal run the following code

        python test.py