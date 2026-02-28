from .models import db, User

class UserRepository:
    def get_all(self):
        return db.session.query(User).all()

    def get_by_id(self, user_id):
        return db.session.get(User, user_id)

    def create(self, name, email):
        user = User(name=name, email=email)
        db.session.add(user)
        db.session.commit()
        return user

    def update(self, user_id, name, email):
        user = self.get_by_id(user_id)
        if user:
            if name is not None:
                user.name = name
            if email is not None:
                user.email = email
            
        db.session.commit()
        db.session.refresh(user)
        return user

    def delete(self, user_id):
        user = self.get_by_id(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return True
        return False