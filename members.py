import time

class MemberObj:
    def __init__(self, name):

        # users name
        self.name = name

        # users total time spent in voice channel
        self.time = 0

        # users total time spent i respective channel
        self.channeltime = {}

        # boolean representing if they currently are connected to
        # a channel
        self.current_channel = None

        self.connect_time = 0

        print('member', self.name, 'initialized')


    def state_change(self, channel):
        if self.current_channel is not channel:
            if self.current_channel is not None:
                self.time = self.time + (int(time.time()) - self.connect_time)
                if channel in self.channeltime:
                    self.channeltime[channel] = self.channeltime[channel] + (int(round(time.time())) - self.connect_time)
                else:
                    self.channeltime[channel] = (int(time.time()) - self.connect_time)

            self.connect_time = int(time.time())
            self.current_channel = channel

    def get_active_time(self):
        return self.time

    def get_active_time_channel(self, channel):
        return self.channeltime.get(channel)
