'''
Created on Mar 6, 2015

4.6 Write a program to prompt the user for hours and rate per hour using raw_input to compute gross pay. 
Award time-and-a-half for the hourly rate for all hours worked above 40 hours. Put the logic to do the 
computation of time-and-a-half in a function called computepay() and use the function to do the computation. 
The function should return a value. Use 45 hours and a rate of 10.50 per hour to test the program 
(the pay should be 498.75). You should use raw_input to read a string and float() to convert 
the string to a number. Do not worry about error checking the user input unless you want to - 

@author: cvora
'''

def computepay(hrs,rps):
    final_pay = 0.0
    hours = float(hrs)
    rate_per_hour = float(rps)
    if  hours>40:
        final_pay += 40 * float(rate_per_hour)
        hours -= 40
        final_pay += hours * rate_per_hour * 1.5
    else:
        final_pay += hours * rate_per_hour 
        
    return final_pay


hrs = raw_input("Enter Hours:")
rate = raw_input("Enter Rate")
p = computepay(hrs,rate)
print p


    