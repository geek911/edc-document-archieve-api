from django.apps import apps as django_apps
from .tshilo_dikotla_forms import TshiloDikotlaForms


class TshiloDikotlaHelper(TshiloDikotlaForms):
    maternal_consent_model = 'td_maternal.subjectconsent'
    infant_consent_model = 'td_infant.infantdummysubjectconsent'

    @property
    def infant_consent_cls(self):
        return django_apps.get_model(self.infant_consent_model)

    @property
    def maternal_consent_cls(self):
        return django_apps.get_model(self.maternal_consent_model)

    @property
    def td_pids(self):
        maternal_pids = self.maternal_consent_cls.objects.values_list(
            'subject_identifier', flat=True).distinct()

        infant_pids = self.infant_consent_cls.objects.values_list(
            'subject_identifier', flat=True).distinct()
        data = {
            'caregiver': maternal_pids,
            'child': infant_pids
        }
        return data
