from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render
from .forms import TrackForm
from .models import Talk
from .models import Track


# Create your views here.
def talk_list(request):
    talks = Talk.objects.all()
    output = ', '.join([str(talk) for talk in talks])
    return HttpResponse(output)


def talk_template_list(request):
    talks = Talk.objects.all()
    return render(request, 'talks/talk_list.html', {'talks': talks})


def talk_details(request, pk):
    talk = Talk.objects.get(pk=pk)
    return render(request, 'talks/talk_details.html', {'talk': talk})


def track_details(request, pk):
    # track = Track.objects.get(pk=pk)
    track = get_object_or_404(Track, pk=pk)
    return render(request, 'talks/track_details.html', {'track': track})


def track_list(request):
    tracks = Track.objects.all()
    return render(request, 'talks/track_list.html', {'tracks': tracks})


def track_new(request):
    if request.method == "POST":
        form = TrackForm(request.POST)
        if form.is_valid():
            track = form.save()
            return redirect('tracks:details', pk=track.pk)
    else:
        form = TrackForm()
    return render(request, 'talks/track_edit.html', {'form': form})
