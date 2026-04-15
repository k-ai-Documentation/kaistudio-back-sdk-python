import json
from typing import List, Dict, Any, Optional
import httpx


class InstanceModule:
    def __init__(self, base_url: str, headers: dict):
        self.__base_url = base_url.rstrip('/') + '/studio/instance'
        self.__headers = headers

    async def create(self, organization_id: str, name: str):
        async with httpx.AsyncClient(verify=False, timeout=None) as client:
            response = await client.post(f"{self.__base_url}/create", headers=self.__headers,
                                         json={"organization_id": organization_id, "name": name})
            return response.json()['response'] if response.status_code == 200 else response.text

    async def get(self, instance_id: str) -> dict:
        async with httpx.AsyncClient(verify=False, timeout=None) as client:
            response = await client.post(f"{self.__base_url}/get-instance", headers=self.__headers,
                                         json={"instance_id": instance_id})
            return response.json()['response'] if response.status_code == 200 else response.text

    async def get_detail(self, instance_id: str) -> dict:
        async with httpx.AsyncClient(verify=False, timeout=None) as client:
            response = await client.post(f"{self.__base_url}/get-instance-detail", headers=self.__headers,
                                         json={"instance_id": instance_id})
            return response.json()['response'] if response.status_code == 200 else response.text

    async def update_name(self, instance_id: str, name: str) -> bool:
        async with httpx.AsyncClient(verify=False, timeout=None) as client:
            response = await client.post(f"{self.__base_url}/update-name", headers=self.__headers,
                                         json={"instance_id": instance_id, "name": name})
            return response.json()['response'] if response.status_code == 200 else response.text

    async def set_scenarios(self, instance_id: str, scenarios: List[str]) -> bool:
        async with httpx.AsyncClient(verify=False, timeout=None) as client:
            response = await client.post(f"{self.__base_url}/set-scenarios", headers=self.__headers,
                                         json={"instance_id": instance_id, "scenarios": scenarios})
            return response.json()['response'] if response.status_code == 200 else response.text

    async def delete(self, instance_id: str) -> bool:
        async with httpx.AsyncClient(verify=False, timeout=None) as client:
            response = await client.post(f"{self.__base_url}/delete", headers=self.__headers,
                                         json={"instance_id": instance_id})
            return response.json()['response'] if response.status_code == 200 else response.text

    async def deploy(self, instance_id: str) -> bool:
        async with httpx.AsyncClient(verify=False, timeout=None) as client:
            response = await client.post(f"{self.__base_url}/deploy", headers=self.__headers,
                                         json={"instance_id": instance_id})
            return response.json()['response'] if response.status_code == 200 else response.text

    async def generate_api_key(self, instance_id: str) -> str:
        async with httpx.AsyncClient(verify=False, timeout=None) as client:
            response = await client.post(f"{self.__base_url}/generate-apikey", headers=self.__headers,
                                         json={"instance_id": instance_id})
            return response.json()['response'] if response.status_code == 200 else response.text

    async def add_kb(self, instance_id: str, type: str, options: Dict[str, Any],
                     search_goal: Optional[Dict[str, str]] = None) -> bool:
        async with httpx.AsyncClient(verify=False, timeout=None) as client:
            response = await client.post(f"{self.__base_url}/add-kb", headers=self.__headers,
                                         json={"instance_id": instance_id, "type": type,
                                               "options": options, "search_goal": search_goal})
            return response.json()['response'] if response.status_code == 200 else response.text

    async def update_kb(self, id: str, instance_id: str, type: str, options: Dict[str, Any],
                        search_goal: Optional[Dict[str, str]] = None) -> bool:
        async with httpx.AsyncClient(verify=False, timeout=None) as client:
            response = await client.post(f"{self.__base_url}/update-kb", headers=self.__headers,
                                         json={"id": id, "instance_id": instance_id, "type": type,
                                               "options": options, "search_goal": search_goal})
            return response.json()['response'] if response.status_code == 200 else response.text

    async def list_kb(self, instance_id: str) -> list:
        async with httpx.AsyncClient(verify=False, timeout=None) as client:
            response = await client.post(f"{self.__base_url}/list-kb", headers=self.__headers,
                                         json={"instance_id": instance_id})
            return response.json()['response'] if response.status_code == 200 else response.text

    async def delete_kb(self, id: str, instance_id: str) -> bool:
        async with httpx.AsyncClient(verify=False, timeout=None) as client:
            response = await client.post(f"{self.__base_url}/delete-kb", headers=self.__headers,
                                         json={"id": id, "instance_id": instance_id})
            return response.json()['response'] if response.status_code == 200 else response.text

    async def grant_user_access_demo(self, instance_id: str, user_id: str) -> dict:
        async with httpx.AsyncClient(verify=False, timeout=None) as client:
            response = await client.post(f"{self.__base_url}/grant-user-access-demo", headers=self.__headers,
                                         json={"instance_id": instance_id, "user_id": user_id})
            return response.json()['response'] if response.status_code == 200 else response.text

    async def revoke_user_access_demo(self, instance_id: str, user_id: str) -> bool:
        async with httpx.AsyncClient(verify=False, timeout=None) as client:
            response = await client.post(f"{self.__base_url}/revoke-user-access-demo", headers=self.__headers,
                                         json={"instance_id": instance_id, "user_id": user_id})
            return response.json()['response'] if response.status_code == 200 else response.text

    async def get_all_users_access_demo(self, instance_id: str) -> list:
        async with httpx.AsyncClient(verify=False, timeout=None) as client:
            response = await client.post(f"{self.__base_url}/get-all-user-access-demo", headers=self.__headers,
                                         json={"instance_id": instance_id})
            return response.json()['response'] if response.status_code == 200 else response.text

    async def update_detail(self, instance_id: str, name: str, extra_properties: dict,
                            logo_file: Optional[bytes] = None) -> bool:
        async with httpx.AsyncClient(verify=False, timeout=None) as client:
            data = {
                "instance_id": instance_id,
                "name": name,
                "extraproperties": json.dumps(extra_properties)
            }
            files = {"logo": ("logo.svg", logo_file, "image/svg+xml")} if logo_file else None
            response = await client.post(f"{self.__base_url}/update-instance-detail",
                                         headers=self.__headers, data=data, files=files)
            return response.json()['response'] if response.status_code == 200 else response.text
