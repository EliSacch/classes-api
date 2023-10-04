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
    who is booking the class), date(date for which the member want to book a class)
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


2. __Booking__
 - id - Integer, PrimaryKey
 - client_name - String, Required
 - booked_date - Date, Required
