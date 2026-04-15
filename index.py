from .modules.KaiStudioCredentials import KaiStudioCredentials
from .modules.core.CoreModule import CoreModule
from .modules.studio.StudioModule import StudioModule
from .modules.global_admin.GlobalAdminModule import GlobalAdminModule


class KaiStudioBackApi:
    def __init__(self, credentials: KaiStudioCredentials):
        base_url = credentials.host if credentials.host else 'https://back.kai-studio.ai'

        headers = {}
        if credentials.token:
            headers['Authorization'] = f'Bearer {credentials.token}'

        self.__credentials = credentials
        self.__core = CoreModule(base_url, headers)
        self.__studio = StudioModule(base_url, headers)
        self.__global_admin = GlobalAdminModule(base_url, headers)

    def get_credentials(self) -> KaiStudioCredentials:
        return self.__credentials

    def core(self) -> CoreModule:
        return self.__core

    def studio(self) -> StudioModule:
        return self.__studio

    def global_admin(self) -> GlobalAdminModule:
        return self.__global_admin
