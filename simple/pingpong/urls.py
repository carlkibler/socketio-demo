
from django.conf.urls.defaults import patterns, include, url
import socketio.sdjango

socketio.sdjango.autodiscover()

urlpatterns = patterns("pingpong.views",
    url("^socket\.io", include(socketio.sdjango.urls)),
    url("^$", "table", name="table"),
)
