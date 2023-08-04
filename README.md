# University Library System

This is a fullstack web application that simulates a university library system. It allows users to sign up, log in, browse books, borrow books, return books, and update their details. It also allows admins to add books, update book details, and manage users.

## Technologies Used

- HTML, CSS, and Ajax for the frontend
- Python Django for the backend
- JavaScript for client-side input validation
- Bootstrap for some pages

## Main Features

- Home page: displays the welcome message and the navigation bar
- Signing up: allows users to create an account as either admin or student
- Login: allows users to log in with their username and password
- Updating user details: allows users to change their name, email, password, etc.
- Adding a book: allows admins to add a new book to the library database
- Updating book details: allows admins to edit the information of an existing book
- Browsing books: allows users to view all the books in the library
- Showing a list of books: allows users to search for books by ISBN, publication year, author, etc.
- Performing operations on books: allows users to borrow, return, or extend the borrowing period of a book
- Log out: allows users to log out of their account

## Installation

To run this project locally, you need to have Python and Django installed on your machine. Then follow these steps:

1. Clone this repository or download it as a zip file
2. Navigate to the project folder and open a terminal window
3. Run `pip install -r requirements.txt` to install the dependencies
4. Run `python manage.py migrate` to create the database tables
5. Run `python manage.py createsuperuser` to create an admin account
6. Run `python manage.py runserver` to start the development server
7. Open your browser and go to `http://localhost:8000/` to access the application

## Team members

This project was developed by:

- [Khaled Ashraf](https://github.com/KhaledAshrafH)
- [Ahmed Sayed](https://github.com/AhmedSayed117)
- [Shimaa Reda](https://github.com/Shimaa-reda)
- Asmaa Ahmed
- Tony Issaq
- Mahmoud Farid

## License

This project is licensed under the MIT License - see the LICENSE file for details.
