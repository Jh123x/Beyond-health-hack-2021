from django.contrib import messages
from django.http.response import HttpResponseNotAllowed
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user

from .models import TherapySessions, Attendance


# Create your views here.
@login_required(redirect_field_name='login', login_url="/login")
def index(request):
    """Main page for viewing sessions"""
    if request.method not in ("GET",):
        return HttpResponseNotAllowed("Other methods not allowed")

    page = request.GET.get('page', 1)
    all_sessions = TherapySessions.objects.all()[page-1:page + 9]
    return render(request, "sessions_list.html", {'sessions': all_sessions})

@login_required
def session(request, path):
    if request.method not in ("GET", "POST"):
        return HttpResponseNotAllowed("Other methods not allowed")

    user = get_user(request)
    session = TherapySessions.objects.filter(session_id=path).get()
    temp = Attendance.objects.filter(session_id=path)
    participants =temp.count()
    
    if request.method == "POST":
        if participants >= session.max_members:
            messages.error(request, "The max number of participants is reached")
            return redirect(f"/sessions/{path}")

        if Attendance.objects.filter(user=user, session=session).exists():
            messages.Error(request, "You have already registered for this session")
            return redirect(f"/sessions/{path}")

        attendance = Attendance(user = user, session = session)
        attendance.save()
        messages.info(request, "Successfully registered for class")
        return redirect(f"/sessions/{path}")

    is_participating = temp.filter(user=user).exists()    
    return render(request, "session.html", {"session":session, "participants":participants, "in_session":is_participating})
