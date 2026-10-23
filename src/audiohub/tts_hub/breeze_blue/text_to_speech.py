"""
text to speech by breeze blue

__author__ = "vci"
__copyright__ = "Copyright 2026, vci"
__license__ = "MIT"
__version__ = "1.0.0.10"
__maintainer__ = "vci"
__email__ = "modernui.app@gmail.com"
__status__ = "development"
__reference__ = "vci"

"""

# from turtle import save

from audiohub.shared.i_tts_proc import AbcTTSProc
from audiohub.shared.vars import BREEZE_BLUE_VARS
import os
from pathlib import Path
from breeze_blue import BreezeBlue, save

class TTSProc(AbcTTSProc):
    """
    text to speech using breeze blue
    AbcTTSProc implementation
    """

    def __init__(self, tts_proc_lib: AbcTTSProc | None = None):
        self.ttslib = tts_proc_lib

    def text_to_speech(self, text: str, file_out: str, **kvargs) -> None:
        """
        text to speech using breeze blue
        :param text: text input
        :param file_out: file to save speech result
        :param kvargs: optional
        :return: None
        """
        # pass

        api_key = os.getenv(BREEZE_BLUE_VARS.get("API_KEY", "") )
        print(f"breeze blue api key: {api_key}")
        client = BreezeBlue(api_key=api_key)

        # # display voice id/name
        # voices = client.voices.search(search="narrator")
        # print([(v["voice_id"], v["name"]) for v in voices["voices"]])

        # voice variables
        # voicd_id = "voc_xeh3w54cqvnp"
        voice_id = "voc_chrdprqdsytw" # ava

        audio = client.text_to_speech.convert(
            voice_id=voice_id,
            text= text,
            model_id="breeze-tts-2",
            output_format="mp3",
        )

        save(audio, file_out)
