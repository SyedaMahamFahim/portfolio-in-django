from django.contrib import admin

# Register your models here.
from .models import Contact
from .models import About,Achievement,Skills,Testimonials,Services,Portfolio


admin.site.register(Contact)
admin.site.register(About)
admin.site.register(Achievement)
admin.site.register(Skills)
admin.site.register(Testimonials)
admin.site.register(Services)
admin.site.register(Portfolio)
