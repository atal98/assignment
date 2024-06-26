from django.apps import AppConfig


class VendorModelsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'vendor_models'

    def ready(self):
        import vendor_models.signals
