from django.apps import apps as django_apps


class FlourishCaregiverFormsViewMixin:

    @property
    def caregiver_non_crfs(self):
        models = []
        app_models = django_apps.get_app_config(self.odk_app).get_models()
        for model in app_models:
            if model._meta.verbose_name.istitle():
                models.append(model._meta.verbose_name)
        return models

    @property
    def caregiver_crfs(self):
        models = [
            'Caregiver Clinician Notes',
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
                'crfs': ['Child Clinician Notes'],
                'non_crfs': ['Consent Copies']
            }
        return data

    def create_non_crf_from(self):
        pass
