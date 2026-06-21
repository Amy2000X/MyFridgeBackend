from deep_translator import GoogleTranslator

# Words that are often translated incorrectly or have multiple meanings
CUSTOM_TRANSLATIONS = {
    "kipfilet": "chicken",
    "malse kipfilet": "chicken",
    "kipdijfilet": "chicken",
    "gehakt": "ground beef",
    "rundergehakt": "ground beef",
    "half om half gehakt": "mixed minced meat",
    "ui": "onion",
    "rode ui": "red onion",
    "lente ui": "spring onion",
    "aardappel": "potato",
    "cherrytomaten": "cherry tomato",
    "parmezaanse kaas": "parmesan cheese",
}


def translate(text: str) -> str:

    text = text.lower().strip()

    if text in CUSTOM_TRANSLATIONS:
        return CUSTOM_TRANSLATIONS[text]

    try:
        return GoogleTranslator(
            source="nl",
            target="en"
        ).translate(text).lower()

    except Exception:
        return text.lower()