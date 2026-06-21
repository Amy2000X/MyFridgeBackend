import re


STOPWORDS = [

    "fresh",

    "large",

    "small",

    "organic",

    "malse",

    "verse",

    "gesneden",

    "fijngesneden",

    "bio"

]


def normalize(text: str):

    text = text.lower()

    text = re.sub(
        r"[^a-zA-Z ]",
        "",
        text
    )

    words = text.split()

    words = [

        word

        for word in words

        if word not in STOPWORDS

    ]

    return " ".join(words)