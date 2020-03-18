from code import Bootcamp

TH_LearnFromHome = Bootcamp()

# Making entries for participant : atr
TH_LearnFromHome.add_participant("atr")
TH_LearnFromHome.setMentorOrLearner("mentor")
TH_LearnFromHome.setAvailableTime("4:30PM-6:00PM")
TH_LearnFromHome.addStacks("expertise","Python","Django","Flask")
TH_LearnFromHome.addStacks("interests","Python","Javascript","Machine learning","C++")

# Get details of participant : atr
TH_LearnFromHome.get_current_participant()

# Making entries for participant : anaswara
TH_LearnFromHome.add_participant("anaswara")
TH_LearnFromHome.setMentorOrLearner("learner")
TH_LearnFromHome.addStacks("expertise","Python","Django")
TH_LearnFromHome.addStacks("interests","Javascript","Machine learning","C++","Python","React")

# Get details of participant : anaswara
TH_LearnFromHome.get_current_participant()
# Switch to participant : atr
TH_LearnFromHome.change_current_participant("atr")
# Get details of participant : atr
TH_LearnFromHome.get_current_participant()

# Making entries for participant : roger
TH_LearnFromHome.add_participant("roger")
TH_LearnFromHome.setMentorOrLearner("learner")
TH_LearnFromHome.addStacks("expertise","Javascript")
TH_LearnFromHome.addStacks("interests","Javascript","Python",)

# Get mentors for the stack Python, Flask, Javascript
print("getMentor() called for the stack Python, Flask, Javascript at available time 5:00PM-5:30PM")
TH_LearnFromHome.getMentor("5:00PM-5:30PM","Python","Flask","Javascript")

#Get learners for a stack
TH_LearnFromHome.get_learners("5:00PM-5:30PM","Python")
