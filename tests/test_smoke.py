from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from rsi_chaik_bot import __version__
from rsi_chaik_bot.app import main


def test_package_metadata_exposed() -> None:
    assert __version__


def test_entrypoint_is_callable() -> None:
    assert callable(main)
