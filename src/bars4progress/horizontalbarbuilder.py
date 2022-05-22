class HorizontalBarBuilder:
	"""
	Creates an horizontal progress bar object.
	Args:
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