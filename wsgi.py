from blog.app import app
from blog.models import User, db

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        debug=True,
    )


@app.cli.command("init-db")
def init_db():
    db.create_all()


@app.cli.command("create-users")
def create_users():
    admin = User(username="admin", is_staff=True)
    james = User(username="aliya")
    db.session.add(admin)
    db.session.add(james)
    db.session.commit()
    print("done! created users")
