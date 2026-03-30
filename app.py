from flask import Flask

app = Flask(__name__)

@app.route('/')
def display_info():
    # Display Name and AppID
    name = "Prathamesh Bhandare"
    app_id = "2408654"
    return f"Name: {name}<br>AppID: {app_id}"

@app.route('/hobbies')
def display_hobbies():
    # Display hobbies
    name = "Prathamesh Bhandare"
    hobbies = ["Reading", "Coding", "Traveling", "Photography"]
    hobbies_list = "<br>".join(hobbies)
    return f"Name: {name}<br>Hobbies:<br>{hobbies_list}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)