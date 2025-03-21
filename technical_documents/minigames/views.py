# Author: Jem Challis, Rami Youhana

from django.shortcuts import render
from .forms import NewGameScore
from .models import GameScore, Game
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
import json

### STR VIEWS START ###
def str_intro(request):
    return render(request, 'str_intro.html')

def str_game(request):
    return render(request, 'str_game.html')

def str_end(request):
    score = request.POST.get('score', 0)
    target = request.POST.get('target', 50)
    user = request.user
    game = Game.objects.get(name = "Sort the Recycling")

    existing_score = GameScore.objects.filter(user=user, game=game).first()
    if existing_score:
        # If the score exists, check if the new score is higher
        if int(score) > int(existing_score.score):
            # If the new score is higher, update the existing entry
            existing_score.score = score
            existing_score.save()
    else:
        game_score = GameScore(user=user, game=game, score=score)
        game_score.save()
        form = NewGameScore()
        if form.is_valid():
            form.save()

    return render(request, 'str_end.html', {'score': score, 'target': target})
### STR VIEWS END ###


### RR VIEWS START ###
def recycle_rush_intro(request):
    return render(request, 'recycle_rush_intro.html')

def recycle_rush_game(request):
    return render(request, 'recycle_rush_game.html')

def recycle_rush_end(request):
    score = request.POST.get('score', 0)
    target = request.POST.get('target', 10)
    user = request.user
    game = Game.objects.get(name = "Recycle Rush")

    existing_score = GameScore.objects.filter(user=user, game=game).first()
    if existing_score:
        # If the score exists, check if the new score is higher
        if int(score) > int(existing_score.score):
            # If the new score is higher, update the existing entry
            existing_score.score = score
            existing_score.save()
    else:
        game_score = GameScore(user=user, game=game, score=score)
        game_score.save()
        form = NewGameScore()
        if form.is_valid():
            form.save()

    return render(request, 'recycle_rush_end.html', {'score': score, 'target': target})
### RR VIEWS END ###


### SS VIEWS START ###
def sea_sweepers_intro(request):
    return render(request, 'sea_sweepers_intro.html')

def sea_sweepers_game(request):
    return render(request, 'sea_sweepers_game.html')

def sea_sweepers_end(request):
    return render (request, 'sea_sweepers_end.html' )

### SS VIEWS END ###


### WAW VIEWS START ###
def whack_a_waste_intro(request):
    return render(request, 'whack_a_waste_intro.html')

def whack_a_waste_game(request):
    return render(request, 'whack_a_waste_game.html')

def whack_a_waste_end(request):
    # Handling POST request to save the score
    if request.method == 'POST':
        score = int(request.POST.get('score', 0))  # Ensure score is an integer
        
        user = request.user
        game = Game.objects.get(name="Whack-A-Waste")

        existing_score = GameScore.objects.filter(user=user, game=game).first()

        if existing_score:
            # If there's an existing score, update it if the new score is higher
            if score > existing_score.score:
                existing_score.score = score
                existing_score.save()
        else:
            # If no existing score, create a new GameScore entry
            GameScore.objects.create(user=user, game=game, score=score)

        return JsonResponse({'message': 'Score saved successfully'})

    # Handling GET request to display the game end page with the score
    score = int(request.GET.get('score', 0))  # Ensure the score is an integer

    return render(request, 'whack_a_waste_end.html', {'score': score})


### WAW VIEWS END

# View to handle saving the score for the games.
# This view is triggered by a POST request with the user's score in JSON format.
# It checks if the user has an existing score for the game:
# - If a score exists and the new score is higher, it updates the score.
# - If no score exists, it creates a new score entry.
# It returns a JSON response with the success or error message.

@login_required
def save_score(request):
    if request.method == 'POST':
        try:
            # Get the score from the request body
            data = json.loads(request.body)
            score = data.get('score')

            # Get the game object for "Whack-A-Waste"
            game = Game.objects.get(name="Whack-A-Waste")

            # Get the user from the request (assuming user is logged in)
            user = request.user

            # Check if a score already exists for the user and game
            existing_score = GameScore.objects.filter(user=user, game=game).first()
            if existing_score:
                # If the score exists, check if the new score is higher
                if int(score) > int(existing_score.score):
                    existing_score.score = score
                    existing_score.save()
            else:
                # Create a new GameScore entry
                GameScore.objects.create(user=user, game=game, score=score)

            return JsonResponse({'status': 'success', 'message': 'Score saved successfully'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
