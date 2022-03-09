from rest_framework.response import Response
from rest_framework.views import APIView
from .flourish_home_view_mixin import FlourishHomeViewMixin
from django.db.utils import IntegrityError
from django.apps import apps as django_apps
from edc_appointment.constants import NEW_APPT


class HomeView(FlourishHomeViewMixin, APIView):

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
        return '%s.cliniciannotesimage' % app_name

    def clinician_notes_model_cls(self, app_name=None):
        app_config = django_apps.get_app_config(
            'edc_odk').clinician_notes_models

        clinician_notes_model = app_config.get(app_name, 'default')

        if clinician_notes_model:
            return django_apps.get_model(
                '%s.%s' % (app_name, clinician_notes_model))

    def get(self, request):
        studies = {

            'flourish': {
                'pids': self.pids,
                'caregiver_forms': self.caregiver_forms,
                'child_forms': self.child_forms
            },
            'tshilo-dikotla': {},
        }

        results = [
            {
                'subject_identifier': 'B142-040990462-9',
                'visit_code': '3001M',
                'timepoint': 0
            }
        ]
        print(self.populate_model_objects(
            'flourish_caregiver',
            results,
            self.clinician_notes_model_cls,
        ))
        return Response(studies)

    def post(self, request):
        pass

    def populate_model_objects(self, app_name, result, model_cls):
        updated = 0
        count = 0
        for data_dict in result:
            if data_dict['visit_code']:
                # Get visit
                visit_obj = self.get_app_visit_model_obj(
                    app_name,
                    data_dict['subject_identifier'],
                    data_dict['visit_code'],
                    data_dict['timepoint'])

                visit_models = self.get_visit_models().get(app_name)
                field_name = None
                if visit_models:
                    field_name = visit_models[0]
                if visit_obj:
                    try:
                        obj, created = model_cls.objects.get_or_create(
                            report_datetime__gte=visit_obj.report_datetime,
                            **{f'{field_name}': visit_obj},
                            defaults={'report_datetime': visit_obj.report_datetime})
                        if created:
                            # self.create_image_obj_upload_image(
                            #     image_cls,
                            #     image_cls_field,
                            #     obj,
                            #     data_dict)
                            count += 1
                        else:
                            # imgs_updated = self.update_existing_image_objs(
                            #     image_cls,
                            #     image_cls_field,
                            #     obj,
                            #     data_dict)
                            # if imgs_updated:
                            updated += 1
                    except IntegrityError as e:
                        raise Exception(e)
        return count, updated

    def get_app_visit_model_obj(
            self, app_name, subject_identifier, visit_code, timepoint):
        visit_model_obj = None
        visit_models = self.get_visit_models().get(app_name)

        if visit_models:
            visit_model_cls = django_apps.get_model(
                visit_models[1])

            visit_model_obj = visit_model_cls.objects.filter(
                subject_identifier=subject_identifier,
                visit_code=visit_code,
                visit_code_sequence=timepoint).exclude(
                    appointment__appt_status=NEW_APPT).order_by('-report_datetime').last()
            if not visit_model_obj:
                message = (f'Failed to get visit for {subject_identifier}, at '
                           f'visit {visit_code}. Visit does not exist.')

        return visit_model_obj

    def get_visit_models(self):
        app_config = django_apps.get_app_config('edc_visit_tracking')
        return app_config.visit_models
