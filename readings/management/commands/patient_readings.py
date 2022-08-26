from datetime import datetime
import os
import glob

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
    help = 'Creating Reading model objects according the file path specified'

    def handle(self, *args, **options):
        directory_path = [f.path for f in os.scandir('.') if f.is_dir() and f.path == "./sample_data"][0]
        file_paths = glob.glob(f"{directory_path}/*")
        
        _model = apps.get_model('readings', 'reading')
        for file_path in file_paths:
            file_path_name = os.path.basename(file_path).split(".")[0]
            with open(file_path) as csv_file:
                reader = csv.reader(csv_file, delimiter=',')
                next(reader)
                header = next(reader)
                for row in reader:
                    _object_dict = {readings_mapping[key]: value for key, value in zip(header, row) if key in readings_mapping_keys}
                    _object_dict["user_id"] = file_path_name
                    _object_dict["device_timestamp"] = datetime.strptime(_object_dict["device_timestamp"], '%d-%m-%Y %H:%M')
                    _model.objects.create(**_object_dict)