from django.utils.translation import ugettext_lazy as _

import horizon

from thermal import dashboard


class Builder(horizon.Panel):
    name = _("Build Templates")
    slug = "builder"


dashboard.Thermal.register(Builder)
