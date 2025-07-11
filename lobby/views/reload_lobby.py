from django.shortcuts import render, redirect
from integration_utils.bitrix24.bitrix_user_auth.main_auth import main_auth


@main_auth(on_cookies=True)
def reload_lobby(request):
    if request.path == '/lobby/':
        return render(request, 'start_page.html')
    return redirect('/lobby/')