from django.http import JsonResponse, HttpResponse
from gvm.connections import UnixSocketConnection
from gvm.protocols.gmp import Gmp
from django.shortcuts import render

def index_view(request):
    items = ['Item 1', 'Item 2', 'Item 3']
    return render(request, 'myapp/index.html', {'items': items})

def add_target(request):
    try:
        with UnixSocketConnection() as connection:
            connection.connect()
            with Gmp(connection) as gmp:
                target = gmp.create_target(name='Target Name', hosts='127.0.0.1')
                return JsonResponse({'message': 'Target created successfully'})
    except Exception as e:
        return JsonResponse({'error': str(e)})

def start_scan(request, target_id):
    try:
        with UnixSocketConnection() as connection:
            connection.connect()
            with Gmp(connection) as gmp:
                gmp.create_task(target_id)
                return JsonResponse({'message': 'Scan started successfully'})
    except Exception as e:
        return JsonResponse({'error': str(e)})

def download_report(request, report_id):
    try:
        with UnixSocketConnection() as connection:
            connection.connect()
            with Gmp(connection) as gmp:
                report = gmp.get_report(report_id)
                file_content = report.download()
                response = HttpResponse(file_content, content_type='application/xml')
                response['Content-Disposition'] = f'attachment; filename="{report_id}.xml"'
                return response
    except Exception as e:
        return JsonResponse({'error': str(e)})
