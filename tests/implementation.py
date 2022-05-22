from time import sleep
from progress_bar import ProgressBar
from progressbar_builder import ProgressBarBuilder, HorizontalBar, Templates

on_finish = lambda: print("\nFinished... right?")

animated_bar = ProgressBarBuilder(Templates.animations()[2])
horizontal_bar = Templates.horizontal_bars()[4]
progressbar = ProgressBar(animated_bar, on_finish, frame_interval=0.1)

def charge_up():
    for i in range(100+1):
        value = i/100
        progressbar.display_progress(value, horizontal_bar.make_fill(value, "{0}"))
        sleep(1)
    
progressbar.start(run_process=charge_up)