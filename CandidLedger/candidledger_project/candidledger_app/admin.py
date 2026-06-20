from django.contrib import admin
from .models import (
    ContactEnquiry,
    TaxUpdate,
    TeamMember,
    Testimonial,
    Feedback,
)

admin.site.register(ContactEnquiry)
admin.site.register(TaxUpdate)
admin.site.register(TeamMember)
admin.site.register(Testimonial)
admin.site.register(Feedback)
