from seeker import create_app

app = create_app(True)

if __name__ == '__main__':
    app.run(debug=True)
