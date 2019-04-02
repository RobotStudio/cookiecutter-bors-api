# -*- coding: utf-8
from bors.apps import AppConfig


class {{ cookiecutter.app_config_name }}(AppConfig):
    name = '{{ cookiecutter.app_name }}'
