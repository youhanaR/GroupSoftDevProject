# Author: Jem Challis, Rami Youhana

from django.shortcuts import render
from .forms import NewGameScore
from .models import GameScore
from core.models import Minigame
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
import json

### STR VIEWS START ###
@login_required
def str_intro(request):
    return render(request, 'str_intro.html')

@login_required
def str_game(request):
    return render(request, 'str_game.html')

@login_required
def str_end(request):
    score = request.POST.get('score', 0)
    target = request.POST.get('target', 50)
    user = request.user
    game = Minigame.objects.get(name = "Sort The Recycling")

    existing_score = GameScore.objects.filter(user=user, minigame=game).first()
    if existing_score:
        # If the score exists, check if the new score is higher
        if int(score) > int(existing_score.score):
            # If the new score is higher, update the existing entry
            existing_score.score = score
            existing_score.save()
    else:
        game_score = GameScore(user=user, minigame=game, score=score)
        game_score.save()
        form = NewGameScore()
        if form.is_valid():
            form.save()

    return render(request, 'str_end.html', {'score': score, 'target': target})
### STR VIEWS END ###


### RR VIEWS START ###
@login_required
def recycle_rush_intro(request):
    return render(request, 'recycle_rush_intro.html')

@login_required
def recycle_rush_game(request):
    return render(request, 'recycle_rush_game.html')

@login_required
def recycle_rush_end(request):
    score = request.POST.get('score', 0)
    target = request.POST.get('target', 10)
    user = request.user
    game = Minigame.objects.get(name = "Recycle Rush")

    existing_score = GameScore.objects.filter(user=user, minigame=game).first()
    if existing_score:
        # If the score exists, check if the new score is higher
        if int(score) > int(existing_score.score):
            # If the new score is higher, update the existing entry
            existing_score.score = score
            existing_score.save()
    else:
        game_score = GameScore(user=user, minigame=game, score=score)
        game_score.save()
        form = NewGameScore()
        if form.is_valid():
            form.save()

    return render(request, 'recycle_rush_end.html', {'score': score, 'target': target})
### RR VIEWS END ###


### SS VIEWS START ###
@login_required
def sea_sweepers_intro(request):
    return render(request, 'sea_sweepers_intro.html')

@login_required
def sea_sweepers_game(request):
    return render(request, 'sea_sweepers_game.html')

@login_required
def sea_sweepers_end(request):
    # Handling POST request to save the score
    if request.method == 'POST':
        score = int(request.POST.get('score', 0))
        user = request.user
        game = Minigame.objects.get(name="Sea Sweepers")  # Ensure your game name is correct

        existing_score = GameScore.objects.filter(user=user, minigame=game).first()
        if existing_score:
            # Update the score only if the new score is higher
            if score > existing_score.score:
                existing_score.score = score
                existing_score.save()
        else:
            # Create a new GameScore record if none exists
            GameScore.objects.create(user=user, minigame=game, score=score)

        return JsonResponse({'message': 'Score saved successfully'})

    # Handling GET request: display the game end page with the score
    score = int(request.GET.get('score', 0))
    return render(request, 'sea_sweepers_end.html', {'score': score})

### SS VIEWS END ###


### WAW VIEWS START ###
@login_required
def whack_a_waste_intro(request):
    return render(request, 'whack_a_waste_intro.html')

@login_required
def whack_a_waste_game(request):
    return render(request, 'whack_a_waste_game.html')

@login_required
def whack_a_waste_end(request):
    # Handling POST request to save the score
    if request.method == 'POST':
        score = int(request.POST.get('score', 0))  # Ensure score is an integer
        
        user = request.user
        game = Minigame.objects.get(name="Whack A Waste")

        existing_score = GameScore.objects.filter(user=user, minigame=game).first()

        if existing_score:
            # If there's an existing score, update it if the new score is higher
            if score > existing_score.score:
                existing_score.score = score
                existing_score.save()
        else:
            # If no existing score, create a new GameScore entry
            GameScore.objects.create(user=user, minigame=game, score=score)

        return JsonResponse({'message': 'Score saved successfully'})

    # Handling GET request to display the game end page with the score
    score = int(request.GET.get('score', 0)) 

    return render(request, 'whack_a_waste_end.html', {'score': score})


### WAW VIEWS END



### SNS VIEWS

def sns_intro(request):
    return render(request, 'sns_intro.html')

def sns_game(request):
    return render(request, 'sns_game.html')

def sns_end(request):
    user = request.user
    game = Minigame.objects.get(name="Sort N Serve")

    if request.method == 'POST':
        score = int(request.POST.get('score', 0))
    else:
        score = int(request.GET.get('score', 0))

    if score:
        existing_score = GameScore.objects.filter(user=user, minigame=game).first()

        if existing_score:
            if score > existing_score.score:
                existing_score.score = score
                existing_score.save()
        else:
            GameScore.objects.create(user=user, minigame=game, score=score)

    if request.method == 'POST':
        return JsonResponse({'message': 'Score saved successfully'})

    return render(request, 'sns_end.html', {'score': score})


### SAS VIEWS END ###


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
            game = Minigame.objects.get(name="Whack A Waste")

            # Get the user from the request (assuming user is logged in)
            user = request.user

            # Check if a score already exists for the user and game
            existing_score = GameScore.objects.filter(user=user, minigame=game).first()
            if existing_score:
                # If the score exists, check if the new score is higher
                if int(score) > int(existing_score.score):
                    existing_score.score = score
                    existing_score.save()
            else:
                # Create a new GameScore entry
                GameScore.objects.create(user=user, minigame=game, score=score)

            return JsonResponse({'status': 'success', 'message': 'Score saved successfully'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)