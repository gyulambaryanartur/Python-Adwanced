from flask import Flask, render_template, request, abort
import hashlib
import json


salt = ''
users = json.load(open('users'))
with open('salt') as salt_file:
    salt = salt_file.read()


app = Flask(__name__)

def is_json_key_present(json, key):
    try:
        buf = json[key]
    except KeyError:
        return False

    return True

@app.route("/")
def index():
    return render_template("index.html")
@app.route('/persons')
def persons_route():
    persons = json.load(open('persons.json'))

    return render_template('persons.html', data=persons)



@app.route('/login')
def login_page():
    return render_template('login.html')
@app.route('/register')
def register_page():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register_logic():
    username = request.form.get('username')
    password = request.form.get('psw')
    passwordrp = request.form.get('psw-repeat')
    if password!=passwordrp:
        return abort(400)

        #stored_username = userread.get(username)
    if is_json_key_present(users,username):
         
         return abort(409)
    with open('users', mode='w', encoding='utf-8') as user:
        
        #user=json.load(open('users'))
        
        password=hashlib.sha256(f"{password}{salt}".encode()).hexdigest()
        users[username]=password
        json.dump(users,user)

    return f'User registerd succesfully |'

@app.route('/login', methods=['POST'])
def login_logic():

    username = request.form.get('username')
    password = request.form.get('password')

    stored_password = users.get(username)

    if stored_password == None:
        return abort(401)

    pass_hash = hashlib.sha256(f"{password}{salt}".encode()).hexdigest()

    if pass_hash != stored_password:

        
        
        return abort(401)

    return 'You\'re Welcome!'


if __name__ == '__main__':
    app.run(host='localhost', port=8000, debug=True)
