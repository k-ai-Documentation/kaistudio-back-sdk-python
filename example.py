import asyncio

from kai_sdk_python_kaistudio.index import KaiStudio, KaiStudioCredentials

credentials = KaiStudioCredentials(
    organization_id="your organization id",
    instance_id="your instance id",
    api_key="your api key"
)


file_manager = KaiStudio(credentials).file_manager()

