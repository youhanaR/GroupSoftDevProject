# Author: Jem Challis

from django.shortcuts import render
from .forms import NewGameScore
from .models import GameScore, Game

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
