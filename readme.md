# AST to JavaScript Parser

This project is a Python-based parser that generates valid JavaScript code from a JSON file representing an Abstract Syntax Tree (AST).

## Features

- **AST → JavaScript Conversion:**
  - Supports literal, binary, and unary expressions.
  - Handles variable declarations and assignments.
  - Processes standard, arrow, and immediately invoked function expressions (IIFE).
  - Generates conditional blocks (`if` statements).

- **Special Cases Handling:**
  - Automatically identifies and properly formats immediately invoked function expressions.
  - Explicitly ignores unsupported or invalid elements.

## Prerequisites

- Python 3.x

## Installation

Clone the repository:

```bash
git clone https://github.com/ptirem/astdesob/ast-to-js-parser.git
cd ast-to-js-parser
```

## Usage

1. **Run the script specifying the path to your AST JSON file:**

```bash
python ast_parser.py path/to/ast.json > output.js
```
or
```bash
python ast_parser.py path/to/ast.json 
```

2. **JavaScript output is printed directly to the terminal:**

```javascript
(() => {
    let d = [1856, 1824, 1776, 1728, 1776, 1728, 1776];
    d = d.map((c) => String.fromCharCode((c >> 4)));
    console.log(d);
})();

function example() {
    console.log("AST to JS!");
}
```

## Project Structure

```
.
├── ast_parser.py       # Main AST to JS parsing script
└── README.md           # Project documentation
```

## Notes

- The current parser does not yet support all possible JavaScript expression types. Contributions to extend its capabilities are welcome.

## Contributing

Pull requests and suggestions for improvements are encouraged. Feel free to open an issue or directly submit your pull request!

## License

This project is distributed under the MIT License. See the `LICENSE` file for more details.
