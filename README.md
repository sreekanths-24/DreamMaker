# DreamMaker

DreamMaker is a web application designed to help users manage their dreams, goals, todos, and events in an organized manner. With DreamMaker, users can set and track their dreams, create todos associated with their dreams, and manage events relevant to their goals.

## Features

- **Dream Management**: Users can create, view, update, and delete their dreams or short-term goals.
- **Todo Management**: Users can create, view, update, and delete todos associated with their dreams, helping them stay organized and focused on achieving their goals.
- **Event Management**: Users can manage events relevant to their dreams, such as deadlines, meetings, or milestones.
- **User Authentication**: Secure user authentication system using Django's built-in authentication framework.

## Technologies Used

- **Django**: Backend web framework for building the DreamMaker application.
- **HTML/CSS/JavaScript**: Frontend development for creating user interfaces and interactivity.
- **SQLite**: Default database used by Django for data storage and retrieval.
- **Bootstrap**: Frontend framework for responsive and mobile-friendly design.
- **Font Awesome**: Icon toolkit used for adding scalable vector icons to the user interface.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/sreekanths-24/DreamMaker.git
   ```

2. Navigate to the project directory:

   ```bash
   cd DreamMaker
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:

   ```bash
   python manage.py migrate
   ```

5. Start the development server:

   ```bash
   python manage.py runserver
   ```

6. Access the application at [http://localhost:8000](http://localhost:8000) in your web browser.

## Usage

- **Create Account**: Sign up for a new account or log in if you already have one.
- **Dashboard**: View and manage your dreams, todos, and events from the dashboard.
- **Dreams**: Add, edit, and delete dreams or short-term goals.
- **Todos**: Create, update, and delete todos associated with your dreams.
- **Events**: Manage events relevant to your dreams, such as deadlines or milestones.

## Contributing

Contributions to DreamMaker are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
