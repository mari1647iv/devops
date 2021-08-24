from setuptools import setup

setup(
    name='app_python',
    version='1.0',
    description='Simple Python web application, that shows current time in Moscow',
    author='Marina Ivanova',
    author_email='m.ivanova@innopolis.university',
    packages=['app_python'],
    install_requires=['Flask == 1.1.2', 'pytz'],
)
