from django.apps import AppConfig


class EpsilonConfig(AppConfig):
    name = 'epsilon'

    def ready(self):
        import epsilon.signals
