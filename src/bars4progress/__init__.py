from progressbar import ProgressBar
from animatedbarbuilder import AnimatedBarBuilder
from templates import animations

anim = AnimatedBarBuilder(animations[0])

a = ProgressBar(animated_bar, on_finish=lambda: print("yeeha"))