
"""
interface for Test-to-speech processing

__author__ = "vci"
__copyright__ = "Copyright 2026, vci"
__license__ = "MIT"
__version__ = "1.0.0.10"
__maintainer__ = "vci"
__email__ = "modernui.app@gmail.com"
__status__ = "development"
__reference__ = "vci"

"""

from abc import ABC, abstractmethod

class AbcTTSProc(ABC):
    """
    contains abstract methods for TTS related tasks
    """

    @abstractmethod
    def text_to_speech(self, text: str, file_out: str, **kvargs) -> None:
        """
        converts text to speech
        :param text: text input
        :param file_out: save-to file
        :param **Kvargs: name/value pairs

        the method is to be implemented by class
        """
        pass