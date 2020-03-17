'''

Problem statement

Write a python class for tech learners and mentors. Should have following methods

    addStacks() : Add a particular stack of interest/expertise
    setMentorOrLearner() : Set whether the participant is learner or mentor
    setAvailableTime() : if person is mentor set available time
    getMentor() : Takes stack and time as params and finds available mentors.

'''
class Bootcamp(dict):

    participant_types = ['mentor','learner']

    def add_participant(self, username):
        self.current_participant = username
        self[self.current_participant] = dict()

    def addStacks(self, stack_type, *args):
        if stack_type=='expertise':
            self[self.current_participant]['expertise'] = list(args)
        elif stack_type=='interests':
            self[self.current_participant]['interests'] = list(args)

    def setMentorOrLearner(self, type):
        if type in self.participant_types:
            self[self.current_participant]['participant_type'] = type
        else:
            print("Invalid participant type")

    def change_current_participant(self, username):
        if username in self.keys:
            self.current_participant = username
            print("Participant changed")
        else:
            print("Participant doesn't exist. Try adding using add_participant method.")

    def setAvailableTime():
        ''' pending '''
        pass

    def getMentor():
        ''' pending '''
        pass
