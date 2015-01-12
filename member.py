# http://www.interviewzen.com/question/PWmpkV

# General Instructions:

# This 3 question exercise should take approximately 60 minutes to complete.  While we prefer 2 complete answers to 3 partial solutions, the tool does allow additional time should you choose to use it.

# Given this is an evaluation where you are not able to ask clarifying questions, please list your assumptions. Please copy link at the top of your browser screen this is your unique test link .When finished, before submitting your answer online, please copy/paste your link at top of browser and answer in an email and send directly to neilland@amazon.com. Thank you!

# We value production-ready code. Candidates should look to submit solutions they would be proud to ship to customers. Candidates can implement solutions in any language with which they feel comfortable (C++, C#, Java, etc.). 

class Member(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.friends = []

    def set_friends(self, friends):
        self.friends = friends

    def __str__(self):
        return self.name + ":" + self.email


def print_social_graph(member):
    def handler_one(friend):
        print friend
    [handler_one(friend) for friend in member.friends]
    [print_social_graph(friend) for friend in member.friends]

if __name__ == '__main__':
    chen =  Member('chen', '')

    m1 = Member('m1', '')
    m2 = Member('m2', '')
    m3 = Member('m3', '')

    mm1 = Member('mm1', '')
    mm2 = Member('mm2', '')

    m1.set_friends([mm1,mm2])
    chen.set_friends([m1,m2,m3])

    print_social_graph(chen)
