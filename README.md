# Cinema Application

This is a Django-based cinema management application that allows users to manage cinema rooms, schedule movies with specific showtimes, and ensure there are no conflicts between movie schedules in the same room. The application provides validation to avoid scheduling overlapping movies in a specific room by enforcing time gaps between the movies.

## Features

- **Cinema Room Management**: Users can create and manage cinema rooms.
- **Movie Scheduling**: Movies can be scheduled for specific rooms with unique start times and durations.
- **Automatic Conflict Checking**: The system automatically checks for scheduling conflicts in the same room and ensures that no movies overlap.
- **Buffer Time Enforcement**: A buffer of 30 minutes is enforced between movies to allow for theater cleaning, transitions, and other logistics.
- **Seat Booking System**: Users can view available seats for a specific movie in a specific room and select a seat to book. Once a seat is booked, it is marked as unavailable, ensuring no other user can book the same seat for that movie and time.
- **Automatic Seat Management**:
  - **Room Creation**: When a new room is created, the system automatically generates seats based on the specified number of rows and columns. For example, if a room has 5 rows and 10 columns, 50 seats will be created in the database.
  - **Room Update**: When the room configuration (number of rows and columns) is updated, the seat configuration is automatically adjusted. The system will add seats if the number of rows or columns increases or remove seats if the capacity decreases. This ensures the seat layout always reflects the current room capacity.

- **Poster Management**: Each movie can have an associated poster image that is automatically deleted from the filesystem when the movie is deleted.
- **Cascading Deletions**: When a room is deleted, all associated movies are deleted, and their posters are removed from the filesystem.

## Demo Video

[Click here to download and watch the demo video](./demo/demo-video.mp4)


## Installation

To set up and run the cinema application, follow the steps below:

### Prerequisites

- Python 3.12.5
- Django 5.1.1
- SQlite
- Virtualenv

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/RabbiHasanR/movie_theater_ticket_booking_application.git
   cd movie_theater_ticket_booking_application
2. Set up a virtual environment
    ```bash
    virtualenv env
    source env/bin/activate
3. Install Dependencies:
    ```bash
    pip install -r requirements.txt
4. Create the necessary database migrations:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
5. Create superuser to access the admin panel
    ```bash
    python manage.py createsuperuser
6. Run the development server
    ```bash
    python manage.py runserver
7. Access the admin panel at http://127.0.0.1:8000/admin/ to start managing rooms and movies.
