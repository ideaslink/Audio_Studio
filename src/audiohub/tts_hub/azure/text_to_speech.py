"""
text to speech by azure

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
import azure.cognitiveservices.speech as speechsdk

from audiohub.shared.vars import AZURE_SPEECH_VARS
import os


class TTSProc(AbcTTSProc):
    """
    text to speech
    AbcTTSProc implementation
    """

    def __init__(self, tts_proc_lib: AbcTTSProc | None = None):
        self.ttslib = tts_proc_lib

    def text_to_speech(self, text: str, file_out: str, **kvargs) -> None:
        """
        text to speech using azure tts
        :param text: text input
        :param file_out: file to save speech result
        :param kvargs: optional
        :return: None
        """
        api_key = os.getenv(AZURE_SPEECH_VARS.get("API_KEY", ""))
        
        region = "eastus"
        voice = 'en-US-AriaNeural'
        wpm = 60
        # apply attributes
        if "region" in kvargs:
            region = kvargs['region']
        if "wpm" in kvargs:
            wpm = kvargs['wpm']
        if "voice" in kvargs:
            voice = kvargs['voice']

        speech_config = speechsdk.SpeechConfig(subscription=api_key, region=region)
        speech_config.speech_synthesis_voice_name = voice
        audio_config = speechsdk.audio.AudioOutputConfig(filename=file_out)

        # use the default speaker as audio output.
        speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
        

        result = speech_synthesizer.speak_text_async(text).get()

        # Check result
        if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
            print(f"Speech synthesized for text {text}")
        elif result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = result.cancellation_details
            print(f"Speech synthesis canceled: {cancellation_details.reason}")

