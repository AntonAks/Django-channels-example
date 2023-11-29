import logging
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


logger = logging.getLogger(__name__)


@login_required(login_url="")
def index(request):
    logging.warning(f"request.user: {request.user}")

    return render(request, "chat/index.html")


@login_required(login_url="")
def room(request, room_name):
    logging.warning(f"request.user: {request.user}")
    return render(request, "chat/room.html", {"room_name": room_name,
                                              "user_name": request.user.username})
