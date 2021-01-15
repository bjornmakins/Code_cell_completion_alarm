# Credit due: James Dietle (mindtrinket)
# Url: https://forums.fast.ai/t/sound-alerts-in-jupyter-for-code-completion-and-exceptions/4614

## Import up sound alert dependencies
from IPython.display import Audio, display

def allDone():
  display(Audio(url='https://www.youtube.com/watch?v=16b6RzPSdV8&ab_channel=ClaphamJunction', autoplay=True))
## Insert whatever audio file you want above
