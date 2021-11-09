import mimetypes
import os
from django.http.response import HttpResponse


def download_report(request,report_filename):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filename=report_filename
    filepath = BASE_DIR + '/healthcare/reports/' + filename +".pdf"
    path = open(filepath, 'rb')
    mime_type, _ = mimetypes.guess_type(filepath)
    response = HttpResponse(path.read(), content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s.pdf" % filename
    return response

