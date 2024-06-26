# Documentation for the Anki Card Adder Script

## Overview

This script allows users to add words to Anki by pressing `Ctrl+C+C`. It retrieves the word from the clipboard, fetches its translation using the Reverso API, and adds it to Anki using the AnkiConnect API.

## Dependencies

The script relies on several Python packages and custom modules:

- `time`: Standard Python module for time-related functions.
- `pyperclip`: A cross-platform clipboard module to get the copied text.
- `keyboard`: A module for keyboard event handling.
- `utils.anki`: A custom module assumed to contain a function `add_card_to_anki` for adding cards to Anki.
- `utils.reverso`: A custom module assumed to contain a function `get_translation` for fetching translations from Reverso.

## Installation

Before running the script, ensure you have the required packages installed. You can install them using `pip`:

```bash
pip install pyperclip keyboard
```

Ensure that the custom modules `utils.anki` and `utils.reverso` are available in your Python path.

## Usage

1. **Run the Script**: Execute the script in your Python environment.
2. **Copy a Word**: Copy a word to your clipboard.
3. **Press `Ctrl+C+C`**: Press `Ctrl+C+C` to trigger the script.
4. **Check Output**: The script will fetch the translation and add the word to Anki, printing the status in the console.

Ensure these functions are implemented correctly in their respective modules.

## Conclusion

- This script provides a simple and efficient way to add words to Anki using the clipboard and keyboard shortcuts. Ensure all dependencies are installed and custom modules are correctly implemented for smooth operation.
- Make sure that the Anki app is runing  and the Reverso app too at your Pc.