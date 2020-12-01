from ezprez.core import *
from ezprez.components import *

# Remember this example has EVERYTHING from ezprez in it

# Get setup
slide_1 = Slide("First get ezprez installed", "windows", Code("shell", "> pip install ezprez"), "mac/linux", Code("shell", "$ sudo pip3 install ezprez"), "or add it to your python project", Code("python", "# Inside setup.py\nsetuptools.setup(\n...# Other code\ninstall_requires=['ezprez']\n... # Other code\n)"))

# Basic text slide
slide_2 = Slide("This is the most basic slide...", "It's just text nothing more")

# Links
slide_3 = Slide("You can also add links", "Like this one", Link("to my website", "https://kieranwood.ca"))

# Basic List slide
slide_4 = Slide("A bit fancier", "We can also do lists for any longer content needed", ["With", "Several", "items"])

# Alignment https://webslides.tv/demos/components#slide=14
slide_5 = Slide("We can also re-align content horizontally...", Code("Python", "from ezprez.core import Slide\nSlide(heading, *contents, horizontal_alignment='left')"), horizontal_alignment='left')
slide_6 = Slide("...and vertically", Code("Python", "from ezprez.core import Slide\nSlide(heading, *contents, vertical_alignment='top')"), vertical_alignment='top')
slide_7 = Slide("Porque no los dos", Code("Python", "from ezprez.core import Slide\nSlide(heading, *contents, horizontal_alignment='right', vertical_alignment='bottom')"), horizontal_alignment='right', vertical_alignment='bottom')

# Colors https://webslides.tv/demos/components#slide=27
slide_8 = Slide("You can also change the background color", Link("Here are the available colors (on those slides it says 'bg-color', just use 'color' i.e. 'bg-black' becomes 'black')", "https://webslides.tv/demos/components#slide=27"), Code("python", "from ezprez.core import Slide\nSlide(heading, *contents, background='black')"), background='black')

# Footers
foot = Footer([[SocialLinks.github,"https://github.com/Descent098/ezprez-example"]])

slide_9 = Slide("You can add footers (like in the bottom left)...", Code("python", "from ezprez.core import Presentation\nfrom ezprez.components import Footer, SocialLinks\nfoot = Footer([[SocialLinks.github,'https://github.com/Descent098/ezprez-example']])\nPresentation(title, description, slides, footer=foot)"))

# Navigation
nav = Navbar("ezprez Demo", [[SocialLinks.github,"https://github.com/Descent098/ezprez"], [SocialLinks.youtube, "https://www.youtube.com/channel/UC1-WbwQ1sAVZ3AVmrXcBwGw"]])
slide_10 = Slide("..and add navbars (move your mouse to the top)", Code("python", "from ezprez.core import Presentation\nfrom ezprez.components import Navbar, SocialLinks\nnav = Navbar('ezprez Demo', [[SocialLinks.github,'https://github.com/Descent098/ezprez'], [SocialLinks.youtube, 'https://www.youtube.com/channel/UC1-WbwQ1sAVZ3AVmrXcBwGw']])\nPresentation(title, description, slides, navbar=nav)"))

# Why
slide_11 = Slide("Why should I use this?", "The python source code for this presenation is 18 lines", "The html it produced is 251")

# Add all the slides to a list
slides = [slide_1, slide_2,slide_3, slide_4, slide_5, slide_6, slide_7, slide_8, slide_9, slide_10]

# Setup the presentation
prez = Presentation("Welcome to this example Presentation", "This will give you a taste of what ezprez can do, and how to use it", "https://kieranwood.ca/ezprez-example", slides, navbar=nav, footer=foot)

# Export the files to the current directory
prez.export(".", force=True)
