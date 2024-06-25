import requests

ANKI_CONNECT_URL = 'http://localhost:8765'

def add_card_to_anki(word, translation):
    payload = {
        "action": "addNote",
        "version": 6,
        "params": {
            "note": {
                "deckName": "Dev",
                "modelName": "Basic",
                "fields": {
                    "Front": word,
                    "Back": translation
                },
                "tags": []
            }
        }
    }
    response = requests.post(ANKI_CONNECT_URL, json=payload)
    return response.json()