import sys

class AnimatedBarBuilder:
	"""
	Created an animated bar object.
	"""

	def __init__(self, frames: list, frame_delay=0.1):
		self.frames = frames
		self.max_frames = len(frames)
		self.current_frame = 0
		
		self.value = 0

	def next_frame(self):
		"""Displays the next frame of the animation."""
		self.current_frame += 1
		if (self.current_frame > self.max_frames - 1):
			self.current_frame = 0
		self.__display_current_frame()

	def set_progress(self, value):
		"""Sets the progress value that formatted frames receive."""
		self.value = value

	def __display_current_frame(self):
		"""Displays the current frame of the animation."""
		self.__display_frame(self.current_frame)

	def __display_frame(self, frame: int):
		"""Displays the given frame."""
		sys.stdout.write(f"\r{self.__formatted_frames()[frame]}")
		sys.stdout.flush()

	def __formatted_frames(self):
		"""Returns all frames with formatted information without modifying original frames."""
		return [frame.format(self.value) for frame in self.frames]