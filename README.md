# Blue Button Application

## Summary

This is a minimal, yet fully functional, full-stack web application built with Python (Flask) and standard web technologies (HTML, CSS, JavaScript). The core requirement of this application is to display a button with a blue background color. The application serves a single page with an interactive form.

## Setup

To run this application locally, you'll need Python and pip installed.

1.  **Create the files:**
    Save the provided `main.py` and `index.html` files in the same directory.

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install dependencies:**
    The only dependency is Flask.
    ```bash
    pip install Flask
    ```

## Usage

1.  **Run the Flask server:**
    ```bash
    python main.py
    ```

2.  **Access the application:**
    Open your web browser and navigate to `http://127.0.0.1:8080`.

You will see a webpage with a title, an input field, and a blue submit button. Enter your name and click the button to see an interactive message displayed on the page.

## Code Explanation

### `main.py`

This file contains the backend code. It uses the Flask framework to create a simple web server.
- It defines a single route `/` which listens for requests to the root URL.
- When a request is received, it renders the `index.html` template and sends it to the client's browser.

### `index.html`

This file contains the frontend structure, styling, and logic.
-   **HTML**: Defines the basic page structure, including a title (`<h1>`), a form (`<form>`), an input field (`<input>`), and a submit button (`<button>`).
-   **CSS**: Embedded within a `<style>` tag, it styles the page elements. The key rule is `.blue-button`, which sets the `background-color` of the button to `blue` and the text `color` to `white`.
-   **JavaScript**: A script at the bottom of the page adds interactivity. It listens for the form's `submit` event, prevents the page from reloading, reads the value from the input field, and displays a personalized greeting in the `<div id="result">`.

## License

This project is licensed under the MIT License.
