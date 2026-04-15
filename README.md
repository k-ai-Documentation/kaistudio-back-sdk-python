# sdk-python-kaistudio

Python SDK for the [KAI Studio](https://kai-studio.ai) Back API. Mirrors the structure of the official JS SDK (`kaistudio-back-sdk-js`).

## Installation

```bash
pip install git+https://github.com/k-ai-Documentation/kaistudio-back-sdk-python.git
```

For local development:

```bash
pip install -e .
```

## Quick Start

```python
import asyncio
from kaistudio_back_sdk.index import KaiStudioBackApi, KaiStudioCredentials

credentials = KaiStudioCredentials(
    token="your-bearer-token",
    # host="https://your-server/"  # optional, defaults to https://back.kai-studio.ai
)

api = KaiStudioBackApi(credentials)

async def main():
    user = api.core().user()
    print(await user.get_info())

asyncio.run(main())
```

> All API methods are `async` and must be called with `await`.

## Module Overview

```
api.core().user()               # User management
api.studio().instance()         # Instance management
api.studio().knowledge_base()   # Knowledge base utilities
api.studio().organization()     # Organization management
api.global_admin()              # Global admin operations
```

---

## `api.core().user()`

| Method | Parameters | Description |
|---|---|---|
| `get_info` | — | Get authenticated user info |
| `add_user` | `name, email, organization_id` | Create a user and send a welcome email |
| `update_user` | `id, name, email, organization_id` | Update user details |
| `delete_user` | `id, organization_id` | Delete a user |
| `update_password` | `id, password` | Update a user's password |
| `set_user_admin` | `id, is_global_admin, organization_id` | Grant or revoke admin status |

```python
user = api.core().user()
info = await user.get_info()
result = await user.add_user(name="Jane Doe", email="jane@example.com", organization_id="org-123")
```

---

## `api.studio().instance()`

| Method | Parameters | Description |
|---|---|---|
| `create` | `organization_id, name` | Create a new instance |
| `get` | `instance_id` | Get instance configuration |
| `get_detail` | `instance_id` | Get instance detail (name, logo, extra properties) |
| `update_name` | `instance_id, name` | Rename an instance |
| `set_scenarios` | `instance_id, scenarios` | Set scenarios (`AUDIT`, `SEARCH`, `DOCUMENT_COMPANION`) |
| `delete` | `instance_id` | Delete an instance |
| `deploy` | `instance_id` | Deploy an instance |
| `generate_api_key` | `instance_id` | Generate a new API key |
| `add_kb` | `instance_id, type, options, search_goal` | Add a knowledge base |
| `update_kb` | `id, instance_id, type, options, search_goal` | Update a knowledge base |
| `list_kb` | `instance_id` | List knowledge bases |
| `delete_kb` | `id, instance_id` | Remove a knowledge base |
| `grant_user_access_demo` | `instance_id, user_id` | Grant demo access to a user |
| `revoke_user_access_demo` | `instance_id, user_id` | Revoke demo access from a user |
| `get_all_users_access_demo` | `instance_id` | List users with demo access |
| `update_detail` | `instance_id, name, extra_properties, logo_file` | Update instance detail (`logo_file` is SVG bytes) |

```python
instance = api.studio().instance()
config = await instance.get(instance_id="inst-123")
kbs = await instance.list_kb(instance_id="inst-123")
```

---

## `api.studio().knowledge_base()`

| Method | Parameters | Description |
|---|---|---|
| `list_available_kb_type` | — | List all available KB types |
| `get_credentials_for_by_type` | `kb_type` | Get the required credentials schema for a KB type |
| `get_kb_type_from_internal_type` | `kb_type` | Resolve an internal KB type to its display type |

---

## `api.studio().organization()`

| Method | Parameters | Description |
|---|---|---|
| `list` | — | List organizations for the authenticated user |
| `create` | `name` | Create an organization (global admin only) |
| `change_name` | `organization_id, name` | Rename an organization |
| `add_user` | `organization_id, user_id, is_admin` | Add a user to an organization |
| `update_user` | `organization_id, user_id, is_admin` | Update a user's admin status |
| `remove_user` | `organization_id, user_id` | Remove a user from an organization |
| `list_users` | `organization_id` | List users in an organization |
| `list_instances` | `organization_id` | List instances in an organization |
| `is_admin` | `organization_id, user_id` | Check if a user is an admin |
| `grant_user_can_access_kaistudio` | `organization_id, user_id` | Grant KAI Studio access |
| `revoke_user_can_access_kaistudio` | `organization_id, user_id` | Revoke KAI Studio access |
| `user_can_access_kaistudio` | `organization_id, user_id` | Check if a user has KAI Studio access |

---

## `api.global_admin()`

> Requires global admin role.

| Method | Parameters | Description |
|---|---|---|
| `list_users` | `offset, limit` | List all users (paginated) |
| `list_apps` | — | List all apps |
| `list_apps_for_user` | `user_id` | List apps assigned to a user |
| `add_app_for_user` | `user_id, app_id` | Assign an app to a user |
| `remove_app_for_user` | `user_id, app_id` | Remove an app from a user |
| `toggle_user_active` | `user_id` | Toggle a user's active status |

```python
admin = api.global_admin()
users = await admin.list_users(offset=0, limit=20)
```

---

## Contributing

- bxu@k-ai.ai
- rmei@k-ai.ai
- sngo@k-ai.ai
