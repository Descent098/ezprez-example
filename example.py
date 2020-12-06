from ezprez.core import *
from ezprez.components import *

# Remember this example has EVERYTHING from ezprez in it

# Get setup
Slide("First get ezprez installed", "windows", Code("shell", "> pip install ezprez"), "mac/linux", Code("shell", "$ sudo pip3 install ezprez"), "or add it to your python project", Code("python", "# Inside setup.py\nsetuptools.setup(\n...# Other code\ninstall_requires=['ezprez']\n... # Other code\n)"))
Slide("Then setup the boilerplate", "Here's your hello world!", Code("python", "from ezprez.core import Slide, Presentation\nfrom ezprez.components import *\n\nSlide('Hello World!', 'Welcome to ezprez')\nprez = Presentation('Hello world presentation', 'This is the most basic presenation', 'https://example.com/url')\nprez.export('.', force=True)"))

# Table of contents
sections = {"Setup":2, "Links":6, "Lists":7, "Alignment":8, "Colors":11, "Footers":13, "Navbars":14, "Icons":15, "Buttons": 16, "Videos": 17, "Raw HTML":18}
Slide("Table of contents", TableOfContents(sections))

# Basic text slide
Slide("This is the most basic slide...", "It's just text nothing more")

# Links
Slide("You can also add links", "Like this one", Link("to my website", "https://kieranwood.ca"))

# Basic List slide
Slide("A bit fancier", "We can also do lists for any longer content needed", ["With", "Several", "items"])

# Alignment https://webslides.tv/demos/components#slide=14
Slide("We can also re-align content horizontally...", Code("Python", "from ezprez.core import Slide\nSlide(heading, *contents, horizontal_alignment='left')"), horizontal_alignment='left')
Slide("...and vertically", Code("Python", "from ezprez.core import Slide\nSlide(heading, *contents, vertical_alignment='top')"), vertical_alignment='top')
Slide("Porque no los dos", Code("Python", "from ezprez.core import Slide\nSlide(heading, *contents, horizontal_alignment='right', vertical_alignment='bottom')"), horizontal_alignment='right', vertical_alignment='bottom')

# Colors https://webslides.tv/demos/components#slide=27
Slide("You can also change the background color", Link("Here are the available colors (on those slides it says 'bg-color', just use 'color' i.e. 'bg-black' becomes 'black')", "https://webslides.tv/demos/components#slide=27"), Code("python", "from ezprez.core import Slide\nSlide(heading, *contents, background='black')"), background='black')
Slide("You can also set a default background color for the whole presentation", Code("python", "from ezprez.core import Presentation\nfrom ezprez.components import *\n\nPresentation(title, description, url, background=color)"))

# Footers
foot = Footer([SocialLink.github.link("https://github.com/Descent098/ezprez-example")])
Slide("You can add footers (like in the bottom left)...", Code("python", "from ezprez.core import Presentation\nfrom ezprez.components import Footer, SocialLinks\nfoot = Footer([[SocialLinks.github,'https://github.com/Descent098/ezprez-example']])\nPresentation(title, description, slides, footer=foot)"))

# Navigation
nav = Navbar("ezprez Demo", [SocialLink.github.link("https://github.com/Descent098/ezprez"), SocialLink.youtube.link("https://www.youtube.com/channel/UC1-WbwQ1sAVZ3AVmrXcBwGw")])
Slide("..and add navbars (move your mouse to the top)", Code("python", "from ezprez.core import Presentation\nfrom ezprez.components import Navbar, SocialLinks\nnav = Navbar('ezprez Demo', [[SocialLinks.github,'https://github.com/Descent098/ezprez'], [SocialLinks.youtube, 'https://www.youtube.com/channel/UC1-WbwQ1sAVZ3AVmrXcBwGw']])\nPresentation(title, description, slides, navbar=nav)"))

# Icons
Slide("ezprez", Icon("fa-heart", size="15px"), Link("'s icons...", "https://fontawesome.com"))

# buttons
Slide("And buttons..", Button("Like this", "#"), Button("Or different colors", "#", color="#141414"), Button("Or one's with icons", "#", icon=Icon("fa-heart", size="15px")), Button("or Ghost style, and without rounding", "#", ghost=True, rounding=False))

# Videos
Slide("Even youtube videos work", Video("wSVljLh1VmI"))

# Raw
Slide("And in those sticky situations, you can add raw html", Raw("<h3><strong><em>Like this</em></strong></h3>"))

# Why
Slide("Why should I use this?", "The python source code for this presenation is 25 lines", "The html it produced is 418 lines", Icon("fa-thumbs-up"))

# Setup the presentation
prez = Presentation("Welcome to this example Presentation", "This will give you a taste of what ezprez can do, and how to use it", "https://kieranwood.ca/ezprez-example", navbar=nav, footer=foot)

# Export the files to the current directory at /Presentation
prez.export(".", force=True, folder_name="Presentation")
