class BaseMessage():
    def __init__(self,senderId) -> None:
        self.senderId=senderId
        self.type='BaseMessage'