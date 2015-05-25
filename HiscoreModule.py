from ModuleBase import RSModule
import RSInfoBot

class HiscoreModule(RSModule):
    targetURL = 'http://services.runescape.com/m=hiscore_oldschool/a=13/hiscorepersonal.ws?user1='

    def createComment(self, r, comment):
        s = comment.body.find(self.targetURL)
        if s >= 0:
            return 'You have linked the stats of ' + comment.body[s]
        else:
            return ''


    def validate(self, r, comment):
        return self.targetURL in comment.body

    def handle(self, r, comment):
        reply = self.createComment(r, comment)
        if len(reply) > 1:
            comment.reply(RSInfoBot.signature % reply)
            return True
        else:
            return False




