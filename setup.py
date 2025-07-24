import setuptools

setuptools.setup(
    name="kai_sdk_python_kaistudio",
    version="20250724",
    author="KAI",
    author_email="support@kai.ai",
    description="sdk kaistudio python",
    packages=setuptools.find_packages(),
    install_requires=['httpx==0.28.0'],
    python_requires='>=3.8',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    url='https://github.com/k-ai-Documentation/sdk-python'
)
