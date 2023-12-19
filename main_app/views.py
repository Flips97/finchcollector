from django.shortcuts import render

finches = [
    {'name': 'Stitch', 'type': 'Blue Finch', 'description': 'Bright blue bird', 'age':1},
    {'name': 'Sammy', 'type': 'Saffron Finch', 'description': 'Yellow bird with additude', 'age':3},
]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    return render(request, 'finches/index.html', {
        'finches': finches
    })