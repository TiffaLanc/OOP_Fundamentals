from veh_event import Vehicle, Event

print ("-" * 100)
print ("Vehicle Registration System\n")
dodge = Vehicle('XP3310', 'Dodge Charger', 'Trish')
dodge.update_owner()
print("-" * 100)

event1 = Event('Baby Shower', 'Saturday Evening')
event2 = Event('Hiking', 'Sunday Morning')

event1.add_participant()
event2.add_participant()
event2.add_participant()

print("Event Managment System\n")
print(event1.participant_count())
print(event2.participant_count())
print("-" * 100)


