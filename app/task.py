from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Task (db.Model):
    
    id = db.Column("id", db.Integer, primary_key=True)
    task = db.Column("task", db.String(100), nullable = False)
    status = db.Column("status", db.Boolean, default = False)

    def __repr__(self):
        return f"Task {self.id}: {self.task}"