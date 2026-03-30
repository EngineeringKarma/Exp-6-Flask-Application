# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def display_info():
    # Display Name and AppID
    name = "Your Name Here"
    app_id = "APP-001"
    return f"Name: {name}<br>AppID: {app_id}"

@app.route('/hobbies')
def display_hobbies():
    # Display hobbies (for testing the pipeline)
    name = "Your Name Here"
    hobbies = ["Reading", "Coding", "Traveling", "Photography"]
    hobbies_list = "<br>".join(hobbies)
    return f"Name: {name}<br>Hobbies:<br>{hobbies_list}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)