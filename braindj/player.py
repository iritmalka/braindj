# import win32com.client
import subprocess

class Player(object):
	def start_song(self):
		pass
	def next_song(self):
		pass
	def get_current_song(self):
		pass
	def pause(self):
		pass


class MacItunesPlayer(Player):
	ITUNES_SHELL_PATH = './itunes.sh' # '~/bin/itunes.sh'
	AVILABE_CMDS = ['status', 'play', 'pause', 'next', 'prev', 'mute', 'unmute', 
					'stop', 'quit', 'vol up', 'vol down']

	@classmethod
	def run_cmd(cls, cmd):
		"""
		gets a command to put on itunes.sh script
		"""
		if cmd not in cls.AVILABE_CMDS:
			raise ValueError("cmd not available")

		sub = subprocess.Popen("%s %s" % (cls.ITUNES_SHELL_PATH, cmd), 
					shell=True, stdin=subprocess.PIPE, 
					stdout=subprocess.PIPE, stderr=subprocess.PIPE)

		return sub

	def start_song(self):
		self.run_cmd("play")

	def next_song(self):
		self.run_cmd("next")

	def get_current_song(self):
		sub = self.run_cmd("status")
		return sub.stdout.read()

	def pause(self):
		self.run_cmd("pause")


class WinItunesPlayer(Player):
	def __init__(self):
		import win32com.client
		self.itunes = win32com.client.Dispatch("iTunes.Application")

	def get_current_song(self):
		# self.itunes.CurrentTrack. (artists?)
		return self.itunes.CurrentTrack.Name

	def pause(self):
	    self.itunes.Pause()

	def start_song(self):
	    self.itunes.Play()

	def next_song(self):
	    self.itunes.Pause()
	    self.itunes.NextTrack()

	def close(self):
		self.itunes.Quit()

