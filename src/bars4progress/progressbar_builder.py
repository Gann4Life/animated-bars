import sys

def spin(ascii_art: str, shift: int): 
	"""Shifts the (one line) ascii art by the given index."""
	return ascii_art[shift:] + ascii_art[:shift]

class ProgressBarBuilder:
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

class HorizontalBar:
	"""Creates an horizontal progress bar.
	params:
		length: __int__ - The length of the progress bar.
		fill_symbol: __str__ - The string or character that's going to fill over progress.
		empty_symbol: __str__ - The string or character that symbolizes empty/remaining progress.
		formatting: __str__ - How the information is going to be displayed.
	"""

	def __init__(self, length = 10, fill_symbol="#", empty_symbol=" ", formatting="[{fill}{space}] {progress}%"):
		self.length = length
		self.fill_symbol = fill_symbol
		self.empty_symbol = empty_symbol
		self.formatting = formatting
	
	def make_fill(self, value: float, progress: str) -> str:
		"""Returns a formatted horizontal progress bar with a fill based on the given value."""
		char_progress = round(value * self.length)
		return self.formatting.format(
			fill=self.fill_symbol * char_progress,
			space=self.empty_symbol * (self.length - char_progress),
			progress=progress
		)

class Templates:
	"""Available options: 
		Templates.animations()[index]
		Templates.horizontal_bars()[index]	
	"""
	
	def horizontal_bars():
		return [
			HorizontalBar(),
			HorizontalBar(fill_symbol="/", empty_symbol=" "),
			HorizontalBar(fill_symbol="/", empty_symbol="-"),
			HorizontalBar(fill_symbol="█", empty_symbol=" ", formatting="{fill}{space} {progress}%"),
			HorizontalBar(fill_symbol="█", empty_symbol="▒", formatting="{fill}{space} {progress}%"),
			HorizontalBar(fill_symbol="▐", empty_symbol=" ", formatting="{fill}{space} {progress}%"),
			HorizontalBar(fill_symbol="▐", empty_symbol="▒", formatting="{fill}{space} {progress}%"),
			HorizontalBar(fill_symbol="<", empty_symbol="-", formatting="[{space}{fill}] {progress}% (Reverse c:)"),
		]
		
	def animations(): 
		return [
			["(O w O) {0}",
			"(ow O ) {0}",
			"(w O  ) {0}",
			"(wO   ) {0}",
			"(o    ) {0}",
			"(     ) {0}",
			"(    -) {0}",
			"(   - ) {0}",
			"(  -  ) {0}",
			"( -   ) {0}",
			"(-    ) {0}",
			"(     ) {0}",
			"(    o) {0}",
			"(   Ow) {0}",
			"(  O w) {0}",
			"( O w ) {0}"],

			["["+spin("▁ ▂ ▃ ▄ ▅ ▆ ▇ █ ▇ ▆ ▅ ▄ ▃ ", 0*2)+"] {0}",
			"["+spin("▁ ▂ ▃ ▄ ▅ ▆ ▇ █ ▇ ▆ ▅ ▄ ▃ ", -1*2)+"] {0}",
			"["+spin("▁ ▂ ▃ ▄ ▅ ▆ ▇ █ ▇ ▆ ▅ ▄ ▃ ", -2*2)+"] {0}",
			"["+spin("▁ ▂ ▃ ▄ ▅ ▆ ▇ █ ▇ ▆ ▅ ▄ ▃ ", -3*2)+"] {0}",
			"["+spin("▁ ▂ ▃ ▄ ▅ ▆ ▇ █ ▇ ▆ ▅ ▄ ▃ ", -4*2)+"] {0}",
			"["+spin("▁ ▂ ▃ ▄ ▅ ▆ ▇ █ ▇ ▆ ▅ ▄ ▃ ", -5*2)+"] {0}",
			"["+spin("▁ ▂ ▃ ▄ ▅ ▆ ▇ █ ▇ ▆ ▅ ▄ ▃ ", -6*2)+"] {0}",
			"["+spin("▁ ▂ ▃ ▄ ▅ ▆ ▇ █ ▇ ▆ ▅ ▄ ▃ ", -7*2)+"] {0}",
			"["+spin("▁ ▂ ▃ ▄ ▅ ▆ ▇ █ ▇ ▆ ▅ ▄ ▃ ", -8*2)+"] {0}",
			"["+spin("▁ ▂ ▃ ▄ ▅ ▆ ▇ █ ▇ ▆ ▅ ▄ ▃ ", -9*2)+"] {0}",
			"["+spin("▁ ▂ ▃ ▄ ▅ ▆ ▇ █ ▇ ▆ ▅ ▄ ▃ ", -10*2)+"] {0}",
			"["+spin("▁ ▂ ▃ ▄ ▅ ▆ ▇ █ ▇ ▆ ▅ ▄ ▃ ", -11*2)+"] {0}",
			"["+spin("▁ ▂ ▃ ▄ ▅ ▆ ▇ █ ▇ ▆ ▅ ▄ ▃ ", -12*2)+"] {0}"],

			["[" + spin("⠁⠂⠄⡀⢀⠠⠐⠈", 0) + "] {0}",
			"[" + spin("⠁⠂⠄⡀⢀⠠⠐⠈", -1) + "] {0}",
			"[" + spin("⠁⠂⠄⡀⢀⠠⠐⠈", -2) + "] {0}",
			"[" + spin("⠁⠂⠄⡀⢀⠠⠐⠈", -3) + "] {0}",
			"[" + spin("⠁⠂⠄⡀⢀⠠⠐⠈", -4) + "] {0}",
			"[" + spin("⠁⠂⠄⡀⢀⠠⠐⠈", -5) + "] {0}",
			"[" + spin("⠁⠂⠄⡀⢀⠠⠐⠈", -6) + "] {0}",
			"[" + spin("⠁⠂⠄⡀⢀⠠⠐⠈", -7) + "] {0}"],
			
			["[▁ ▁ ▁] {0}",
			"[▂ ▁ ▁] {0}",
			"[▃ ▁ ▁] {0}",
			"[▄ ▁ ▁] {0}",
			"[▅ ▁ ▁] {0}",
			"[▆ ▁ ▁] {0}",
			"[▇ ▁ ▁] {0}",
			"[█ ▁ ▁] {0}",
			"[▇ ▁ ▁] {0}",
			"[▆ ▁ ▁] {0}",
			"[▅ ▁ ▁] {0}",
			"[▄ ▁ ▁] {0}",
			"[▃ ▁ ▁] {0}",
			"[▂ ▁ ▁] {0}",
			"[▁ ▁ ▁] {0}",
			"[▁ ▂ ▁] {0}",
			"[▁ ▃ ▁] {0}",
			"[▁ ▄ ▁] {0}",
			"[▁ ▅ ▁] {0}",
			"[▁ ▆ ▁] {0}",
			"[▁ ▇ ▁] {0}",
			"[▁ █ ▁] {0}",
			"[▁ ▇ ▁] {0}",
			"[▁ ▆ ▁] {0}",
			"[▁ ▅ ▁] {0}",
			"[▁ ▄ ▁] {0}",
			"[▁ ▃ ▁] {0}",
			"[▁ ▂ ▁] {0}",
			"[▁ ▁ ▁] {0}",
			"[▁ ▁ ▂] {0}",
			"[▁ ▁ ▃] {0}",
			"[▁ ▁ ▄] {0}",
			"[▁ ▁ ▅] {0}",
			"[▁ ▁ ▆] {0}",
			"[▁ ▁ ▇] {0}",
			"[▁ ▁ █] {0}",
			"[▁ ▁ ▇] {0}",
			"[▁ ▁ ▆] {0}",
			"[▁ ▁ ▅] {0}",
			"[▁ ▁ ▄] {0}",
			"[▁ ▁ ▃] {0}",
			"[▁ ▁ ▂] {0}"]
		]