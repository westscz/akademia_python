from app import app


if __name__ == "__main__":
    with app.app_context():
        app.config["DEBUG"] = True
        app.run(host="0.0.0.0")
