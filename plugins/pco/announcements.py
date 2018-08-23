from will.plugin import WillPlugin
from will.decorators import respond_to, periodic, hear, randomly, route, rendered_template, require_settings
from plugins.pco import birthday, address, phone_numbers, checkins, msg_attachment, authenticate, pcoservices


class ScheduledAnnounce(WillPlugin):

    def announcement_channel(self, passed_channel=None):
        """"If you pass a channel it will save it as the announcement channel, and return the announcement channel.
        If you pass no channel it will return the saved channel. If no channel is set it defaults to the announcements
        channel."""
        if not self.load("announcement_channel") and passed_channel is None:
            self.save("announcement_channel", "announcements")
        elif channel:
            self.save("announcement_channel", passed_channel)
        return self.load("announcement_channel")

    # @hear("announce birthdays")
    # @periodic(hour='14', minute='10')  # at a certain time
    @periodic(hour='07', minute='50')  # at a certain time
    def announce_birthdays(self):
        birthday.announce_todays_birthdays(self, channel=self.announcement_channel())

    @respond_to("(!setannouncements)(?P<channelname>.*?(?=(?:\?)|$))")
    def set_anounce_chan(self, channelname):
        announce_chan = self.announcement_channel(channelname)
        self.reply(self, "Announcement channel is set to %s" % announce_chan)


    # @periodic(hour='14', minute='10')  # at a certain time
    # @periodic(second=0)  # every minute at 0 seconds
    def announce(self):
        self.say("Announcement!", channel=self.announcement_channel())

    # @hear("this channel")
    def this_channel(self, channel=None):
        self.say("This channel's name is %s" % self.message.data.channel.name, channel=channel)
        self.say("This channel's id is %s" % self.message.data.channel.id, channel=channel)
