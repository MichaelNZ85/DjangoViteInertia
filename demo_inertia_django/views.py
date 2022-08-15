from inertia import render


def home(request):
    return render(request, 'Event/Index', props={
        'events': ['Big Purrs', 'Meow meow', 'Furry Friends Meetup']
    })