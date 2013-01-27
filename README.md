#PairIT
-----

![PairIt Sketch](https://raw.github.com/ajrod/pairit/master/sketch.png "PairIt Sketch")

Sketch made by [Sacha Chua](http://sachachua.com/blog/2012/12/sketchnotes-angel-hack-toronto-pitches/).
##About
Angel Hack project - This is a [hackathon project](http://www.hackathon.io/741) myself, Warren Marivel and Surya Nallu
participated in; three University of Toronto Undergraduates. This Toronto hackathon is one of the largest in the world with 100s of 
participants this year. You can find more information about angel hack here at their [website](http://angelhack.ca).

The theme of the hackathon was to solve any problem in about 24 hours. We chose to create a Pair Programming app,
to allow remote users to easily collaborate with no downloads or any plugins. We called this prototype PairIT. The
app was to be built on nodejs and socket.io so that we could learn something new in the process.

At the end of the 24 hour sprint, we had a basic IDE that could be shared with other users in real time.
Think of it as google docs for programmers; as you edit the file other users in the session see 
these changes in real time. We made it so that there could only be one person editing the code at a time (the driver)
and one or more navigators. The driver and navigator could easily switch at any time.

To make collaboration efficent we added syntax highlighting for several languages (such as Python), 
syntax checking, a chat window, and you could upload a file by dragging and droping new files into the editor. 
Finally, once your done editing the file you could export the file, to a gist or download it.

![PairIt Snapshot 1](https://raw.github.com/ajrod/pairit/master/snapshot1.png "PairIt Snapshot 1")
![PairIt Snapshot 2](https://raw.github.com/ajrod/pairit/master/snapshot2.png "PairIt Snapshot 2")
##The Pitch

After the 24 hour sprint had passed each team had to do a 2 minute pitch to 12 judges. To think, we worked hard for 
24 hours and they only gave us 2 minutes! The pressure was on to deliver the idea of PairIT and show off full use case 
for our app in this small window of time. I was chosen to be the speaker for our team, while Warren would be on the 
computer demonstrating what I was talking about and Surya would answer any questions from the Judges after the demo.

Our team was one of the first teams to pitch (i think we were the 11th) and there was an audience over of 500+. I was 
quiet nervous as I didn't have much experience in public speaking to a large audience and at this point I was exausted
from not sleeping in over 36 hours. After a couple Red Bulls and an adrenaline rush, I pitched PairIT and we were able
to cover all that we wanted. The pitch went smoothly and we finished exactly at the 2 minute mark.

After the pitch, one of the Microsoft judges asked us why not just use RDP? It took us a moment to realize
what he was suggesting was windows Remote Desktop Protocol as a viable solution instead.
Our problems with RDP is of course you have to have a windows OS 
(or be willing to install additional software on other OS's), configure your firewalls, 
install additional software for an IDE, and then give some remote user full access to your computer (no thanks). 
Instead PairIT seeks to be a light weight solution with no strings attached, you simply need a web browser.


##Hackathon Results

We recieved feedback from the judges almost immediately and we were happy to find that it was mostly positive.
* "Liked the presentation with story off the top.  Most importantly,
  there is a real need for this.  As for name, needs some work!"
* "Cool."
* "Great idea.. I'm old I think it'll be hard to get people to change off rdp initially"
* "Awesome live demo; Good to play on strengths of what you would use; Showed full use case and workflow for programmers."
* "Cool tech but can you use it on projects? Nice work for a weekend."

We would have to wait about 5 more hours to get the results of the hackathon, because there were so many other
teams left to pitch. The announcement came late in the evening of the second day of the hackathon. 

We ended up coming in the top 5 which exceeded our expectations. Had we known that we had a chance we may have
prepared more and had a larger team since the top 2 teams got to go to Silicon Valley and become incubated 
with lots of investments. You can see PairIt briefly mentioned in the prize section at http://torontoangelhack.eventbrite.com/.


##Going Forward
We were all pleased about our results on team PairIT. We have since renamed it to PairIDE and 
are now working on PairIDE as a Capstone project at University of Toronto. You can follow updates 
at our new [github](https://github.com/pairide/pairide) or our website www.PairIDE.com. The Capstone is expected
to finish April 3rd, 2013.


Disclaimer about PairIt's code
-----
None of us had any experience in node, socket.io or any of the other technologies used but we thought it would be exciting to 
learn as we go. Combine this with the extreme time constraints and the pressure of a hackathon to create your product in 24 hrs 
and you have a recipe for dirty code! So I warn you, some of the code is inefficient and just plain ugly; 
many sacrifices needed to be made for immediate gains and anyone who wants to look at the code may find it 
painful to read. 






