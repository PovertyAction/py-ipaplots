"""ipaplots - A matplotlib style package for creating IPA-themed plots."""

import os
from pathlib import Path
import matplotlib.pyplot as plt

__version__ = "0.0.1"

# Get the path to the styles directory
_STYLE_DIR = Path(__file__).parent / "styles"
_STYLE_FILE = _STYLE_DIR / "ipaplots.mplstyle"

# Register the style with matplotlib
if _STYLE_FILE.exists():
    plt.style.library["ipaplots"] = str(_STYLE_FILE)
else:
    import warnings
    warnings.warn(f"Could not find ipaplots style file at {_STYLE_FILE}")

def load_style():
    """Load the ipaplots style."""
    if "ipaplots" in plt.style.library:
        plt.style.use("ipaplots")
    else:
        raise ValueError("ipaplots style not found in matplotlib style library")