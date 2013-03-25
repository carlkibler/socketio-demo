from django.shortcuts import render

# This is a *necessary* import! Loading this alerts the gevent-socketio
# library to build the SocketIO namespace. Remove it and nothing will
# answer the incoming client calls.
from sockets import PingPongNamespace

def table(request, template="table.html"):
    """
    Show the table.
    """
    context = {}
    return render(request, template, context)

