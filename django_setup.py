import sys
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blog_comments.settings")
django.setup()