from stream.models import Stream
from django.views import generic


class IndexView(generic.ListView):
    template_name = 'stream/index.html'
    context_object_name = 'stream'

    def get_queryset(self):
        """Return the last five published questions."""
        return Stream.objects.order_by('-created_at')

