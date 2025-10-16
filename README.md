# Q-th Prime Number Calculator

## Summary

This is a minimal, single-page web application that computes the q-th prime number. A user enters an integer `q`, and the application finds and displays the prime number at that position in the sequence of primes (e.g., for q=1, the result is 2; for q=2, the result is 3).

The entire application is contained within a single `index.html` file, utilizing vanilla JavaScript for the logic and simple CSS for styling.

## Setup

No installation or build process is required. Simply download the `index.html` file and open it in any modern web browser.

## Usage

1.  Open the `index.html` file in your browser.
2.  You will see an input field labeled "Enter a number (q):".
3.  Type a positive integer into the field.
4.  Click the blue "Find Prime" button.
5.  The application will calculate the result and display it below the button.

For large values of `q`, the calculation may take a few moments. The UI will display a "Calculating..." message during this time.

## Code Explanation

### `index.html`

The file contains three main parts: HTML for the structure, CSS for styling, and JavaScript for the functionality.

*   **HTML Structure**: A simple form contains a number input (`<input type="number">`), a submit button (`<button>`), and a `div` element with the ID `result` to display the output.
*   **CSS Styling**: Inline CSS within a `<style>` tag provides basic centering, font settings, and styling for the form elements. As requested, the button has a blue background.
*   **JavaScript Logic**: The core logic is within a `<script>` tag.
    *   **Event Listener**: An event listener is attached to the form's `submit` event. It prevents the default page reload, gets the user's input, and triggers the prime number calculation.
    *   **`findNthPrime(q)`**: This function finds the q-th prime. It starts counting from the number 2 and iterates upwards, using the `isPrime` helper function to check each number. It keeps a count of the primes it has found. When the count matches `q`, it returns the current number.
    *   **`isPrime(num)`**: This is a helper function that determines if a given number is prime. It uses an efficient trial division method, checking for divisibility only up to the square root of the number.
    *   **Responsiveness**: The calculation is wrapped in a `setTimeout(..., 0)` to allow the browser to update the UI with a "Calculating..." message before starting the potentially long-running computation. This prevents the UI from freezing.

## License

This project is licensed under the MIT License.