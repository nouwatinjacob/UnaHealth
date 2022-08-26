from datetime import datetime
import os
import glob
from re import M

from django.apps import apps
from django.contrib.auth.hashers import make_password
from django.core.management.base import BaseCommand



class Command(BaseCommand):
    help = 'Creating Reading model objects according the file path specified'

    def handle(self, *args, **options):
        directory_path = [f.path for f in os.scandir('.') if f.is_dir() and f.path == "./sample_data"][0]
        file_paths = glob.glob(f"{directory_path}/*")
        
        _model = apps.get_model('users', 'user')
        for file_path in file_paths:
            file_path_name = os.path.basename(file_path).split(".")[0]
            _object_dict = {"user_id": file_path_name, "username": file_path_name,
                            "password": make_password("password")}
            print()
            _model.objects.create(**_object_dict)