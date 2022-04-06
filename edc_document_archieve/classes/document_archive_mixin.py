from django.apps import apps as django_apps


class DocumentArchiveMixin:
    @property
    def consent_image_model_cls(self):
        consent_image_model = 'edc_odk.consentimage'
        return django_apps.get_model(consent_image_model)

    @property
    def specimen_consent_image_model_cls(self):
        specimen_consent_image_model = 'edc_odk.specimenconsentimage'
        return django_apps.get_model(specimen_consent_image_model)

    @property
    def national_id_image_model_cls(self):
        nation_id_image_model = 'edc_odk.nationalidentityimage'
        return django_apps.get_model(nation_id_image_model)

    @property
    def note_to_file_image_model_cls(self):
        note_to_file_image_model = 'edc_odk.notetofiledocs'
        return django_apps.get_model(note_to_file_image_model)

    @property
    def clinician_notes_archive_image_model_cls(self):
        clinician_notes_archive_image_model = 'edc_odk.cliniciannotesimagearchive'
        return django_apps.get_model(clinician_notes_archive_image_model)

    @property
    def lab_results_file_model_cls(self):
        labresults_file_model = 'edc_odk.labresultsfile'
        return django_apps.get_model(labresults_file_model)

    def clinician_notes_image_model(self, app_name=None):
        return django_apps.get_model('%s.cliniciannotesimage' % app_name)

    def clinician_notes_model_cls(self, app_name=None):
        app_config = django_apps.get_app_config(
            'edc_odk').clinician_notes_models
        clinician_notes_model = app_config.get(app_name, 'default')

        if clinician_notes_model:
            return django_apps.get_model(
                '%s.%s' % (app_name, clinician_notes_model))

    @property
    def td_consent_version_cls(self):
        td_consent_version_model = 'td_maternal.tdconsentversion'
        return django_apps.get_model(td_consent_version_model)

    @property
    def flourish_consent_version_cls(self):
        flourish_consent_version_model = 'flourish_caregiver.flourishconsentversion'
        return django_apps.get_model(flourish_consent_version_model)
    
    @property
    def infant_clinician_notes_image_model_cls(self):
        clinician_notes_image_model = 'td_infant.cliniciannotesimage'
        return django_apps.get_model(clinician_notes_image_model)

    @property
    def assent_image_model_cls(self):
        assent_image_model = 'edc_odk.assentimage'
        return django_apps.get_model(assent_image_model)

    @property
    def adult_main_consent_image_model_cls(self):
        adult_main_consent_image_model = 'edc_odk.adultmainconsentimage'
        return django_apps.get_model(adult_main_consent_image_model)

    @property
    def continued_participation_image_model_cls(self):
        continued_consent_image_model = 'edc_odk.continuedparticipationimage'
        return django_apps.get_model(continued_consent_image_model)

    @property
    def parental_consent_image_model_cls(self):
        parental_consent_image_model = 'edc_odk.parentalconsentimage'
        return django_apps.get_model(parental_consent_image_model)
