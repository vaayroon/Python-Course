"""for i in ["Pildoras", "Informaticas", 3]:
    print("Hola", end=" ")
"""
email = False
inputEmail = input("Enter your valid email: ")

for i in inputEmail:
    if i == "@":
        email = True

"if email==True:"
if email:
    print("Correct Email")
else:
    print("Incorrect Email")

"----------------------------------------------------------"

"Here we are saying to python that we are gonna use f function --> that allow us to play with different formats"
for i in range(5):
    print(f"The value of the variables is {i}")

"Here we say to python to count from 8 to 49 with a step of 2"
for i in range(8, 50, 2):
    print(f"The value of the variables is {i}")

"While loop --> while condition:"

j = 1
while j <= 5:
    print("while loop: " + str(j))
    j = j + 1

print("The loop has finished")


"----------------------------------------------------------"
name = "Pildoras Informaticas"
count = 0
i = 0
for i in name:
    if i == " ":
        continue
    count += 1

print("There number of letters is: " + str(count))