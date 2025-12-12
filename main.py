from drafter import *
from drafter import add_website_header
from dataclasses import dataclass

@dataclass
class State:
    """
    If music is playing or not.
    
    Attributes:
        playing: bool
    """
    name: str

#############################################################################
# Website styling

set_site_information(
    author="your_email@udel.edu",
    description="""A brief description of what your website does.
    Use a triple quoted string if you want to span multiple lines.""",
    sources=["List any help resources or sources you used"],
    planning=["your_planning_document.pdf"],
    links=["https://github.com/your-username/your-repo"]
)
hide_debug_information()
set_website_title("Housewitching")
set_website_framed(False)

#Takes away default website styling
set_website_style("none")

#Custom website styling
add_website_css("""
body {
    background-color: #222222;
    color: White;
    font-size: 40px;
    font-family: "Papyrus", sans-serif;
    width: 960px;
    margin: 0 auto;
    text-align: center;
    line-height: 1.5;
    justify-content: center;
}

p {
    line-height: 1.5;
    color: White;
}

h1 {
    color: White;
}

img {
    display: block;
    margin: auto;
    width: 500;
    border: 15px solid White;
    border-radius: 30px;
    padding: 10px;
  
}

button {
    background-color: #656565;
    font-family: "Papyrus", sans-serif;
    font-size: 30px;
    color: White;
    text-align: center;
    border-radius: 30px;
    padding: 10px;
    border: 5px solid White;
}

input[type="text"] {
    background-color: #656565;
    font-family: "Papyrus", sans-serif;
    font-size: 30px;
    color: White;
    text-align: center;
    border-radius: 30px;
    padding: 10px;
    border: 5px solid White;
}
""")

#<!-- Content of your audioplayer.html file -->

add_website_header(
    """
    <audio controls autoplay loop muted>
        <source src="once_upon_a_time.mp3" type="audio/mpeg">
    </audio>
    """)

@route
def index(state: State) -> Page:
    """ The audio page. """
    return Page(state,[
        "Just Audio.",
        """<button onclick="toggleMute()">Mute | Unmute</button>""",
        ])

#############################################################################    
# Start server

start_server(State(
    True,
))
