# Python 'turtlex' Package

Python convenience functions to control turtle window appearance and behaviour.

## Installation

Install the package using PIP with:

```shell
$ pip install turtlex
```

## Usage
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
