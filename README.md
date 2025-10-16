# Pth Prime Finder

## Summary

This is a minimal, working application designed to find the *p*-th prime number. It includes a command-line interface (CLI) written in Python and an interactive web interface (HTML with JavaScript). Both components implement an efficient algorithm to calculate the desired prime number.

## Setup

### Prerequisites

- Python 3.x (for the command-line script)
- A modern web browser (for the web interface)

### Installation

1.  **Download the files.**
    Save `main.py` and `index.html` to a local directory.

2.  **No further installation is required.** The Python script uses only standard libraries, and the HTML file is self-contained.

## Usage

### Command-Line Interface (CLI)

To find the *p*-th prime using the Python script, run `main.py` from your terminal, passing the integer *p* as an argument.

**Syntax:**
```bash
python main.py <p>
```

**Example:** To find the 10th prime number:
```bash
python main.py 10
```
**Output:**
```
The 10th prime number is: 29
```

### Web Interface

1.  Open the `index.html` file in your web browser.
2.  Enter a positive integer into the input field.
3.  Click the "Calculate" button.
4.  The result will be displayed below the form. The interface will show a "Calculating..." message for larger numbers.

## Code Explanation

### `main.py` (Python CLI)

-   **`is_prime(n)`**: This function checks if a given number `n` is prime. It uses an optimized trial division method, only checking divisors up to the square root of `n` and skipping multiples of 2 and 3.
-   **`find_pth_prime(p)`**: This function iterates through numbers, uses `is_prime()` to identify primes, and stops once it has found the *p*-th one.
-   **Main Block (`if __name__ == "__main__":`)**: This part of the script handles command-line arguments. It parses the input, validates that it's a positive integer, calls `find_pth_prime()`, and prints the result to the console.

### `index.html` (Web Interface)

-   **HTML**: The file contains a simple form with a number input field and a submit button. A `div` with the id `result` is used to display the output.
-   **CSS**: Basic inline CSS is used to style the page for better readability and user experience.
-   **JavaScript**: An event listener is attached to the form's `submit` event. The `isPrime` and `findPthPrime` functions are JavaScript implementations of the same logic found in the Python script. When the user submits a number, the script validates the input, displays a "Calculating..." message, and then computes the prime number. Using `setTimeout` ensures the UI updates before starting a potentially long calculation.

## License

This project is licensed under the MIT License.

```
MIT License

Copyright (c) 2024 The Developer

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
```
