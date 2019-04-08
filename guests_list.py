guests = ['Ogango', 'Odindo' , 'Sore']
print(guests)
unattending_guest = 'Odindo'
guests.remove(unattending_guest)
print(guests)
print(" \nMr " + unattending_guest.title() + "will not be attending this dinner")
guests.insert(0, 'Gitonga')
guests.insert(2, 'Hawanga')
guests.insert(4, 'Chenane')
print(guests)
message = "You are cordially invited to Sir Brian's birthday dinner" + guests [0].title() + "!"
print(message)
message = "You are cordially invited to Sir Brian's birthday dinner" + guests [2].title() + "!"
print(message)
message = "You are cordially invited to Sir Brian's birthday dinner" + guests [4].title() + "!"
print(message)
