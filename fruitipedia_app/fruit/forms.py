from django import forms

from fruitipedia_app.fruit.models import Fruit


class DeleteFruitForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = ("name", "image_url", "description")

        widgets = {
            "image_url": forms.URLInput(attrs={"placeholder": "Image URL"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["disabled"] = "disabled"






