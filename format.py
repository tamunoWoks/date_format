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
            month, day, year = date.split('/')
        




if __name__ == "__main__":
    main()