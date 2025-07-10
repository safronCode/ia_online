from django.shortcuts import render, redirect
from integration_utils.bitrix24.bitrix_user_auth.main_auth import main_auth


@main_auth(on_cookies=True)
def add_deal(request):
    if request.method == 'POST':
        stage_id = request.POST.get('stage_id')
        title = request.POST.get('title')
        opportunity = request.POST.get('opportunity')
        begindate = request.POST.get('begindate')
        closedate = request.POST.get('closedate')
        address = request.POST.get('address')
        vip_status = request.POST.get('vip_status')

        fields = {
            'STAGE_ID': stage_id,
            'TITLE': title,
            'OPPORTUNITY': opportunity,
            'BEGINDATE': begindate,
            'CLOSEDATE': closedate,
            'UF_CRM_1752105537687': address,
            'UF_CRM_1752105693326': vip_status,
        }

        if vip_status == 'on':
            fields['UF_CRM_1752105693326'] = "1"
        else:
            fields['UF_CRM_1752105693326'] = "0"

        but = request.bitrix_user_token
        but.call_api_method('crm.deal.add', {'fields': fields})
        return redirect('active_deals')

    return render(request, 'add_mode.html')