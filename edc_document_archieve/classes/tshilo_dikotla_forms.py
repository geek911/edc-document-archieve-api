from django.apps import apps as django_apps


class TshiloDikotlaForms:

    @property
    def maternal_non_crfs(self):
        models = []
        app_models = django_apps.get_app_config(self.odk_app).get_models()
        for model in app_models:
            if model._meta.verbose_name.istitle():
                models.append({
                    'app_label': model._meta.app_label,
                    'model_name': model._meta.verbose_name
                })
            if model._meta.verbose_name == 'Note to file':
                models.append({
                        'app_label': model._meta.app_label,
                        'model_name': model._meta.verbose_name
                })
        return models

    @property
    def maternal_crfs(self):
        models = [
            {
                'app_label': 'td_maternal',
                'model_name': 'Clinician Notes',
            },
        ]
        return models

    @property
    def maternal_forms(self):
        data = {
            'crfs': self.maternal_crfs,
            'non_crfs': self.maternal_non_crfs
            }
        return data

    @property
    def infant_forms(self):
        data = {
                'crfs': [{
                    'app_label': 'td_infant',
                    'model_name': 'Clinician Notes'
                }],
                'non_crfs': []
            }
        return data
