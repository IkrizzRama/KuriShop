from django.forms import ModelForm
from main.models import objectEntry

class ObjectEntryForm(ModelForm):
    class Meta:
        model = objectEntry
        fields = ["object", "price", "description"]