from src import create_app

app = create_app()

with app.app_context():
    from src import routes
    
if __name__ == '__main__':
    app.run(debug=True)