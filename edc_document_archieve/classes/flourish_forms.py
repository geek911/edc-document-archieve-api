from django.apps import apps as django_apps


class FlourishForms:
    odk_app = 'edc_odk'

    @property
    def caregiver_non_crfs(self):
        models = []
        app_models = django_apps.get_app_config(self.odk_app).get_models()
        for model in app_models:
            if model._meta.verbose_name.istitle():
                models.append({
                    'app_label': model._meta.app_label,
                    'model_name': model._meta.verbose_name
                })
        return models

    @property
    def caregiver_crfs(self):
        models = [
            {
                'app_label': 'flourish_caregiver',
                'model_name': 'Clinician Notes',
            }
        ]
        return models

    @property
    def caregiver_forms(self):
        data = {
            'crfs': self.caregiver_crfs,
            'non_crfs': self.caregiver_non_crfs
            }
        return data

    @property
    def child_forms(self):
        data = {
                'crfs': [{
                    'app_label': 'flourish_child',
                    'model_name': 'Clinician Notes'
                }],
                'non_crfs': [{
                    'model_name': 'Consent Copies',
                    'app_label': 'flourish_child',
                }]
            }
        return data

    def create_non_crf_from(self):
        pass
