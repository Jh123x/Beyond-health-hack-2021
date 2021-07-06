import datetime

from django.http.response import HttpResponseNotAllowed
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import TherapySessions, Attendance


# Create your views here.
@login_required(redirect_field_name='login', login_url="/login")
def index(request):
    """Main page for viewing sessions"""
    if request.method != "GET":
        return HttpResponseNotAllowed("Other methods not allowed")

    page = request.GET.get('page', 1)

    all_sessions = TherapySessions.objects.all()[page-1:page + 9]

    return render(request, "sessions_list.html", {'sessions': all_sessions})

@login_required
def session(request, path):
    if request.method != "GET":
        return HttpResponseNotAllowed("Other methods not allowed")

    session = TherapySessions.objects.filter(session_id=path).get()
    participants = Attendance.objects.filter(session_id=path).count()

    return render(request, "session.html", {"session":session, "participants":participants})
