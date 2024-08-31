import json
import os
from django.conf import settings

def load_templates():
    template_path = os.path.join(
        settings.BASE_DIR,
        'template',  
        'component',
        'Messages',
        'template.json'
    )
    with open(template_path, 'r') as file:
        return json.load(file)

TEMPLATES = load_templates()

def generate_message(template_key, **kwargs):
    template = TEMPLATES.get(template_key, {})
    message = template.copy()
    for key, value in kwargs.items():
        message['message'] = message['message'].replace(f"[{key}]", value)
    return message