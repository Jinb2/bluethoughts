from bluethoughts import db


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    keywords = db.Column(db.String(100),nullable=False)
    message = db.Column(db.Text, nullable=False)
    location = db.Column(db.String(100),nullable=False)

    def __repr__(self):
        return f"Post('{self.location}','{self.keywords}','{self.message}')"
