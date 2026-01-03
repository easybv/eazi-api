# users/validators.py

from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

class CustomPasswordValidator:
    def validate(self, password, user=None):
        # You can perform custom password validation here
        pass

    def get_help_text(self):
        return _("Your custom password help text goes here.")
