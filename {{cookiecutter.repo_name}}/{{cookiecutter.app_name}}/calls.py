# -*- coding: utf-8 -*-
{% if cookiecutter.calls != "Comma-separated list of API calls" %}
from bors.app import Call

{% for call in cookiecutter.call.split(',') %}
class {{ call.strip() }}(Call):
    pass

{% endfor %}
{% endif %}
