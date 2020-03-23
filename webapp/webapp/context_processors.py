from django.conf import settings

def public_app_info (request):
    if settings.APP_NAME :
        return {'app_name': settings.APP_NAME}
    else :
        return {'app_name': 'My App'}
