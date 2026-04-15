from typing import Optional
import httpx


class GlobalAdminModule:
    def __init__(self, base_url: str, headers: dict):
        self.__base_url = base_url.rstrip('/') + '/global-admin'
        self.__headers = headers

    async def list_users(self, offset: Optional[int] = None, limit: Optional[int] = None) -> list:
        async with httpx.AsyncClient(verify=False, timeout=None) as client:
            response = await client.post(f"{self.__base_url}/list-users", headers=self.__headers,
                                         json={"offset": offset, "limit": limit})
            return response.json()['response'] if response.status_code == 200 else response.text

    async def list_apps(self) -> list:
        async with httpx.AsyncClient(verify=False, timeout=None) as client:
            response = await client.post(f"{self.__base_url}/list-apps", headers=self.__headers)
            return response.json()['response'] if response.status_code == 200 else response.text

    async def list_apps_for_user(self, user_id: str) -> list:
        async with httpx.AsyncClient(verify=False, timeout=None) as client:
            response = await client.post(f"{self.__base_url}/list-apps-for-user", headers=self.__headers,
                                         json={"user_id": user_id})
            return response.json()['response'] if response.status_code == 200 else response.text

    async def add_app_for_user(self, user_id: str, app_id: str) -> bool:
        async with httpx.AsyncClient(verify=False, timeout=None) as client:
            response = await client.post(f"{self.__base_url}/add-app-for-user", headers=self.__headers,
                                         json={"user_id": user_id, "app_id": app_id})
            return response.json()['response'] if response.status_code == 200 else response.text

    async def remove_app_for_user(self, user_id: str, app_id: str) -> bool:
        async with httpx.AsyncClient(verify=False, timeout=None) as client:
            response = await client.post(f"{self.__base_url}/remove-app-for-user", headers=self.__headers,
                                         json={"user_id": user_id, "app_id": app_id})
            return response.json()['response'] if response.status_code == 200 else response.text

    async def toggle_user_active(self, user_id: str) -> bool:
        async with httpx.AsyncClient(verify=False, timeout=None) as client:
            response = await client.post(f"{self.__base_url}/toggle-user-active", headers=self.__headers,
                                         json={"user_id": user_id})
            return response.json()['response'] if response.status_code == 200 else response.text
