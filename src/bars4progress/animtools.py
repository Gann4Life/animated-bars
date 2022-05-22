def spin(ascii_art: str, shift: int): 
	"""Shifts the (one line) ascii art by the given index."""
	return ascii_art[shift:] + ascii_art[:shift]