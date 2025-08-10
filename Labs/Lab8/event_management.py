attendees = {"John", "Jane", "Emily", "Michael"}
vip_attendees = {"Jane", "Michael"}

attendees.add("Sarah")
print("New attendees list after adding 'Sarah':")
for index,persons in enumerate(attendees,1):
    print(f"{index}. {persons}")

if "Emily" in vip_attendees:
    print("\nEmily is a VIP attendee.")
else:
    print("\nEmily is not a VIP attendee.")

only_regular = attendees.difference(vip_attendees)
only_vip = vip_attendees.difference(attendees)

print("\nList of only regular attendees:")
for index,persons in enumerate(only_regular,1):
    print(f"{index}. {persons}")

print("\nList of only VIP attendees:")
if not only_vip:
    print("None")
else:
    for index,persons in enumerate(only_vip,1):
        print(f"{index}. {persons}")

print("\nList of all attendees:")
for index,persons in enumerate(attendees.union(vip_attendees),1):
    print(f"{index}. {persons}")