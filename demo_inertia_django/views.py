from inertia import render


def home(request):
    return render(request, 'Events/Index', props={
        'events': ['Big Purrs', 'Meow meow', 'Furry Friends Meetup']
    })
