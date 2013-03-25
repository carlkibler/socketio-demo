from socketio import socketio_manage

from django.http import HttpResponse
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import get_object_or_404, render, redirect

from sockets import PingPongNamespace

def table(request, template="table.html"):
    """
    Show the table.
    """
    context = {}
    return render(request, template, context)

