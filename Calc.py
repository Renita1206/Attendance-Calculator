def calc(credit, percent, attended, held, compensated):
    if(credit==5):
        hours=105
    else:
        hours = 75

    #Attendance percentage criteria
    percentage = percent
    x = int((1 - percentage/100)*hours - held + attended + compensated)
    return x