"""LiquidityWatch: Tracks liquidity pool changes for a pair and alerts on large moves."""

__version__ = "1.0.0"

from .core import run
from .cli import main

__all__ = ["main", "run", "__version__"]