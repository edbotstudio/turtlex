# Python 'turtlex' package

Python convenience functions to control turtle window appearance and behaviour.

## Installation

Install the package using PIP with:

```shell
$ pip install turtlex
```

## Usage
Let's just jump straight in to a turtle program using the turtlex front() function.

```python
import turtle                                   # we'll need the turtle package
import turtlex                                  # utils for window appearance and behaviour

screen = turtle.Screen()                        # 'screen' is our window
screen.title("Just wanted to say..")
screen.setup(500, 400)                          # set the window size in pixels
screen.bgcolor("lightgreen")                    # set the window background color

# Say hello!
turtle.write("Hello world!", font=("Courier", 30, "italic"), align="center")
turtle.hideturtle()

turtlex.front(screen, True)                     # keep on top of existing windows
screen.mainloop()                               # process window events
```

Easy! Here's the full list of functions.

### Functions in the turtlex package

```python
front(screen, alwaysAtFront=False)
```
Send the window to the top of the window stack. If 'alwaysAtFront' is true then keep the window at the front.

```python
fullscreen(screen, full=True)
```
Setting 'full' to true will make the window fullscreen.

```python
opacity(screen, alpha=0.5)
```
Set the opacity of the window by setting the alpha value (0 - 1).

```python
disabled(screen, disabled=True)
```
Set 'disabled' to true to disable window management functions including maximise, minimise, move & close.

```python
toolwindow(screen, tool=True)
```
Setting 'tool' to true changes the title bar decoration to a toolbar.

```python
noresize(screen, x=False, y=False)
```
Setting 'x' and 'y' to true prevents window resizing in the horizontal and vertical direction respectively.

```python
nodecorate(screen, nodecorate=True)
```
Setting 'nodecorate' to true removes the windows decoration including title bar.

```python
minsize(screen, width=None, height=None)
```
Set the minimum size of the window in pixels.

```python
maxsize(screen, width=None, height=None)
```
Set the maximum size of the window in pixels.

```python
minimise(screen)
minimize(screen)
```
Minimise the window.

```python
restore(screen)
```
Restore the window.

<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/edbotstudio/turtlex/issues) for a list of proposed features (and known issues).

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Go to https://github.com/edbotstudio/turtlex.
2. Fork the project.
3. Create your feature branch (`git checkout -b feature/AmazingFeature`).
4. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
5. Push to the branch (`git push origin feature/AmazingFeature`).
6. Open a pull request.

<!-- LICENCE -->
## Licence

Distributed under the MIT Licence. See the [LICENCE](../main/LICENCE) for more information.
