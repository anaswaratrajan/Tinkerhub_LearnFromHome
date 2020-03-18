'''

Problem statement

Write a python class for tech learners and mentors. Should have following methods

    addStacks() : Add a particular stack of interest/expertise
    setMentorOrLearner() : Set whether the participant is learner or mentor
    setAvailableTime() : if person is mentor set available time
    getMentor() : Takes stack and time as params and finds available mentors.

'''
from datetime import datetime
from pprint import pprint

class Bootcamp(dict):
    '''Class to handle the tech learners and mentors of a bootcamp.
     Note : # Always setMentorOrLearner before addStacks
            # All participants are identified by their usernames (usernames assumed to be unique)
            '''

    participant_types = ['mentor','learner']
    mentors = dict()
    learners = dict()

    def add_participant(self, username):
        self.current_participant = username
        self[self.current_participant] = dict()
        print("\nParticipant %s added"%username)

    def get_current_participant(self):
        print("\n")
        pprint(self[self.current_participant])

    def addStacks(self, stack_type, *args):
        if stack_type=='expertise':
            self[self.current_participant]['expertise'] = list(args)
            if self[self.current_participant]['participant_type'] == 'mentor':
                for i in args:
                    if i in self.mentors.keys():
                        self.mentors[i].append(self.current_participant)
                    else:
                        self.mentors[i] = [self.current_participant]

        elif stack_type=='interests':
            self[self.current_participant]['interests'] = list(args)
            if self[self.current_participant]['participant_type'] == 'learner':
                for i in args:
                    if i in self.learners.keys():
                        self.learners[i].append(self.current_participant)
                    else:
                        self.learners[i] = [self.current_participant]


    def setMentorOrLearner(self, type):
        if type in self.participant_types:
            self[self.current_participant]['participant_type'] = type
            print("Participant type %s set for %s"%(type,self.current_participant))
        else:
            print("Invalid participant type")

    def change_current_participant(self, username):
        if username in self:
            self.current_participant = username
            print("Participant changed to %s"%username)
        else:
            print("Participant doesn't exist. Try adding using add_participant method.")

    def setAvailableTime(self, avail_time):
        if self[self.current_participant]['participant_type']=='mentor':
            self[self.current_participant]['available_time'] = [datetime.strptime(i,"%I:%M%p") for i in avail_time.split("-")]
            print("Available time %s set for %s"%(avail_time, self.current_participant))
        else:
            print("Participant not mentor")

    def getMentor(self, avail_time, *args):
        req_from_time, req_to_time = [datetime.strptime(i,"%I:%M%p") for i in avail_time.split("-")]
        avail = dict()
        for i in args:
            avail[i] = []
            if i in self.mentors.keys():
                for j in self.mentors[i]:
                    if req_from_time>=self[j]['available_time'][0] and req_to_time<=self[j]['available_time'][1]:
                        avail[i].append((j, req_from_time, req_to_time))
            else:
                avail[i] = None
        print("\nAvailable mentors for the stack: %s")
        pprint(avail)

    def get_learners(self, *args):
        avail = dict()
        for i in args:
            avail[i] = []
            if i in self.learners.keys():
                for j in self.learners[i]:
                    avail[i].append((j, i))
            else:
                avail[i] = None
        print("\n\nAvailable learners for the stack:\n")
        pprint(avail)
