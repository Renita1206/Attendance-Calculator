#Attendance percentage criteria
percentage = 80

# No. of [M,T,W,T,F] in semester
days = [15, 15, 16, 15, 15]

# No. of hours in each day for each subject
DBMS = [2, 1, 1, 2, 1]
MI= [2,3,0, 1, 1]
SE = [1, 0, 1, 1, 2]
DA = [0, 2, 1, 2, 0]
GTA = [1 , 0, 2, 0, 2]

#Total number of classes for each subject
t_DBMS = 0
for i in range(5):
    t_DBMS+=days[i] * DBMS[i]
#print(t_DBMS)

t_MI = 0
for i in range(5):
    t_MI+=days[i] * MI[i]
#print(t_MI)

t_SE = 0
for i in range(5):
    t_SE+=days[i] * SE[i]
#print(t_SE)

t_DA = 0
for i in range(5):
    t_DA+=days[i] * DA[i]
#print(t_DA)

t_GTA = 0
for i in range(5):
    t_GTA+=days[i] * GTA[i]
#print(t_GTA)

sub = input("Enter subject (DBMS/MI/SE/DA/GTA): ")
if(sub=="DBMS" or sub=="MI" or sub=="SE" or sub=="DA" or sub=="GTA"):
    attended = int(input("Enter no of classes attended: "))
    sessions = int(input("Enter no. of classes held: "))
    if(sub=="DBMS"):
        x = int((1 - percentage/100)*t_DBMS - sessions + attended)
    elif(sub=="MI"):
        x = int((1 - percentage/100)*t_MI - sessions + attended)
    elif(sub=="SE"):
        x = int((1 - percentage/100)*t_SE - sessions + attended)
    elif(sub=="DA"):
        x = int((1 - percentage/100)*t_DA - sessions + attended)
    elif(sub=="GTA"):
        x = int((1 - percentage/100)*t_GTA - sessions + attended)
else:
    print("Invalid subject")
    exit(0)
print("Current Attendance Percentage: ", round((attended/sessions)*100))
print("You can bunk",x,"classes")
