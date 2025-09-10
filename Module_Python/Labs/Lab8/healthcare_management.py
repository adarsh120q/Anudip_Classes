scheduled_appointments = {"Anna", "Bob", "Clara"}
walkin_appointments = {"Clara", "David", "Eva"}

print("Patients with both appointments:")
for index,persons in enumerate(scheduled_appointments.intersection(walkin_appointments),1):
    print(f"{index}. {persons}")

print("\nList of all patients:")
for index,persons in enumerate(scheduled_appointments.union(walkin_appointments),1):
    print(f"{index}. {persons}")

print("\nList of patients having only walk-in appointments:")
for index,persons in enumerate(walkin_appointments.difference(scheduled_appointments),1):
    print(f"{index}. {persons}")

walkin_appointments.add("Frank")
print("\nList of patients having walk-in appointments after adding 'Frank':")
for index,persons in enumerate(walkin_appointments,1):
    print(f"{index}. {persons}")

scheduled_appointments.discard("Eva")
print("\nList of patients having scheduled appointments after removing 'Eva':")
for index,persons in enumerate(scheduled_appointments,1):
    print(f"{index}. {persons}")