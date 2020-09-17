# A simple presentation framework for my IT Tools presentations
No such tool existed, so I made it myself

### Features
* Markdown-based (with some extra features)
* Compiles into a [Reveal.js](https://revealjs.com/) presentation
* Can embed [Asciinema](https://asciinema.org/) for animated terminal examples

### See it in action

![demo gif](./presentation_framework/demo.gif)

# Installation
* optional - create a virtual environment (`virtualenv venv`)
* `pip install -r requirements.txt`

# Writing your own presentations
Refer to already existing presentations in the `markdown` folder,
the syntax is simple AF.

# Building presentations
## The simple, but tedious way
* Create a a file with your presentation in the `markdown` folder
* `python prometheus.py -i markdown/your_presentation_here.md`

It only builds the presentation **once**, you have to rerun the command each time
you change the `.md` file

## The better way (with autoreload), but requires the [`entr`](http://eradman.com/entrproject/) utility
* Same as before, create a file with your presentation in the `markdown`
* `./live_compile.sh markdown/your_presentation_here.md`

The script will watch for the changes in your file and reload the presentation
each time you save the file. `ctrl-c` to stop.
