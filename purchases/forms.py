from django.forms import ModelForm
from .models import POStatus

class POStatusForm(ModelForm):
    class Meta:
        model = POStatus
        fields = ['code', 'status', 'seq']
