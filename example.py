from kai_sdk_python_kaistudio.index import KaiStudioBackApi, KaiStudioCredentials

credentials = KaiStudioCredentials(
    token="your bearer token",
    # host="https://your-server/"  # optional, defaults to https://back.kai-studio.ai
)

api = KaiStudioBackApi(credentials)

# Core — user management
user = api.core().user()

# Studio — instance, knowledge base, organization management
instance = api.studio().instance()
knowledge_base = api.studio().knowledge_base()
organization = api.studio().organization()

# Global admin
global_admin = api.global_admin()
