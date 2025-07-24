from .modules.FileInstance import FileInstance
from .modules.ManageInstance import ManageInstance
from .modules.KaiStudioCredentials import KaiStudioCredentials

class KaiStudio:
    __file__: FileInstance
    def __init__(self, credentials: KaiStudioCredentials):
        self.__credentials = credentials

        if self.__credentials.instance_id and self.__credentials.api_key:
            headers = {
                'api-key': self.__credentials.api_key,
                'instance-id': self.__credentials.instance_id,
                'organization-id': self.__credentials.organization_id
            }

            base_url: str = "https://api.kai-studio.ai/"

            if self.__credentials.host:
                base_url = self.__credentials.host
                if self.__credentials.api_key:
                    headers = {
                        'api-key': self.__credentials.api_key
                    }
            self.__file = FileInstance(headers=headers, base_url=base_url)
            self.__manage_instance = ManageInstance(headers=headers, base_url=base_url)

    def get_credentials(self) -> KaiStudioCredentials:
        return self.__manage_instance

    def file_manager(self) -> FileInstance:
        return self.__file