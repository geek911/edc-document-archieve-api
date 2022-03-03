from django.apps import AppConfig as DjangoAppConfig


class AppConfig(DjangoAppConfig):
    name = 'edc_document_archieve'
    verbose_name = "EDC Document Archieve"
    admin_site_name = 'edc_document_archieve_admin'
