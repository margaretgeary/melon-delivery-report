def melon_count(day_number, file_name):
##Defining a function that takes day number and file name as parameters.    
    print("Day ", day_number)
    ##Printing the day and day number (provided by user)
    the_file = open(file_name)
    ##Opening the file name
    for line in the_file:
        line = line.rstrip()
        words = line.split('|')

        melon = words[0]
        count = words[1]
        amount = words[2]

        print("Delivered {} {}s for total of ${}".format(
          count, melon, amount))
    the_file.close()

melon_count(1, "um-deliveries-20140519.txt")
melon_count(2, "um-deliveries-20140520.txt")
melon_count(3, "um-deliveries-20140521.txt")
##Running the function to take the day number and file name as arguments.