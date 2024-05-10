def main():
    months = [
        'January','February','March','April','May','June',
        'July','August','September','October','November','December'
    ]
    while True:     
        #Collect date as user input 
        date = input('Date: ').strip()

        #Check format of input date string and split
        if "/" in date:
            #split input at forward slash
            month, day, year = date.split('/')
        elif "," in date:
            #remove comma from input
            date = date.replace(',','')
            #split input at whitespace
            month, day, year = date.split()
        else:
            #return to input if both conditions fail
            continue

        #check for errors
        try:
            #convert month and days to int and ensurethey are not more than12 and 31 respectively
            if int(month) > 12 or int(day) > 31:
                continue
            else:
                break
        except ValueError:
            continue
        




if __name__ == "__main__":
    main()