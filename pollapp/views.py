from django.shortcuts import (render,
                              get_list_or_404,
                              get_object_or_404,
                              HttpResponse)
from pollapp.models import Poll, Choice
import socket
# Create your views here.


def poll_details(request, poll_id=None):
    poll = get_object_or_404(Poll, pk=poll_id)
    choice = poll.choice_set.all()
    total_votes = 0
    for i in choice:
        total_votes = total_votes+i.vote
    return render(request, 'detail.html', {'data_hash': poll,
                                           'total_votes': total_votes})


def vote(request, poll_id=None):
    poll = get_object_or_404(Poll, pk=poll_id)
    option_id = request.GET.get('option_id')
    fingerprint = request.GET.get('fp')
    ip_address = socket.gethostbyname(socket.gethostname())

    if poll.fingerprint != fingerprint and poll.ip_address != ip_address:
        poll.fingerprint = fingerprint
        poll.ip_address = ip_address
        poll.save()
        selected_choice = poll.choice_set.get(pk=option_id)
        selected_choice.vote += 1
        selected_choice.save()
        return HttpResponse(poll.id, content_type="text/plain")
    else:
        return HttpResponse('voted', content_type="text/plain")
