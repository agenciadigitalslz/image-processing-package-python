from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="image_processing_dio",
    version="0.0.1",
    author="Seu Nome",
    author_email="seu.email@exemplo.com",
    description="Pacote de processamento de imagens usando Skimage",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/seu-usuario/image-processing-package-python",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
    ],
)
