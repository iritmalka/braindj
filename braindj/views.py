import json
from collections import deque
import random

from django.http import HttpResponse
import likeness_monitor
import player


SECONDS = 10


class JsonResponse(HttpResponse):

    def __init__(self, data, status=200):
        content = json.dumps(data, separators=(',', ':'))
        super(JsonResponse, self).__init__(
            content, content_type='application/json', status=status)


class SizedDeque(deque):
	def __init__(self, size=SECONDS):
		self.size = size
		deque.__init__(self)
	def append(self, attr):
		if len(self) == self.size:
			self.popleft()
		deque.append(self, attr)


class LikenessMonitor(object):
	def __init__(self, seconds=SECONDS):
		self.seconds = seconds
		self.likes = SizedDeque(seconds)

	def update(self, num):
		self.likes.append(num)

	def mean(self):
		return float(sum(self.likes)) / len(self.likes)

	def reset(self):
		self.likes = SizedDeque(self.seconds)

	def __repr__(self):
		return "Likes<%s>" % repr(self.likes)


class BrainDJ(object):
	def __init__(self):
		self.player = player.MacItunesPlayer()
		self.like_score = LikenessMonitor(SECONDS)

	def start(self):
		self.player.start_song()
		self.like_score.update(self.get_likeness_value())

	def next_song(self):
		self.player.next_song()
		self.like_score.reset()


dj = BrainDJ()

def state(request):
	return JsonResponse({'state': dj.like_score.mean()})

def play(request):
    player.start_song()

def next(request):
    player.next_song()

def pause(request):
    player.pause()

def get_current_song(request):
    return JsonResponse({'current_song': player.get_current_song()})
