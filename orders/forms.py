from django.forms import modelformset_factory
from .models import Order

# A regular form, not a formset
OrderFormSet = modelformset_factory(
    Order, fields=("qty", "ingredient_order"), extra=1
)