import flask
from routes.predict_route import predict_blueprint
app = flask.Flask(__name__)

app.register_blueprint(predict_blueprint, url_prefix="/predict")

if __name__ == "__main__":
    app.run(debug=True)
