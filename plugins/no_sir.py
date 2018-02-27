from errbot import BotPlugin, re_botcmd
from string import punctuation

class NoSir(BotPlugin):
    """
    Reply to users using 'sir'
    """
    punct = [c for c in punctuation if c!='@']
    punct = ''.join(punct)
    # Ignore LineLengthBear, PycodestyleBear
    @re_botcmd(pattern=r'(?:(?:\s+[punct]?sir[punct]?$)|(?:^sir[punct]?\s+)|(?:\s+[punct]?sir[punct]?\s+))',
               flags=re.IGNORECASE)
    def reply_sir(self, msg, match):
        """
        Reply to users using 'sir'
        """
        user = msg.frm.nick
        return ('Hey @' + user+', there is no need to be so formal!'
                ' Just use @<username> to address people and '
                'keep it casual :wink:')
