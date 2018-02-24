order_log = open("customer-orders.txt")
underpaid = []
overpaid = []


def check_if_paid(order_log):
    """ Checks all orders in the order log, alerts if any customer underpaid """
    for line in order_log:
        line = line.rstrip().split("|")
        if int(line[2]) > float(line[3]):
            leftover = math_pay_amounts(line[2], line[3])
            line.append(leftover)
            underpaid.append(line)
        elif int(line[2]) < float(line[3]):
            leftover = math_pay_amounts(line[2], line[3])
            line.append(leftover)
            overpaid.append(line)


def math_pay_amounts(owed, paid):
    """ Typecasts amounts owed & paid, adds or subtracts to return difference """
    owed = int(owed)
    paid = float(paid)
    if owed > paid:
        leftover = owed - paid
    else:
        leftover = paid - owed
    return leftover


def print_pay_status(underpaid, overpaid):
    """ Prints all customers who overpaid or underpaid """
    print "\nThe following customers have overpaid:"

    if len(overpaid) == 0:
        print "NONE"
    else:
        for line in overpaid:
            print line[0:4], " -- OVERPAY AMOUNT: $", line[4]

    print "\nThe following customers have underpaid:"

    if len(underpaid) == 0:
        print "NONE"
    else:
        for line in underpaid:
            print line[0:4], " -- UNDERPAY AMOUNT: $", line[4]

check_if_paid(order_log)
print_pay_status(underpaid, overpaid)
