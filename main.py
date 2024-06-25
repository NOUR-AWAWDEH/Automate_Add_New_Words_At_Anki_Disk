import time
import pyperclip
import keyboard
from utils.anki import add_card_to_anki
from utils.reverso import get_translation

def main():
    print("Press Ctrl+C+C to add a word to Anki...")

    while True:
        if keyboard.is_pressed('ctrl+c+c'):
            time.sleep(0.1)  # Prevent multiple triggers
            word = pyperclip.paste()
            if word:
                print(f"Adding word: {word}")
                translation = get_translation(word)
                if translation:
                    result = add_card_to_anki(word, translation)
                    if result.get('error'):
                        print(f"Error: {result['error']}")
                    else:
                        print(f"Successfully added: {word} - {translation}")
                else:
                    print("Error fetching translation.")
            else:
                print("Clipboard is empty.")
            time.sleep(1)  # Prevent multiple triggers

if __name__ == "__main__":
    main()