# Blue Button Application

## Summary

This is a minimal, full-stack web application that demonstrates a simple interactive form. The main feature, as per the user request, is a submit button styled with a blue background color. The application is built with a Python Flask backend to serve the HTML and a vanilla JavaScript frontend to handle user interaction.

## Setup

Follow these steps to set up and run the application locally.

1.  **Prerequisites**:
    *   Python 3.x installed.
    *   `pip` (Python package installer) available.

2.  **Download the files**:
    Place `main.py` and `index.html` in the same directory.

3.  **Install dependencies**:
    This application requires the Flask library. Install it using pip:
    ```bash
    pip install Flask
    ```

4.  **Run the application**:
    Execute the Python script from your terminal:
    ```bash
    python main.py
    ```

5.  **Access the application**:
    You will see output indicating the server is running, usually on `http://127.0.0.1:8080`. Open this URL in your web browser.

## Usage

1.  Open your web browser and navigate to the URL where the application is running (e.g., `http://127.0.0.1:8080`).
2.  You will see a title, a text input field, and a blue "Submit" button.
3.  Enter any text into the input field.
4.  Click the blue "Submit" button.
5.  The text you entered will be displayed below the form without the page reloading.

## Code Explanation

### `main.py`
This file contains the backend server code using the Flask framework.
-   It imports `Flask` and `render_template`.
-   It creates a Flask application instance.
-   It defines a single route `/` which, when accessed, serves the `index.html` file to the client.
-   The `if __name__ == '__main__':` block ensures the server only runs when the script is executed directly.

### `index.html`
This file contains the structure, styling, and client-side logic for the web page.
-   **HTML**: Defines the basic page structure, including a `<h1>` title, a `<form>`, an `<input>` field, a `<button>`, and a `div` with the id `result` to display output.
-   **CSS**: Contained within a `<style>` block. It provides basic styling for the page. The key rule is `button { background-color: blue; }`, which fulfills the primary requirement.
-   **JavaScript**: Contained within a `<script>` block.
    -   It adds an event listener to the form's `submit` event.
    -   `event.preventDefault()` is called to stop the browser from reloading the page on form submission.
    -   It retrieves the value from the text input field and updates the `textContent` of the `result` div to display the user's input.

## License

This project is licensed under the MIT License.

---
**MIT License**

Copyright (c) 2024

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
