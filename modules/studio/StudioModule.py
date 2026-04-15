from .InstanceModule import InstanceModule
from .KnowledgeBaseModule import KnowledgeBaseModule
from .OrganizationModule import OrganizationModule


class StudioModule:
    def __init__(self, base_url: str, headers: dict):
        self.__instance = InstanceModule(base_url, headers)
        self.__knowledge_base = KnowledgeBaseModule(base_url, headers)
        self.__organization = OrganizationModule(base_url, headers)

    def instance(self) -> InstanceModule:
        return self.__instance

    def knowledge_base(self) -> KnowledgeBaseModule:
        return self.__knowledge_base

    def organization(self) -> OrganizationModule:
        return self.__organization
