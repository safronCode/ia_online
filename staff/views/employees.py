from django.utils import timezone
from datetime import timedelta
from django.shortcuts import render

from integration_utils.bitrix24.bitrix_user_auth.main_auth import main_auth



@main_auth(on_cookies=True)
def employees_telephony(request):

    but = request.bitrix_user_token
    departments_result = but.call_list_method('department.get', {
        'sort': 'ID',
        'order': 'ASC',
    })


    def saturation_managers(departments):
        dep_by_id = {dep['ID']: dep for dep in departments}

        for department in departments:
            department['managers'] = []

            if department.get('PARENT'):
                parent_id = department['PARENT']
                parent_dep = dep_by_id.get(parent_id)
                department['managers'] = list(parent_dep.get('managers', []))
                local_manager = but.call_list_method('im.department.managers.get',
                                                     {'ID': [department['ID']],
                                                      'USER_DATA': 'Y'})
                department['managers'].append(local_manager.get(department['ID'], [{}])[0].get('name'))

            else:
                global_manager = but.call_list_method('im.department.managers.get',
                                                     {'ID': [department['ID']],
                                                      'USER_DATA': 'Y'})
                department['managers'].append(global_manager.get(department['ID'], [{}])[0].get('name'))

            department['managers'] = list(dict.fromkeys(department['managers']))[::-1]

        return departments

    def saturation_employees(departments):

        for department in departments:
            employees_result = but.call_list_method('im.department.employees.get', {
                'ID': [department['ID']],
                'USER_DATA': 'Y'
            })


            employees_list = []
            for employees in employees_result[department['ID']]:
                employees_list.append({
                    'id': employees.get('id'),
                    'name': employees.get('name'),
                    'work_position': employees.get('work_position'),
                    'avatar': employees.get('avatar')
                })

            department['employees'] = employees_list

        return departments

    def saturation_calls(departments):
        calls_result = but.call_list_method('voximplant.statistic.get', {
            'FILTER': {
                'CALL_TYPE': '1',
                '>CALL_DURATION': 60,
                '>CALL_START_DATE': (timezone.now()  - timedelta(hours=24)).isoformat()
            }
        })

        user_call_counts = {}


        for call in calls_result:
            user_id = call.get('PORTAL_USER_ID')

            if user_id is not None:
                if str(user_id) not in user_call_counts:
                    user_call_counts[str(user_id)] = 0

                user_call_counts[str(user_id)] += 1

        for department in departments:
            for employee in department.get('employees', []):

                employee['calls24'] = user_call_counts.get(str(employee['id']), 0)

        return departments


    def context_formation(departments):
        context = []
        for department in departments:
            departament_context = {
                'departament_ID': department.get('ID'),
                'departament_NAME': department.get('NAME'),
                'managers_list': department.get('managers'),
                'employees_list': department.get('employees'),
            }
            context.append(departament_context)
        return context


    saturation_managers(departments_result)
    saturation_employees(departments_result)
    saturation_calls(departments_result)
    context = context_formation(departments_result)

    return render(request, 'staff_table.html', {"context": context})