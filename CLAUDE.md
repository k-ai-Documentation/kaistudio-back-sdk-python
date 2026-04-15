# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This is `kai_sdk_python_kaistudio`, a Python SDK for interacting with the KAI Studio API. It supports two deployment modes: **SaaS** (cloud-hosted, requires `organization_id`, `instance_id`, `api_key`) and **Premise** (self-hosted, requires `host` and optional `api_key`).

## Installation

```bash
pip install git+https://github.com/k-ai-Documentation/sdk-python-kaistudio.git
```

For local development, install the package in editable mode from the repo root:

```bash
pip install -e .
```

The only dependency is `httpx==0.28.0`.

## Architecture

Mirrors the JS SDK (`kaistudio-back-sdk-js`) structure exactly.

```
index.py                         # KaiStudioBackApi factory — entry point
modules/
  KaiStudioCredentials.py        # Auth config: token (Bearer) + optional host
  core/
    CoreModule.py                # Namespace: exposes .user()
    UserModule.py                # /core/user/*
  studio/
    StudioModule.py              # Namespace: exposes .instance(), .knowledge_base(), .organization()
    InstanceModule.py            # /studio/instance/*
    KnowledgeBaseModule.py       # /studio/knowledge-base/*
    OrganizationModule.py        # /studio/organization/*
  global_admin/
    GlobalAdminModule.py         # /global-admin/*
example.py                       # Usage reference
```

**`KaiStudioBackApi` (index.py)** accepts `KaiStudioCredentials` and exposes three top-level namespaces: `.core()`, `.studio()`, `.global_admin()`.

**All API methods are `async`** — callers must use `await` inside an `async` context (e.g., `asyncio.run(...)`).

`instance_id` and `organization_id` are **explicit per-method parameters** — they are not stored in credentials.

## Credentials

```python
KaiStudioCredentials(
    token="...",             # Bearer token for Authorization header
    host="https://..."       # optional, defaults to https://back.kai-studio.ai
)
```
