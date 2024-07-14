from flask import Flask, render_template, request, jsonify
import re
import random

app = Flask(__name__)

response = {
    "hi": ["Hello, how can I help you?"],
    "hello": ["Hello, how can I help you?"],
    "i feel (.*)": ["Why do you feel {}?", "How long have you been feeling {}?"],
    "i am (.*)": ["Why do you say you're {}?", "How long have you been {}?"],
    "i'm (.*)": ["Why are you {}?", "How long have you been {}?"],
    "i (.*)": ["Why do you {}?", "What makes you think you {} me?"],
    "(.*) sorry (.*)": ["There's no need to apologize.", "What are you apologizing for?"],
    "(.*) friend (.*)": ["Tell me more about your friend.", "How do your friends make you feel?"],
    "yes": ["You seem quite sure.", "Ok, but can you elaborate."],
    "no": ["Why not?", "Ok, but can you elaborate a bit?"],
    "(.*)": ["Can you elaborate on that?", "Let's change focus a bit.... tell me about your something which makes your feeling good."],
    "": ["Why do you think that?", "Please tell me more.", "Let's change focus a bit.... tell me about something which makes your feeling good."]
}

def match_response(input_text):
    if input_text.lower() == "bye":
        return "Goodbye!"
    for pattern, response_list in response.items():
        matches = re.match(pattern, input_text.lower())
        if matches:
            chosen_response = random.choice(response_list)
            return chosen_response.format(*matches.groups())
    return "I'm sorry I don't understand what you're saying."

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    user_input = request.form["user_input"]
    response_text = match_response(user_input)
    return jsonify({"response": response_text})

if __name__ == "__main__":
    app.run(debug=True)
