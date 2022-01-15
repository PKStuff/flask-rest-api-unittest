from flask_app import db

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"{self.id}--{self.name}"
