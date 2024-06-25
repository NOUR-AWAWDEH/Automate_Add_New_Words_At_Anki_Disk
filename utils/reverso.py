from reverso_api.context import ReversoContextAPI

def get_translation(word):
    try:
        # Create an instance of the ReversoContextAPI with the source and target languages
        reverso = ReversoContextAPI(word, "", "ru", "en")
        translations = list(reverso.get_translations())
        if translations:
            return translations[0].translation  # Adjust based on the actual structure of translation object
        else:
            return None
    except Exception as e:
        print(f"Error fetching translation: {e}")
        return None