import pytest
from television import *

class Test:
    def setup_method(self):
        '''

setting up the television        '''
        self.tv1 = Television()

    def teardown_method(self):
        '''
        clear the test
        '''
        del self.tv1

    def test_init(self):
        '''
        test that default settings when television is launched
        '''
        assert self.tv1.__str__() == 'Power = False, Channel = 0, Volume = 0'

    def test_power(self):
        '''
        test if the television turns on/off
        '''
        self.tv1.power()
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 0'
        self.tv1.power()
        assert self.tv1.__str__() == 'Power = False, Channel = 0, Volume = 0'

    def test_mute(self):
        '''
        test if the television mutes or unmutes along with the volume if  up unmutes, if down uncomutes
        '''
        self.tv1.mute()
        assert self.tv1.__str__() == 'Power = False, Channel = 0, Volume = 0'
        self.tv1.power()
        self.tv1.volume_up()
        self.tv1.mute()
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 0'
        self.tv1.mute()
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 1'

    def test_channel_up(self):
        '''
        test if the channel goes up to max then loops
        '''
        self.tv1.channel_up()
        assert self.tv1.__str__() == 'Power = False, Channel = 0, Volume = 0'
        self.tv1.power()
        self.tv1.channel_up()
        assert self.tv1.__str__() == 'Power = True, Channel = 1, Volume = 0'

        self.tv1.channel_up()
        self.tv1.channel_up()
        self.tv1.channel_up()
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 0'

    def test_channel_down(self):
        self.tv1.channel_down()
        assert self.tv1.__str__() == 'Power = False, Channel = 0, Volume = 0'

        self.tv1.power()
        self.tv1.channel_down()
        assert self.tv1.__str__() == 'Power = True, Channel = 3, Volume = 0'

        self.tv1.channel_up()
        self.tv1.channel_up()
        self.tv1.channel_down()
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 0'

    def test_volume_up(self):
        self.tv1.volume_up()
        assert self.tv1.__str__() == 'Power = False, Channel = 0, Volume = 0'
        self.tv1.power()
        self.tv1.volume_up()
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 1'

        self.tv1.mute()
        self.tv1.volume_up()
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 2'

        self.tv1.volume_up()
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 2'

    def test_volume_down(self):
        self.tv1.volume_down()
        assert self.tv1.__str__() == 'Power = False, Channel = 0, Volume = 0'
        self.tv1.power()
        self.tv1.volume_up()
        self.tv1.volume_up()
        self.tv1.volume_down()
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 1'

        self.tv1.mute()
        self.tv1.volume_down()
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 0'

        self.tv1.volume_down()
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 0'