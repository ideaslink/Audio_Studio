"""
text to speech by ElevenLabs

__author__ = "vci"
__copyright__ = "Copyright 2026, vci"
__license__ = "MIT"
__version__ = "1.0.0.10"
__maintainer__ = "vci"
__email__ = "modernui.app@gmail.com"
__status__ = "development"
__reference__ = "vci"
"""

import os
from pathlib import Path

from elevenlabs.client import ElevenLabs

from audiohub.shared.i_tts_proc import AbcTTSProc
from audiohub.shared.vars import ELEVEN_LABS__VARS


class TTSProc(AbcTTSProc):
    """
    text to speech
    AbcTTSProc implementation
    """

    def __init__(self, tts_proc_lib: AbcTTSProc | None = None):
        self.ttslib = tts_proc_lib

    def text_to_speech(self, text: str, file_out: str, **kvargs) -> None:
        """
        text to speech using ElevenLabs TTS
        :param text: text input
        :param file_out: file to save speech result
        :param kvargs: optional voice, model_id, output_format, wpm
        :return: None
        """
        api_key = os.getenv(ELEVEN_LABS__VARS.get("API_KEY", ""))
        if not api_key:
            raise ValueError(
                "ElevenLabs API key is not set; set ELEVENLABS_API_KEY in the environment"
            )

        voice_id = str(kvargs.get("voice", "21m00Tcm4TlvDq8ikWAM"))
        model_id = str(kvargs.get("model_id", "eleven_multilingual_v2"))
        output_format = str(kvargs.get("output_format", "mp3_44100_128"))

        client = ElevenLabs(api_key=api_key)
        audio = client.text_to_speech.convert(
            text=text,
            voice_id=voice_id,
            model_id=model_id,
            output_format=output_format,
        )

        output_path = Path(file_out)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        with output_path.open("wb") as audio_file:
            if isinstance(audio, bytes):
                audio_file.write(audio)
            else:
                for chunk in audio:
                    if chunk:
                        audio_file.write(chunk)
