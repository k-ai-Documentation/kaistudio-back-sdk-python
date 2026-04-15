from .UserModule import UserModule


class CoreModule:
    def __init__(self, base_url: str, headers: dict):
        self.__user = UserModule(base_url, headers)

    def user(self) -> UserModule:
        return self.__user
