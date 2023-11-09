# Flask To-Do List Application

This is a simple Flask To-Do List Application. It allows you to add, delete, and manage tasks.

## Getting Started

These instructions will help you get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.6 or higher
- [Git](https://git-scm.com/)

### Clone the Repository

1. Open your terminal or command prompt.

2. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/yourusername/my_todo_app.git
    ```

3. Change your current working directory to the project folder:

    ```bash
    cd my_todo_app
    ```

### Set Up a Virtual Environment

4. Create a virtual environment:

    - On Windows:

      ```bash
      python -m venv venv
      ```

    - On macOS and Linux:

      ```bash
      python3 -m venv venv
      ```

5. Activate the virtual environment:

    - On Windows:

      ```bash
      venv\Scripts\activate
      ```

    - On macOS and Linux:

      ```bash
      source venv/bin/activate
      ```

### Install Dependencies

6. Install project dependencies:

    ```bash
    pip install -r requirements.txt
    ```

### Create a .env File

7. Create a `.env` file in the project directory and add your secret key:

    ```
    SECRET_KEY=your_secret_key_here
    ```

### Run the Application

8. Start the Flask application:

    ```bash
    flask run
    ```

9. Open your web browser and go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/) to access the To-Do List Application.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
