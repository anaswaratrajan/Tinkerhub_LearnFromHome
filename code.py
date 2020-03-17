'''

Problem statement

Write a python class for tech learners and mentors. Should have following methods

    addStacks() : Add a particular stack of interest/expertise
    setMentorOrLearner() : Set whether the participant is learner or mentor
    setAvailableTime() : if person is mentor set available time
    getMentor() : Takes stack and time as params and finds available mentors.

'''
from datetime import datetime


class Bootcamp(dict):

    participant_types = ['mentor','learner']
    mentors = dict()

    def add_participant(self, username):
        self.current_participant = username
        self[self.current_participant] = dict()

    def addStacks(self, stack_type, *args):
        if stack_type=='expertise':
            '''pending - condition to check if mentor before adding stack to mentors dict '''
            self[self.current_participant]['expertise'] = list(args)
            for i in args:
                if i in self.mentors.keys():
                    self.mentors[i].append(self.current_participant)
                else:
                    self.mentors[i] = [self.current_participant]

        elif stack_type=='interests':
            self[self.current_participant]['interests'] = list(args)

    def setMentorOrLearner(self, type):
        if type in self.participant_types:
            self[self.current_participant]['participant_type'] = type
        else:
            print("Invalid participant type")

    def change_current_participant(self, username):
        if username in self:
            self.current_participant = username
            print("Participant changed")
        else:
            print("Participant doesn't exist. Try adding using add_participant method.")

    def setAvailableTime(self, avail_time):
        self[self.current_participant]['available_time'] = [datetime.strptime(i,"%I:%M%p") for i in avail_time.split("-")]


    def getMentor(self, avail_time, *args):
        req_from_time, req_to_time = [datetime.strptime(i,"%I:%M%p") for i in avail_time.split("-")]
        avail = dict()
        for i in args:
            avail[i] = []
            if i in self.mentors.keys():
                for j in self.mentors[i]:
                    if req_from_time>=self[j]['available_time'][0] and req_to_time<=self[j]['available_time'][1]:
                        avail[i].append((j,req_from_time, req_to_time))
            else:
                avail[i] = None
        print(avail)
