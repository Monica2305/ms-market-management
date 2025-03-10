# user_service.py (Service)
from Infrastructure.Models.user import UserModel
from Infrastructure.http.whats_app import send_whatsapp_message

def create_user(db_session, user_data):
    user = UserModel(**user_data)
    db_session.add(user)
    db_session.commit()