MELON_COST = 1.00


def melon_payment_calculator(payment_data_filename):
    """Calculate cost of melons and determine who has underpaid."""

    payment_data = open(payment_data_filename) # open the file 

    # iterate over lines in file
    for line in payment_data: 
        # for each line, split by |
        order = line.split('|')

        # get the full name at index 1
        customer_name = order[1] 

        # get the first name after splitting by " "
        customer_first = customer_name.split(" ")[0] 

        # get # of melons and payment ammount
        customer_melons = float(order[2])
        customer_paid = float(order[3])

        # calculate expected price
        customer_expected = customer_melons * MELON_COST

        # check if customer over or under paid
        if customer_expected < customer_paid:
            print "{} paid ${:.2f}, expected ${:.2f}".format(
                customer_name, customer_paid, customer_expected)
            print "{} has overpaid for their melons.".format(customer_first)

        elif customer_expected > customer_paid:
            print "{} paid ${:.2f}, expected ${:.2f}".format(
                customer_name, customer_paid, customer_expected)
            print "{} has underpaid for their melons.".format(customer_first)

    # close the file
    payment_data.close()

# call the function 
melon_payment_calculator("customer-orders.txt")
