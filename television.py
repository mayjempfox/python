class Television:
    '''
    class variables
    example: min_volume = minimum  volume level is 0
    so on...
    '''
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        '''
        starting settings for the television
        meaning it is off, unmuted, min vol is 0, min channel is 0
        '''
        self.__muted = False
        self.__status = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self):
        '''
        on / off
        '''
        self.__status = not self.__status

    def mute(self) -> None:
        '''
        mute/ unmuted
        '''
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self):
        '''
        increase volume by 1 loops back after max
        '''
        if self.__status:
            if self.__channel >= Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self) -> None:
        '''
        decrease by 1 loops back after max channel
        '''
        if self.__status:
            if self.__channel <= Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self) -> None:
        '''
        increase volume by 1
        if muted goes unmute
        no change if reaches max volume
        '''
        if self.__status:
            self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        '''
        decrease volume by 1
        if TV is muted goes unmute
        no change if reaches min volume
        '''
        if self.__status:
            self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        '''
        string that returns whats television status ex power = 0, channel = 0, volume = 0
        '''
        if self.__muted:
            volume = Television.MIN_VOLUME
        else:
            volume = self.__volume

        return f'Power = {str(self.__status)}, Channel = {self.__channel}, Volume = {volume}'
