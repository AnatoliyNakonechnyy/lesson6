from flask import Flask

from routes.about import about_bp
from routes.home import home_bp
from routes.post import post_bp
from routes.users import users_bp

app = Flask(__name__)

app.register_blueprint(post_bp)
app.register_blueprint(about_bp)
app.register_blueprint(home_bp)
app.register_blueprint(users_bp)

if __name__ == "__main__":
    app.run(debug=True)
