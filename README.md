# Tinkerhub_LearnFromHome

Class for the techlearners and mentors of the bootcamp

### Table of contents
-------------
* [Problem statement](#problem)
* [Features](#features)
* [Usage](#usage)

<a name="description"></a>
# Problem statement

Write a python class for tech learners and mentors. Should have following methods

    addStacks() : Add a particular stack of interest/expertise
    setMentorOrLearner() : Set whether the participant is learner or mentor
    setAvailableTime() : if person is mentor set available time
    getMentor() : Takes stack and time as params and finds available mentors.


# Features

- add_participant(<username>) - Add new participant
  
- setMentorOrLearner( <participant_type>) : Set whether the participant is learner or mentor 
participant_type - 'mentor'/'learner'

- addStacks( <stack_type>, <argument1> ,<argument2> ...) : Add a particular stack of interest/expertise 
Note: Both mentors and learners can add expertise and interests. But only expertises of mentors are taken for getMentor()
and interests of learners taken for getlearners()
stack_type - 'expertise'/'interests' 
argument1, argument2 .. - interests/expertises Eg: "Python","Javascript"
  
- setAvailableTime(<avail_time>) : if person is mentor set available time 
avail_time format - "%I:%M%p-%I:%M%p" Eg: "4:30PM-5:00PM"

- getMentor(<avail_time>,<argument1> ,<argument2> ...) : Takes stack and time as params and finds available mentors.

- get_current_participant() - Get details of current participant

- change_current_participant(<username>) - Switch to another participant

- get_learners(<argument1> ,<argument2> ...)
  
  See usage for more details

# Usage

Clone the repo
```
  git clone https://github.com/anaswaratrajan/Tinkerhub_LearnFromHome.git
  
```
Enter directory Tinkerhub_LearnFromHome
```
  cd Tinkerhub_LearnFromHome
```

To test the class either run test.py or import the code to cli and test according to the doc

## Run test.py
```
  python test.py
``` 

or
## Test in cli
```
  from code import Bootcamp

  TH_LearnFromHome = Bootcamp()
``` 
Making entries (setMentorOrLearner after add_participant)

```
  TH_LearnFromHome.add_participant("atr")
  TH_LearnFromHome.setMentorOrLearner("mentor")
  TH_LearnFromHome.setAvailableTime("4:30PM-6:00PM")
  TH_LearnFromHome.addStacks("expertise","Python","Django","Flask")
  TH_LearnFromHome.addStacks("interests","Python","Javascript","Machine learning","C++")
```
Get details of current participant 
```
  TH_LearnFromHome.get_current_participant()
```
Switch to another participant
```
  TH_LearnFromHome.change_current_participant("atr")
```
Get mentor for a stack in available time
```
  TH_LearnFromHome.getMentor("5:00PM-5:30PM","Python","Flask","Javascript")
```
Get learners for a stack
```
TH_LearnFromHome.get_learners("5:00PM-5:30PM","Python")
```
