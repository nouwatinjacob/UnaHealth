from datetime import datetime
import os

from django.apps import apps
from django.core.management.base import BaseCommand

import csv

readings_mapping = {
    "Gerät": "device",
    "Seriennummer": "serial_number",
    "Gerätezeitstempel": "device_timestamp",
    "Aufzeichnungstyp": "recording_type",
    "Glukosewert-Verlauf mg/dL": "glucose_value_history",
    "Glukose-Scan mg/dL": "glucose_scan"
}
readings_mapping_keys = readings_mapping.keys()


class Command(BaseCommand):
    help = 'Creating model objects according the file path specified'

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str, help="file path")
        parser.add_argument('--model_name', type=str, help="model name")
        parser.add_argument('--app_name', type=str, help="django app name that the model is connected to")

    def handle(self, *args, **options):
        file_path = options['path']
        file_path_name = os.path.basename(file_path).split(".")[0]
        _model = apps.get_model(options['app_name'], options['model_name'])
        with open(file_path) as csv_file:
            reader = csv.reader(csv_file, delimiter=',')
            next(reader)
            header = next(reader)
            for row in reader:
                print("header", header)
                _object_dict = {readings_mapping[key]: value for key, value in zip(header, row) if key in readings_mapping_keys}
                _object_dict["user_id"] = file_path_name
                _object_dict["device_timestamp"] = datetime.strptime(_object_dict["device_timestamp"], '%d-%m-%Y %H:%M')
                # print("_object_dict", _object_dict, "Gerät" in readings_mapping_keys)
                _model.objects.create(**_object_dict)