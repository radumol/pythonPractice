

#Author: Radu Molea 

#Question 1


def exp(x, y):

    """Takes two integers ad recursively computes the exponent function"""
    if y == 0:      #special case when the power is 0
        return 1
    
    if y == 1:       #in case power(y) is 1 
        return x

    if y != 1:        #all the other cases
        return x * exp(x, y - 1)   #x multiplies with itself for each one in y


#Question 2
    

def ancestry(n):
    
    """Calculates the number of ancestors if we go back n generations """
    
    if n == 0:     #special case when n is 0
        return 1    # only 1 generation

    else:               #in all other cases:
        return ancestry(n-1) * 2   #keep multiplying with 2 until n reaches 0


#Question 3



def reverse(input_string):

    """Takes a string parameter and returns it in reverse recursevly """

    if len(input_string) == 0:  #base case when lenght of the string is 0
        return input_string     #empty string

    else:                                          
        return reverse(input_string[1:]) + input_string[0]
                  # Leter by leter starting with the first letter,
                  #after adding all string letters
                  #the original string ends up being in reverse



#Question 4


def palindrome(string):

    """Recursively determines if a given string is a palindrome """
    
    if len(string) < 2:  #base case when lenght of the string is either 1 or 0
        return True       #the string will always be a palindrome

    if string[0] != string[-1]:  #base case when first letter of the string is not identical to the last
        return False            # the string can't be a palindrome

    return palindrome(string[1:-1])  #each recursion removes first and last letter from string




#Question 5


#5a
    
import random  #to generate random numbers


class Duck:
   
    """A duck class with each object containig wingspan and weight variables """
    
    def __init__(self):   #initializes the wingspan and weight variables for each duck
        
        self.wingspan = round(random.uniform(80.0,100.0), 1)  # wingspan is randomly generated
        self.weight = round(random.uniform(0.7, 1.6), 2)   #the same is the case with weight
        

#5b
        
def makeFlock(n):

    """Returns a list of n Duck objects """

    duckList = [] #empty list that will be filled with duck objects

    for i in range(n):      # for loop that goes n times
        duckList.append(Duck())   #appends another generated duck object to the list

    return duckList  #returns the final list with duck objects


#5c

def sortDucks(ducks):

    """Tackes a list of Duck objects as a parameter,
    and returs the list in ascending order according to the ducks wingspan"""
    
    aList = []  # empty list that will be filled with duck object's wingspan measures

    try:                                #to avoid the "float has no atribute wingspan" error related to the recursive method 
        for i in range(len(ducks)):     #goes through the list of duck objects
            aList.append(ducks[i].wingspan)   #extracts the wingspan measure from each object and appends it to the list
    except:                         #this will always be the case after it runs first time
        for i in range(len(ducks)): #goes through the list of wingspan measures that recursevly will be put as parameter
            aList.append(ducks[i])  #appends each measure to the empty list
    #print aList 
    
    if(len(aList)<=1):    #base case when the lenght of the local list is smaller or equal to 0

	    return aList   # the local list is returned
	
    #recursive case (break down the list)
    front = sortDucks(aList[:len(aList)/2])  #first half of the list
    back = sortDucks(aList[len(aList)/2:])   #second half
	
    #merging
    aList = []  #after front and back is established the list is emptied
    a=0    #some type of counter
    b=0    #
    
    while(True):                         #while loop for the merged sort
	    if(front[a]<=back[b]):       # in case first element of first half is smaller or equal to the first element of second half
		    aList.append(front[a])  #first element of first half is appended to the list
		    a+=1                  #counter goes up so it will go to the next letter
	    else:                         #in all the other cases
		    aList.append(back[b])  #first letter that wasn't considered yet of the second half is attached to the list 
		    b+=1                #second half's counter goes up by one
	
	    if(a==len(front)):         #another if statement, if a is equal to the lenght of first half of the list
		    aList.extend(back[b:])  #adds to the list what follows from the bth element of the second half
		    return aList       
	    elif(b==len(back)):
		    aList.extend(front[a:])
		    return aList
        
    
