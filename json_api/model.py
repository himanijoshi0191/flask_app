from config import db, ma


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self,username,email):
        self.username = username
        self.email  = email

class UserSchema(ma.Schema):
    class Meta:
        model = User
        fields = ('username','email')

