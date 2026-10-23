"""
text to speech by espeak

__author__ = "vci"
__copyright__ = "Copyright 2026, vci
__license__ = "MIT
__version__ = "1.0.0.10"
__maintainer__ = "vci"
__email__ = "modernui.app@gmail.com"
__status__ = "development"
__reference__ = "vci"

"""
    
from audiohub.shared.i_tts_proc import AbcTTSProc
import espeakng


class TTSProc(AbcTTSProc):
    """
    text to speech
    AbcTTSProc implementation
    """

    def __init__(self, tts_proc_lib: AbcTTSProc | None = None):
        self.ttslib = tts_proc_lib

    def text_to_speech(self, text: str, file_out: str, **kvargs) -> None:
        """
        text to speech using especk-ng
        :param text: text input
        :param file_out: file to save speech result
        :param kvargs: optional
        :return: None
        """
        # pass
        ttsobj = espeakng.Speaker()
        voice = 'en'
        wpm = 60
        # apply attributes
        if "voice" in kvargs:
            voice = kvargs['voice']
        if "wpm" in kvargs:
            wpm = kvargs['wpm']
        ttsobj.voice = voice
        ttsobj.wpm = wpm
        ttsobj.say(text, wait4prev=True, export_path=file_out)
