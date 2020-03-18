from code import Bootcamp

TH_LearnFromHome = Bootcamp()

TH_LearnFromHome.add_participant("atr")
TH_LearnFromHome.setMentorOrLearner("mentor")
TH_LearnFromHome.setAvailableTime("4:30PM-6:00PM")
TH_LearnFromHome.addStacks("expertise","Python","Django","Flask")
TH_LearnFromHome.addStacks("interests","Python","Javascript","Machine learning","C++")

TH_LearnFromHome.get_current_participant()

TH_LearnFromHome.add_participant("anaswara")
TH_LearnFromHome.setMentorOrLearner("learner")
TH_LearnFromHome.setAvailableTime("12:00PM-7:00PM")
TH_LearnFromHome.addStacks("expertise","Python","Django")
TH_LearnFromHome.addStacks("interests","Javascript","Machine learning","C++","Python","React")

TH_LearnFromHome.change_current_participant("atr")

TH_LearnFromHome.get_current_participant()

TH_LearnFromHome.add_participant("roger")
TH_LearnFromHome.setMentorOrLearner("learner")
TH_LearnFromHome.setAvailableTime("9:00AM-7:00PM")
TH_LearnFromHome.addStacks("expertise","Javascript")
TH_LearnFromHome.addStacks("interests","Javascript","Python",)


TH_LearnFromHome.getMentor("5:00PM-5:30PM","Python","Flask","Javascript")

TH_LearnFromHome.get_learners("5:00PM-5:30PM","Python")
