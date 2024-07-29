from models.models import Setting

def get_setting(request):
    qs = Setting.objects.first()
    return {
        'settings': qs
    }