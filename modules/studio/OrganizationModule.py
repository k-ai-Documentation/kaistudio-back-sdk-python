from typing import List
import httpx


class OrganizationModule:
    def __init__(self, base_url: str, headers: dict):
        self.__base_url = base_url.rstrip('/') + '/studio/organization'
        self.__headers = headers

    async def list(self) -> List[dict]:
        async with httpx.AsyncClient(verify=False, timeout=None) as client:
            response = await client.post(f"{self.__base_url}/list", headers=self.__headers)
            return response.json()['response'] if response.status_code == 200 else response.text

    async def create(self, name: str) -> dict:
        async with httpx.AsyncClient(verify=False, timeout=None) as client:
            response = await client.post(f"{self.__base_url}/create", headers=self.__headers,
                                         json={"name": name})
            return response.json()['response'] if response.status_code == 200 else response.text

    async def add_user(self, organization_id: str, user_id: str, is_admin: bool = False):
        async with httpx.AsyncClient(verify=False, timeout=None) as client:
            response = await client.post(f"{self.__base_url}/add-user", headers=self.__headers,
                                         json={"organization_id": organization_id, "user_id": user_id,
                                               "is_admin": is_admin})
            return response.json()['response'] if response.status_code == 200 else response.text

    async def update_user(self, organization_id: str, user_id: str, is_admin: bool = False):
        async with httpx.AsyncClient(verify=False, timeout=None) as client:
            response = await client.post(f"{self.__base_url}/update-user", headers=self.__headers,
                                         json={"organization_id": organization_id, "user_id": user_id,
                                               "is_admin": is_admin})
            return response.json()['response'] if response.status_code == 200 else response.text

    async def remove_user(self, organization_id: str, user_id: str):
        async with httpx.AsyncClient(verify=False, timeout=None) as client:
            response = await client.post(f"{self.__base_url}/remove-user", headers=self.__headers,
                                         json={"organization_id": organization_id, "user_id": user_id})
            return response.json()['response'] if response.status_code == 200 else response.text

    async def list_users(self, organization_id: str) -> List[dict]:
        async with httpx.AsyncClient(verify=False, timeout=None) as client:
            response = await client.post(f"{self.__base_url}/list-user", headers=self.__headers,
                                         json={"organization_id": organization_id})
            return response.json()['response'] if response.status_code == 200 else response.text

    async def change_name(self, organization_id: str, name: str):
        async with httpx.AsyncClient(verify=False, timeout=None) as client:
            response = await client.post(f"{self.__base_url}/change-name", headers=self.__headers,
                                         json={"organization_id": organization_id, "name": name})
            return response.json()['response'] if response.status_code == 200 else response.text

    async def list_instances(self, organization_id: str) -> List[dict]:
        async with httpx.AsyncClient(verify=False, timeout=None) as client:
            response = await client.post(f"{self.__base_url}/list-instances", headers=self.__headers,
                                         json={"organization_id": organization_id})
            return response.json()['response'] if response.status_code == 200 else response.text

    async def is_admin(self, organization_id: str, user_id: str) -> bool:
        async with httpx.AsyncClient(verify=False, timeout=None) as client:
            response = await client.post(f"{self.__base_url}/is-admin", headers=self.__headers,
                                         json={"organization_id": organization_id, "user_id": user_id})
            return response.json()['response'] if response.status_code == 200 else response.text

    async def grant_user_can_access_kaistudio(self, organization_id: str, user_id: str):
        async with httpx.AsyncClient(verify=False, timeout=None) as client:
            response = await client.post(f"{self.__base_url}/grant-user-can-access-kaistudio",
                                         headers=self.__headers,
                                         json={"organization_id": organization_id, "user_id": user_id})
            return response.json()['response'] if response.status_code == 200 else response.text

    async def revoke_user_can_access_kaistudio(self, organization_id: str, user_id: str):
        async with httpx.AsyncClient(verify=False, timeout=None) as client:
            response = await client.post(f"{self.__base_url}/revoke-user-can-access-kaistudio",
                                         headers=self.__headers,
                                         json={"organization_id": organization_id, "user_id": user_id})
            return response.json()['response'] if response.status_code == 200 else response.text

    async def user_can_access_kaistudio(self, organization_id: str, user_id: str) -> dict:
        async with httpx.AsyncClient(verify=False, timeout=None) as client:
            response = await client.post(f"{self.__base_url}/user-can-access-kaistudio", headers=self.__headers,
                                         json={"organization_id": organization_id, "user_id": user_id})
            return response.json()['response'] if response.status_code == 200 else response.text
