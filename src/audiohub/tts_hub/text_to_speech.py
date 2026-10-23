"""
TTS processing - text to speech

this module contains classes for TTS processing for text to speech

__author__ = "vci"
__copyright__ = "Copyright 2026, vci"
__license__ = "MIT"
__version__ = "1.0.0.10"
__maintainer__ = "vci"
__email__ = "modernui.app@gmail.com"
__status__ = "development"
__reference__ = "tts processing libraries"

"""

from audiohub.shared.i_tts_proc import AbcTTSProc

class TTSProcessingTextToSpeech(AbcTTSProc):
    """
    process TTS text to speech using the injected library
    """

    def __init__(self, tts_lib: AbcTTSProc):
        self.ttsobj = tts_lib

    def text_to_speech(self, text, file_out, **kvargs) -> None:
        """
        text to speech using the injected library
        :param text: text input
        :param file_out: saved result
        :return: None
        """
        self.ttsobj.text_to_speech(text, file_out, **kvargs)