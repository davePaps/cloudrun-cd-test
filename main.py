import functions_framework


@functions_framework.http
def sync_sheets_to_gcs(request):
    return "Hi Dave", 200
