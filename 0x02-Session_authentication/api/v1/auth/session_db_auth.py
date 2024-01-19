#!/usr/bin/env python3
""" Session Authentication Module (Database)
"""
from api.v1.auth.session_auth import SessionAuth
from models.user_session import UserSession


class SessionDBAuth(SessionAuth):
    """ Session Database Authentication Class
    """
    def create_session(self, user_id: str = None) -> str:
        """ Creates a session
        """
        session_id = super().create_session(user_id)
        if session_id:
            session = UserSession(user_id=user_id, session_id=session_id)
            session.save()
            UserSession.save_to_file()
            return session_id
        return None

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ Returns user id based on a session id
        """
        if session_id:
            UserSession.load_from_file()
            session = UserSession.search({'session_id': session_id})
            if session:
                return session[0].user_id
        return None

    def destroy_session(self, request=None):
        """ Deletes the user session / logout
        """
        if request:
            session_id = self.session_cookie(request)
            if session_id:
                session = UserSession.search({'session_id': session_id})
                if session:
                    try:
                        session[0].remove()
                        UserSession.save_to_file()
                        return True
                    except Exception:
                        return False
        return False
