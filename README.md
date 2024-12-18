# Pygame GUI Applications

This repository contains multiple Pygame-based applications with GUI built using `pygame_gui`. Below are examples of different applications such as a simple notepad, a calculator, and an interactive terminal.

## 1. Notepad

This is a basic text entry box that functions as a simple notepad. It supports resizing and dynamically adjusts the layout when the window is resized. The text box takes up most of the screen and allows for typing and editing.

### Features:
- Resizable window.
- Full-screen text input area.
- Automatically adjusts the layout when resized.

## 2. Calculator

This application is a simple calculator that can evaluate mathematical expressions. It uses the `sympy` library to provide high-precision calculations and displays the result on the screen.

### Features:
- Input area for mathematical expressions.
- "Calculate" button to evaluate the expression.
- Error handling for invalid expressions.
- Result displayed on the screen.

## 3. Interactive Terminal

This application simulates a terminal where you can enter Python code and get the results in real-time. It uses the `code` module to interpret and execute Python code, and displays the results directly in a text area.

### Features:
- Input field for entering Python code.
- Display output from the executed code.
- Resizable window with dynamically adjusted UI components.
- Error handling and debugging information.

## Requirements

- `pygame` for GUI.
- `pygame_gui` for UI management.
- `sympy` (for the Calculator application).

## Installation

To install the required libraries, run:

```bash
pip install pygame pygame_gui sympy
```

## Usage

- Run the script for each application to launch the respective GUI.
- In the Notepad, type and edit text.
- In the Calculator, input expressions and click "Calculate".
- In the Terminal, input Python code and see the result.

## License

This project is licensed under the MIT License.
