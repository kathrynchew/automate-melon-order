# import txt file, declare empty strings to aggregate info later
order_log = open("customer-orders.txt")
underpaid = []
overpaid = []


# define functions here:
def check_if_paid(order_log):
    """ Checks all orders in the order log, alerts if any customer underpaid """
    for line in order_log:
        line = line.rstrip().split("|")    # split each line (str) into a list
        if int(line[2]) > float(line[3]):    # check if customer underpaid
            leftover = math_pay_amounts(line[2], line[3])   # if underpaid, check by how much
            line.append(leftover)   # append underpaid amount to line for later printing
            underpaid.append(line)  # append whole line to list of customers who underpaid
        elif int(line[2]) < float(line[3]):    # check if customer overpaid
            leftover = math_pay_amounts(line[2], line[3])   # if overpaid, check by how much
            line.append(leftover)   # append overpaid amount to line for later printing
            overpaid.append(line)   # append whole line to list of customers who overpaid


def math_pay_amounts(owed, paid):
    """ Typecasts amounts owed & paid, adds or subtracts to return difference """
    owed = int(owed)    # typecast str to correct mathematical type
    paid = float(paid)  # typecast str to correct mathematical type
    if owed > paid:
        leftover = owed - paid  # calculate underpaid amount, set to variable to be returned
    else:
        leftover = paid - owed  # calculate overpaid amount, set to variable to be returned
    return leftover


def print_pay_status(underpaid, overpaid):
    """ Prints all customers who overpaid or underpaid """
    print "\nThe following customers have overpaid:"    # print category header for overpaid customers

    if len(overpaid) == 0:  # if no overpaying customers, print filler
        print "NONE"
    else:                   # if yes overpaying customers, loop through list, print info for each customer
        for line in overpaid:
            print line[1], ": ID #", line[0], "-- OVERPAY AMOUNT: $", line[4]

    print "\nThe following customers have underpaid:"   # print category header for underpaid customers

    if len(underpaid) == 0: # if no underpaying customers, print filler
        print "NONE"
    else:                   # if yes underpaying customers, loop through list, print info for each customer
        for line in underpaid:
            print line[1], ": ID #", line[0], "-- UNDERPAY AMOUNT: $", line[4]

# call function to check pay status of all customers
check_if_paid(order_log)
# call function to print all customers who have an irregular pay status
print_pay_status(underpaid, overpaid)
