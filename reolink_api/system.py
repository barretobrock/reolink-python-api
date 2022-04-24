from typing import (
    Dict,
    List
)


class SystemAPIMixin:
    """API for accessing general system information of the camera."""
    def get_general_system(self) -> List[Dict]:
        """:return: response json"""
        body = [{"cmd": "GetTime", "action": 1, "param": {}}, {"cmd": "GetNorm", "action": 1, "param": {}}]
        return self._execute_command('get_general_system', body, multi=True)

    def get_performance(self) -> List[Dict]:
        """
        Get a snapshot of the current performance of the camera.
        See examples/response/GetPerformance.json for example response data.
        :return: response json
        """
        body = [{"cmd": "GetPerformance", "action": 0, "param": {}}]
        return self._execute_command('GetPerformance', body)

    def get_information(self) -> List[Dict]:
        """
        Get the camera information
        See examples/response/GetDevInfo.json for example response data.
        :return: response json
        """
        body = [{"cmd": "GetDevInfo", "action": 0, "param": {}}]
        return self._execute_command('GetDevInfo', body)

    def reboot_camera(self) -> List[Dict]:
        """
        Reboots the camera
        :return: response json
        """
        body = [{"cmd": "Reboot", "action": 0, "param": {}}]
        return self._execute_command('Reboot', body)

    def get_dst(self) -> List[Dict]:
        """
        Get the camera DST information
        See examples/response/GetDSTInfo.json for example response data.
        :return: response json
        """
        body = [{"cmd": "GetTime", "action": 0, "param": {}}]
        return self._execute_command('GetTime', body)
