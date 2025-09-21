import pytest
from src.models.repositories.interfaces.users_repository import UsersRepositoryInterface
from src.controllers.user_creator import UserCreator

# Classe Mock para simular o comportamento do repositório de usuários


class UserRepositoryMock(UsersRepositoryInterface):
    def __init__(self):
        self.select_user_att = {}
        self.insert_user_att = {}

    def select_user(self, person_name: str) -> list:
        self.select_user_att["person_name"] = person_name
        return []

    def insert_user(self, person_name: str, age: int, height: float) -> None:
        self.insert_user_att["person_name"] = person_name
        self.insert_user_att["age"] = age
        self.insert_user_att["height"] = height
        return


class UserRepositoryMockWithError(UsersRepositoryInterface):
    def __init__(self):
        self.select_user_att = {}

    def select_user(self, person_name: str) -> list:
        self.select_user_att["person_name"] = person_name
        return [1, 2, 3]

    def insert_user(self, person_name: str, age: int, height: float) -> None:
        # Simulate error or do nothing
        pass


def test_insert_new_user():
    user_repository = UserRepositoryMock()
    user_creator = UserCreator(user_repository)

    person_name = "my_person_name"
    age = 33
    height = 1.69

    response = user_creator.insert_new_user(person_name, age, height)

    assert user_repository.select_user_att["person_name"] == person_name
    assert isinstance(response, dict)
    assert "type" in response
    assert response["count"] == 1
    assert response["message"] == "Usuário cadastrado com sucesso!"


def test_insert_new_user_with_error():
    user_repository = UserRepositoryMockWithError()
    user_creator = UserCreator(user_repository)

    with pytest.raises(Exception) as exc_info:
        user_creator.insert_new_user("something", 33, 1.11)

    assert str(exc_info.value) == "Usuário já cadastrado!"
