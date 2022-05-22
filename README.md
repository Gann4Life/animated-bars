# bars4progress

Simple and customizable animated progress bars for python.

It allows you to create your own ascii one-line animations and horizontal progress bars.

### Importing
> `from progress_bar import ProgressBar`<br>
> Imports the ProgressBar class which handles animations to display progress.

> `from progressbar_builder import ProgressBarBuilder, Templates`<br>
> Imports the animation utilities and some templates.

### Animations

Before using, we have to setup an animated object.
We can do so with the `ProgressBarBuilder` class.

`progressbar = ProgressBarBuilder(frames)`

`frames` is a list of strings that the ProgressBarBuilder will use as loop animations. In this case, we can use the `Templates` class so we don't have to make one ourselves (although we can).
We can get a template with `Templates.animations()[index]`.

```py
# -1 to get the last animation
frames = Templates.animations()[-1]
progressbar = ProgressBarBuilder(frames)
```

`ProgressBarBuilder` requires you to pass an event when the process finishes. You can add `on_finish=my_function` as argument to the class.

```py
def my_function():
    print("This will run when the progress finishes.")

# -1 to get the last animation
frames = Templates.animations()[-1]
progressbar = ProgressBarBuilder(frames, on_finish=my_function)
```