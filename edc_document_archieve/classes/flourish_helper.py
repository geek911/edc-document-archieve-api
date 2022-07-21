from django.apps import apps as django_apps

from .flourish_forms import FlourishForms


class FlourishHelper(FlourishForms):

    caregiver_consent_model = 'flourish_caregiver.subjectconsent'
    child_consent_model = 'flourish_child.childdummysubjectconsent'
    caregiver_child_consent_model = 'flourish_caregiver.caregiverchildconsent'

    @property
    def child_consent_cls(self):
        return django_apps.get_model(self.child_consent_model)

    @property
    def caregiver_child_consent(self):
        return django_apps.get_model(self.caregiver_child_consent_model)

    @property
    def caregiver_consent_cls(self):
        return django_apps.get_model(self.caregiver_consent_model)

    @property
    def flourish_pids(self):
        caregiver_pids = self.caregiver_consent_cls.objects.values_list(
            'subject_identifier', flat=True).distinct()

        caregiver_child = self.caregiver_consent_cls.objects.objects.values_list(
            'subject_identifier', flat=True).distinct()

        caregiver_pids.extend(caregiver_child)
        child_pids = self.child_consent_cls.objects.values_list(
            'subject_identifier', flat=True).distinct()
        data = {
            'caregiver': caregiver_pids,
            'child': child_pids
        }
        return data
