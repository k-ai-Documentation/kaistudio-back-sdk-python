from typing import Optional
import httpx


class UserModule:
    def __init__(self, base_url: str, headers: dict):
        self.__base_url = base_url.rstrip('/') + '/core/user'
        self.__headers = headers

    async def get_info(self) -> dict:
        async with httpx.AsyncClient(verify=False, timeout=None) as client:
            response = await client.post(f"{self.__base_url}/info", headers=self.__headers)
            return response.json()['response'] if response.status_code == 200 else response.text

    async def add_user(self, name: str, email: str, organization_id: str) -> dict:
        async with httpx.AsyncClient(verify=False, timeout=None) as client:
            response = await client.post(f"{self.__base_url}/add-user", headers=self.__headers,
                                         json={"name": name, "email": email, "organization_id": organization_id})
            return response.json()['response'] if response.status_code == 200 else response.text

    async def update_user(self, id: str, name: str, email: str, organization_id: str) -> dict:
        async with httpx.AsyncClient(verify=False, timeout=None) as client:
            response = await client.post(f"{self.__base_url}/update-user", headers=self.__headers,
                                         json={"id": id, "name": name, "email": email,
                                               "organization_id": organization_id})
            return response.json()['response'] if response.status_code == 200 else response.text

    async def delete_user(self, id: str, organization_id: str) -> bool:
        async with httpx.AsyncClient(verify=False, timeout=None) as client:
            response = await client.post(f"{self.__base_url}/delete-user", headers=self.__headers,
                                         json={"id": id, "organization_id": organization_id})
            return response.json()['response'] if response.status_code == 200 else response.text

    async def update_password(self, id: str, password: str) -> bool:
        async with httpx.AsyncClient(verify=False, timeout=None) as client:
            response = await client.post(f"{self.__base_url}/update-password", headers=self.__headers,
                                         json={"id": id, "password": password})
            return response.json()['response'] if response.status_code == 200 else response.text

    async def set_user_admin(self, id: str, is_global_admin: Optional[bool] = False,
                             organization_id: Optional[str] = None) -> bool:
        async with httpx.AsyncClient(verify=False, timeout=None) as client:
            response = await client.post(f"{self.__base_url}/set-user-admin", headers=self.__headers,
                                         json={"id": id, "is_global_admin": is_global_admin,
                                               "organization_id": organization_id})
            return response.json()['response'] if response.status_code == 200 else response.text
