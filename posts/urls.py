from django.conf.urls import url

from posts.views import RetrieveUpdateDestroyPostView

urlpatterns = [
    url(r"^posts/(?P<pk>\d+)/$", RetrieveUpdateDestroyPostView.as_view()),
]
