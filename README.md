# sdk-python

## Introduction

SDK python kaistudio enables developers to efficiently manage files, instance, perform searches, handle thematic content, and
conduct audits. This toolkit is designed to streamline the integration of complex functionalities into python-based
projects.

## Installation
Install with pip:
```
pip install git+https://github.com/k-ai-Documentation/sdk-python.git@version2.0
```

## Quick start

There are two type of versions: SaaS version and Premise version.

#### SaaS version

SaaS version means you are using the service provided by Kai with cloud service. In this case, you will need 3 keys (
organizationId, instanceId, apiKey) to initialize kaiStudio.

Here's a simple example to get you started with the SDK:

```
from kai_sdk_python_kaistudio.index import KaiStudio, KaiStudioCredentials

credentials = KaiStudioCredentials(
    organization_id="your organization id",
    instance_id="your instance id",
    api_key="your api key"
)

file_manager = KaiStudio(credentials).file_manager()
print("LIST FILES:")
print(await file_manager.list_files())

```

#### Premise version

Premise version means you are using the service in your local server in your enterprise. In this case, you will need
host and api key (optional) to initialize kaiStudio.

Here's a simple example to get you started with the SDK:

```
from kai_sdk_python_kaistudio.index import KaiStudio, KaiStudioCredentials

//apiKey is optionnal
credentials = KaiStudioCredentials(host="your server host", apiKey="your api key")
search = KaiStudio(credentials).search()
print("SEARCH QUERY:")
print(await search.query("what is the history of France TV?", "userid"))

```

## Usage Guide

### ManageInstance

[ManageInstance.py](modules/ManageInstance.py) provides methods for managing instance.

- `generate_new_api_key` : generate a new API key
- `update_name` : update the instance name
  > name: 'The new name for the instance'
- `deploy` : deploy an instance
  > name: 'The name of the instance to deploy'
- `delete` : delete an instance
  > name: 'The name of the instance to delete'
- `add_kb` : add a knowledge base to the instance
  > kb_type: 'Type of knowledge base'
  > options: 'Configuration options for the knowledge base'
  > search_goal: 'The search goal associated with the KB'
- `set_playground` : set playground types for the instance
  > type_list: 'A list of playground types'
- `update_kb` : update a knowledge base
  > id: 'The ID of the knowledge base to update'
  > options: 'Updated configuration options'
  > search_goal: 'Updated search goal'
- `remove_kb` : remove a knowledge base from the instance
  > id: 'The ID of the knowledge base to remove'

For example:

```py
manage_instance = KaiStudio(credentials).manage_instance()
print("GET GLOBAL HEALTH:")
print(await manage_instance.get_global_health())
```

### FileInstance

[FileInstance.py](modules/FileInstance.py) provides methods for interacting with the Kai Studio file management API.

- `list_files` : list all available files in Kai Studio
- `upload_files` : upload multiple files to Kai Studio
  > files: 'List of file data to upload'
- `download_file` : download a file from Kai Studio
  > fileName: 'Name of the file to download'
- `delete_file` : delete a file from Kai Studio
  > fileName: 'Name of the file to delete'

For example:

```py
file_instance = KaiStudio(credentials).file_manager()
print("LIST FILES:")
print(await file_instance.list_files())
```

#### state-document 
We have 7 states for a document:

```python
'PARSING_ERROR', # document type is not supported
'INITIAL_SAVED', # initial save
"UPDATED", # document is updated (without the content) par rapport à l'API
'ON_CONTENT_EXTRACT', # document content is currently is working on fileparser
'CONTENT_EXTRACTED', # document content is fetch from fileparser and chunks is saved
'ON_INDEXATION', # document is in indexation progress
'INDEXED' # document is fully indexed
```

<u>**For more examples, you can check the [example.py](example.py) file.**</u>

## Contributing

bxu@k-ai.ai

rmei@k-ai.ai

sngo@k-ai.ai