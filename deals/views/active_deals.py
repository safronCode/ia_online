from django.shortcuts import render
from integration_utils.bitrix24.bitrix_user_auth.main_auth import main_auth
from datetime import datetime
from dateutil import tz


def iso_transform(date):
    date = datetime.fromisoformat(date.replace('Z', '+00:00'))
    date_moscow = date.astimezone(tz.gettz('Europe/Moscow'))
    return (date_moscow.strftime('%d/%m/%Y'))


@main_auth(on_cookies=True)
def active_deals(request):
    but = request.bitrix_user_token
    recent_active = but.call_api_method("crm.deal.list", {
        'filter': {
            'ASSIGNED_BY_ID': request.bitrix_user.id,
             "!@STAGE_ID": ["WON", "LOSE", "APOLOGY"]
        },
        'order': {'BEGINDATE': 'DESC'},
        'select': ['ID', 'STAGE_ID', 'TITLE','OPPORTUNITY','BEGINDATE','CLOSEDATE','UF_CRM_1752105537687','UF_CRM_1752105693326'],
    })['result'][:10]

    for deal in recent_active:
        deal['BEGINDATE'] = iso_transform(deal['BEGINDATE'])
        deal['CLOSEDATE'] = iso_transform(deal['CLOSEDATE'])
        if deal['UF_CRM_1752105693326'] == "1":
            deal['UF_CRM_1752105693326'] = "✔"
        else:
            deal['UF_CRM_1752105693326'] = "✘"

    return render(request, 'active_mode.html', locals())