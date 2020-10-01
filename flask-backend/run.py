from api.utils.factory import create_app

if __name__ == "__main__":
    app = create_app("api.utils.config")
    app.run(debug=True)
