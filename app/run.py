from seeker import create_app

app = create_app(True, True)

if __name__ == '__main__':
    app.run(debug=True)
