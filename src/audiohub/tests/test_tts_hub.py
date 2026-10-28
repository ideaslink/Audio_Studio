"""
tests for text-to-speech processing

__author__ = "vci"
__copyright__ = "Copyright 2026, vci"
__license__ = "MIT"
__version__ = "1.0.0.10"
__maintainer__ = "vci"
__email__ = "modernui.app@gmail.com"
__status__ = "development"
__reference__ = "vci"

notes:

- use pytest: pytest
- use unittest: indiviual or all tests: python -m unittest src/audiohub/tests/test_tts_hub.py

"""

from audiohub.shared.i_tts_proc import AbcTTSProc # shared.i_tts_proc import AbcTTSProc
# from tts_hub.espeak import text_to_speech
# import audiohub.tts_hub.espeak
# import audiohub.tts_hub.breeze_blue

from audiohub.tts_hub.breeze_blue import text_to_speech as tts_breeze_blue
from audiohub.tts_hub.espeak import text_to_speech as tts_espeak
from audiohub.tts_hub.azure import text_to_speech as tts_azure
import audiohub.tts_hub.text_to_speech


import unittest
import pytest
import os
import sys
from pathlib import Path


class TTSUtilTest(unittest.TestCase):
    """
    unit test for TTS
    """

    def __init__(self, *args, **kvargs):
        super().__init__(*args, **kvargs)
        self.filepath = Path("assets/result-tts.wav")

    def setUp(self):
        pass

    @pytest.mark.skip(reason="skip this test for now")
    # @unittest.skip("skip this test for now")
    def test_text_to_speech(self):
        """
        test text to speech
        """
        # test tts with espeak-ng
        ttslib: AbcTTSProc = tts_espeak.TTSProc()  # audiohub.tts_hub.espeak.text_to_speech.TTSProc()
        # text = 'ni3 hao3, shi4 jie4!'
        # 'welcome 你好，欢迎来到上海！'
        text = "welcome to Miami of Florida, the sunshine state. Enjoy the beach and the sun!"
        data = {"region": "eastus", "wpm": 170}
        # ttslib.text_to_speech(text, file_out=self.filepath, **data)
        audiohub.tts_hub.text_to_speech.TTSProcessingTextToSpeech(ttslib).text_to_speech(text, file_out=self.filepath, **data)
        # text_to_speech.TTSProcessingTextToSpeech(ttslib).text_to_speech(text, file_out=self.filepath, **data)
        self.assertTrue(Path(self.filepath).exists())

    # @pytest.mark.skip(reason="skip this test for now")
    def test_text_to_speech_breeze_blue(self):
        """
        test text to speech using breeze blue
        """

        self.filepath = Path("assets/result-tts-breeze.mp3")

        # test tts with espeak-ng
        ttslib: AbcTTSProc = tts_breeze_blue.TTSProc()
        # text = 'ni3 hao3, shi4 jie4!'
        # 'welcome 你好，欢迎来到上海！'
        text = "welcome to Miami of Florida, the sunshine state. Enjoy the beach and the sun!"
        data = {"model_id": "breeze-tts-2", "wpm": 170, "voice": "voc_xeh3w54cqvnp"}
        audiohub.tts_hub.text_to_speech.TTSProcessingTextToSpeech(ttslib).text_to_speech(text, file_out=self.filepath, **data)
        self.assertTrue(Path(self.filepath).exists())

    @pytest.mark.skip(reason="skip this test for now")
    def test_text_to_speech_azure(self):
        """
        test text to speech using Azure
        """

        self.filepath = Path("assets/result-tts-azure.wav")

        # test tts with espeak-ng
        ttslib: AbcTTSProc = tts_azure.TTSProc()
        text = "welcome to Miami of Florida, the sunshine state. Enjoy the beach and the sun!"
        voice = "en-US-Andrew:DragonHDLatestNeural" # "en-US-Jenny:DragonHDLatestNeural" # "en-US-JennyNeural"
        data = {"region": "eastus", "wpm": 170, "voice": voice}
        audiohub.tts_hub.text_to_speech.TTSProcessingTextToSpeech(ttslib).text_to_speech(text, file_out=self.filepath, **data)
        self.assertTrue(Path(self.filepath).exists())

    def tearDown(self) -> None:
        pass


if __name__ == '__main__':
    unittest.main()
