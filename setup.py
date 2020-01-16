from setuptools import setup

setup(
    name='cam_labyrinth',
    version='0.1',
    author="Camille Clarret",
    author_email="camille.clarret@gmail.com",
    url="https://github.com/CamClrt/labyrinth",
    scripts=['bin/cam_labyrinth.py'],
    packages=['cam_labyrinth'],
    package_data={'cam_labyrinth': ['resources/*','*.txt'],},
)