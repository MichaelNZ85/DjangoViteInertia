from inertia import render


def home(request):
    return render(request, 'Events/Index', props={
        'events': ['Big Purrs', 'Meow meow', 'Furry Friends Meetup']
    })


def contact(request):
    return render(request, 'Contact', props={
        'support_email': 'meow@bigpurrs.mew'
    })
