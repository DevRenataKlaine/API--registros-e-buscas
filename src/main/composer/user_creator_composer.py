from src.models.connection.db_connection_handler import DBConnectionHandler
from src.models.repositories.users_repository import UsersRepository
from src.controllers.user_creator import UserCreator
from src.views.user_creator_view import UserCreatorView


def user_creator_composer():
    conn = DBConnectionHandler()
    model = UsersRepository(conn)
    controller = UserCreator(model)
    view = UserCreatorView(controller)
    return view
