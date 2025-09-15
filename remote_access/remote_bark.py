# Remote Access Profile
class TRRemoteAccessProfile:
    def __init__(self):
        self.api_key = ""


class TRRemoteAccessMessage:
    def __init__(self) -> None:
        self.title = ""
        self.subtitle = ""
        self.body = ""
        self.device_key = ""
        self.device_keys = []
        self.level = 0
        self.volume = 0
        self.badge = 0
        self.call = 0
        self.autoCopy = 0
        self.copy = 0
        self.sound = 0
        self.icon = ""
        self.group = ""
        self.ciphertext = ""
        self.isArchive = 1
        self.url = ""
        self.action = "none"
        self.id = 0
        self.delete = 0


# Remote Notification Manager
class TRRemoteAccessManager:
    def run_service(self):
        print("remote_bark: run_service")

        profile = TRRemoteAccessProfile()

        pass

    pass

    def post_message(self):
        demo = TRRemoteAccessMessage()

        pass
