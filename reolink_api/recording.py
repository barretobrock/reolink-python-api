import random
import string
from urllib import parse
from io import BytesIO
from typing import (
    Callable,
    Dict,
    List
)
import requests
from loguru import logger
from PIL import Image
from reolink_api.RtspClient import RtspClient


class RecordingAPIMixin:
    """API calls for recording/streaming image or video."""

    def get_recording_encoding(self) -> List[Dict]:
        """
        Get the current camera encoding settings for "Clear" and "Fluent" profiles.
        See examples/response/GetEnc.json for example response data.
        :return: response json
        """
        body = [{"cmd": "GetEnc", "action": 1, "param": {"channel": 0}}]
        return self._execute_command('GetEnc', body)

    def get_recording_advanced(self) -> List[Dict]:
        """
        Get recording advanced setup data
        See examples/response/GetRec.json for example response data.
        :return: response json
        """
        body = [{"cmd": "GetRec", "action": 1, "param": {"channel": 0}}]
        return self._execute_command('GetRec', body)

    def set_recording_encoding(self,
                               audio: int = 0,
                               main_bit_rate: int = 8192,
                               main_frame_rate: int = 8,
                               main_profile: str = 'High',
                               main_size: str = "2560*1440",
                               sub_bit_rate: int = 160,
                               sub_frame_rate: int = 7,
                               sub_profile: int = 'High',
                               sub_size: str = '640*480') -> List[Dict]:
        """
        Sets the current camera encoding settings for "Clear" and "Fluent" profiles.
        :param audio: int Audio on or off
        :param main_bit_rate: int Clear Bit Rate
        :param main_frame_rate: int Clear Frame Rate
        :param main_profile: string Clear Profile
        :param main_size: string Clear Size
        :param sub_bit_rate: int Fluent Bit Rate
        :param sub_frame_rate: int Fluent Frame Rate
        :param sub_profile: string Fluent Profile
        :param sub_size: string Fluent Size
        :return: response
        """
        body = [
            {
                "cmd": "SetEnc",
                "action": 0,
                "param": {
                    "Enc": {
                        "audio": audio,
                        "channel": 0,
                        "mainStream": {
                            "bitRate": main_bit_rate,
                            "frameRate": main_frame_rate,
                            "profile": main_profile,
                            "size": main_size
                        },
                        "subStream": {
                            "bitRate": sub_bit_rate,
                            "frameRate": sub_frame_rate,
                            "profile": sub_profile,
                            "size": sub_size
                        }
                    }
                }
            }
        ]
        return self._execute_command('SetEnc', body)

    ###########
    # RTSP Stream
    ###########
    def open_video_stream(self, callback: Callable = None, profile: str = "main", proxies: Dict = None):
        """
        'https://support.reolink.com/hc/en-us/articles/360007010473-How-to-Live-View-Reolink-Cameras-via-VLC-Media-Player'
        Blocking function creates a generator and returns the frames as it is spawned
        :param profile: profile is "main" or "sub"
        :param proxies: Default is none, example: {"host": "localhost", "port": 8000}
        """
        rtsp_client = RtspClient(
            ip=self.ip, username=self.username, password=self.password, proxies=proxies, callback=callback)
        return rtsp_client.open_stream()

    def get_snap(self, timeout: int = 3, proxies=None) -> Image or None:
        """
        Gets a "snap" of the current camera video data and returns a Pillow Image or None
        :param timeout: Request timeout to camera in seconds
        :param proxies: http/https proxies to pass to the request object.
        :return: Image or None
        """
        data = {
            'cmd': 'Snap',
            'channel': 0,
            'rs': ''.join(random.choices(string.ascii_uppercase + string.digits, k=10)),
            'user': self.username,
            'password': self.password,
        }
        params = parse.urlencode(data).encode("utf-8")

        try:
            response = requests.get(self.url, proxies=proxies, params=params, timeout=timeout)
            if response.status_code == 200:
                return Image.open(BytesIO(response.content))
            logger.warning("Could not retrieve data from camera successfully. Status:", response.status_code)
            return None

        except Exception as e:
            logger.error("Could not get Image data\n", e)
            raise
