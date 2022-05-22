# bars4progress

Simple and customizable animated progress bars for python.

It allows you to create your own ascii one-line animations and horizontal progress bars.

*Script example*
```py
"""
bars4progress 0.1.3 - Example 1 only with animations.
"""

from time import sleep

# Importing animation templates
from bars4progress.templates import animations

# Importing the animation builder class
from bars4progress.animatedbarbuilder import AnimatedBarBuilder

# Importing the progress bar main class
from bars4progress.progressbar import ProgressBar

# PART OF STEP 4_
def process_with_progress():
    """
    This is our secondary process.
    We can download a file for example and display its progress.
    """

    # If the progressbar gets stuck, try adding an extra value like +1 or +0.1
    for i in range(100+1):
        # Add some delay to see progress over time
        sleep(0.1)

        # STEP 5_ We need to display a progress between 0 and 1 (progressbar's max_value parameter)
        #         For the second argument we can pass a string containing the actual human-readable progress
        progressbar.display_progress(i/100, "Bar description... {0}")

# PART OF STEP 3_
def my_finish_function():
    print("\Everything seems to be fine. :)")

# STEP 1_ Create our animation frames
animation = animations[-1]

# STEP 2_ Create our animated object
animbar = AnimatedBarBuilder(animation)

# STEP 3_ Create our progress bar and pass the animated object we created.
#         Also don't forget pass your function to know when the progress finishes
# The progress is considered finished once the progressbar's progress values is higher than its max_value parameter.
progressbar = ProgressBar(animbar, my_finish_function)

# STEP 4_ Start progress
#         Pass a function that will execute your main task and set the progressbar's progress there.
progressbar.start(process_with_progress)
```