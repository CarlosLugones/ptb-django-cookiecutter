from django.apps import AppConfig


class BotConfig(AppConfig):
    name = '{{cookiecutter.project_slug}}.bot'
    label = 'bot'
    verbose_name = 'The Bot Core'
