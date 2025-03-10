# route.py
from flask import Flask
from Application.Controllers.user_controller import create_user_controller

app = Flask(__name__)

app.route('/users', methods=['POST'])(create_user_controller)

if __name__ == '__main__':
    app.run(debug=True)