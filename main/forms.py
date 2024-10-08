from django.forms import ModelForm
from main.models import objectEntry
from django.utils.html import strip_tags

class ObjectEntryForm(ModelForm):
    class Meta:
        model = objectEntry
        fields = ["object", "price", "description"]

    def clean_object(self):
        object = self.cleaned_data["object"]
        return strip_tags(object)

    def clean_price(self):
        price = self.cleaned_data["price"]
        return strip_tags(price)