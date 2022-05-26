import requests, random
from flask import Flask, render_template, request, send_file

def generate_random_letters() -> str:
    letters = ""
    for i in range(33, 127):
        letters += chr(i)
    random_letters = random.choices(letters, k=5)
    random_letters = "".join(random_letters)
    random_letters
    return random_letters

encodeMap = {}
decodeMap = {}

def encodeURL(longURL: str) -> str:
    if longURL not in encodeMap:
        short_url = generate_random_letters()
        while short_url in encodeMap.values():
            short_url = generate_random_letters()
        shortURL = "http://gangatinyURL.com/" + short_url
        encodeMap[longURL] = shortURL
        decodeMap[shortURL] = longURL
    return encodeMap[longURL]

app = Flask(__name__)


@app.route("/")
def home_page():
    return render_template("urlshortner.html")


@app.route("/send", methods=["POST"])
def URL_Shortner():
    full_link = request.form.get("full_link")
    short_link = encodeURL(full_link)

    return render_template("urlshortner.html", short_url=short_link, full_url = full_link)


if __name__ == "__main__":
    app.run(debug = True)
