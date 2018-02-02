from collections import OrderedDict

SELECTION = '1: send thank you \n2: create report\n'
DONOR = 'name?'
DONATION = 'donation amount:'

donors = {"Greg": [50], "Charles": [100], "Steve": [200]}

def main():
    while True:
        selection = getInput(SELECTION)
        
        if selection == '1':
            while True:
                donor = getInput(DONOR)
            while True:
                try:
                    donation = int(getInput(DONATION))
                except:
                    print("Not valid")
                else:
                    if donor not in donors:
                        donors[donor] = [donation]
                    else:
                        donors[donor] += [donation]

                    print('{0}, Thank you for your donation of {1}!'.format(donor, donation))
        
        elif selection == '2':
            ordered = OrderedDict(sorted(donors.items()))

            for donor, donations in ordered.items():
                num = len(donations)
                total = sum(donations)
                avg = total/num
                print("Name: {0} \t Total: {1} \t Number Donations: {2} \t Average donation: {3}".format(donor, total, num, avg))

def getInput(prombt):
        return input(prombt)

main()