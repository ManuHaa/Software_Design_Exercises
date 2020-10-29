#This class represents the instance of a psubscription

from RegisteredUser import RegisteredUser

class RegisteredUser:
    def __init__(self, subscriptionUser, subscriptionChannel):
        self.subscriptionUser = subscriptionUser
        self.subscriptionChannel = subscriptionChannel

    def get_subscriptionUser(self):
        return self.subscriptionUser

    def set_subscriptionUser(self, subscriptionUser):
        self.subscriptionUser = subscriptionUser

    def get_subscriptionChannel(self):
        return self.subscriptionChannel

    def set_subscriptionChannel(self, subscriptionChannel):
        self.subscriptionChannel = subscriptionChannel
