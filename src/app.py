from flask import Flask
from config import Config
from routes import api

app = Flask(__name__)
app.config.from_object(Config)

# Register routes
app.register_blueprint(api)

if __name__ == '__main__':
    app.run()
