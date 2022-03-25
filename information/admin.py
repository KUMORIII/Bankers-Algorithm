from django.contrib import admin

from information.models import *

# Register your models here.

admin.site.register(Resource)
admin.site.register(Process)
admin.site.register(Need)
admin.site.register(Max)
admin.site.register(Allocation)

admin.site.site_title = "AHU-Banker's Algorithm"
admin.site.site_header = "AHU-Banker'sAlgorithm-Django管理"