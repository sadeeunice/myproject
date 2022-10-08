'''
Folasade Orepo- Orjay and Marte Borgmann
HW08, CS111
This program takes in mystery wines and analyzes its qualities to define it as either red or white
'''
import math
###
# Functions for Part I
###
def get_name_mapping():
    '''
    A function that will return a dictionary that
    maps features of the data (strings) to their
    corresponding index (int).'''
    name_map = {}
    name_map['fixed acidity'] = 0
    name_map['volatile acidity'] = 1 
    name_map['citric acid'] = 2 
    name_map['residual sugar'] = 3
    name_map['chlorides'] = 4 
    name_map['free sulfur dioxide'] = 5 
    name_map['total sulfur dioxide'] = 6 
    name_map['density'] = 7 
    name_map['pH'] = 8 
    name_map['sulphates'] = 9 
    name_map['alcohol'] = 10 
    
    return(name_map)

def read_wine_data(filename):
    '''
    A funtion that takes in the data from a file and returns a dictionary with the key being quality score, the values being the wine score at each of the qualities, and the features associated with each value being the 11 other floats defining each wine
    '''
    file = open(filename, 'r')
    
    
    #Skip over the first line in the file because it is headings and not data
    next(file)

    
    quality_data = {}
    quality_data[1] = []
    quality_data[2] = []
    quality_data[3] = []
    quality_data[4] = []
    quality_data[5] = []
    quality_data[6] = []
    quality_data[7] = []
    quality_data[8] = []
    quality_data[9] = []
    quality_data[10] = []
    
    for line in file:
        line = line.rstrip()
        data = line.split(";")

        fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides, free_sulfur_dioxide, total_sulfur_dioxide, density, pH, sulphates, alcohol, quality = float(data[0]), float(data[1]), float(data[2]), float(data[3]), float(data[4]), float(data[5]), float(data[6]), float(data[7]), float(data[8]), float(data[9]), float(data[10]), int(data[11])
        

        quality_data[quality].append((fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides, free_sulfur_dioxide, total_sulfur_dioxide, density, pH, sulphates, alcohol))
        
        
    return(quality_data)


def compute_averages(feature_list, idx):
    '''
    This function takes in a list of tuples (feature_list)
    and computes the average of items stored in index
    idx of all tuples.  
    
    For example: if feature list = [(1,2),(3,4])]
    and idx = 0, then the function will return 2 
    (the average of 1 and 3).
    '''
    
    num_idx = 0
    acc_idx = 0
    acc_num = 0
    
    #A loop through each tuple in the passed list to average floating-point values at same indices
    for i in range(len(feature_list)):
        
        #finding the tuple at i
        tuple = feature_list[i]
        #finding the value in tuple at idx
        num = tuple[idx]
        #adding together all values at the idx indicated
        acc_num += num
        #adding 1 so that there is a count of how many indices have been added to acc_num
        num_idx += 1
    #finding the average of values added
    avg_idx = acc_num / num_idx
    
    return(avg_idx)


def get_averages(quality_data):
    '''
    Computes average values for all features in the provided 
    dictionary where keys are quality scores and values are 
    lists of tuples of the features.
    
    Parameters:
    quality_data (dictionary) - a dictionary object returned by read_wine_data
    
    Returns:
    avg_data (dictionary) - a dictionary where keys are the 
    same as the quality_data dictionary and values are averages of the list of tuples stored as values in the quality_data dictionary.
    '''
    avg_data = dict()
    # a loop through the quality_data dictionary that then creates another dictionary with the averages of values from the tuples
    for key in quality_data:
        features = quality_data[key]
        
        #if statement to make sure that the range is functional
        if len(features) > 0:
            num_features = len(features[0])
            avgs = []
            for i in range(num_features):
                avgs.append(compute_averages(features, i))
            
            avg_data[key] = tuple(avgs)

    return avg_data

def print_average(average_data, name_map, data_type):
    '''
    This function takes in 3 parameters:
    (1) average_data -  a dictionary object as output by get_averages
    (2) name_map - a dictionary object as output by get_name_mapping
    (3) data_type - a string that describes one of the 11 non-quality features of the wine.
    (i.e. 'fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar','chlorides',
    'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol' )
    
    This function will print to the screen information about the average values associated with the provided feature.
    '''

    #looping through a dictionary to find the value associated with the data_type key in dictionary name_map
    for key, value in average_data.items():
        print("Quality:", key, ";", data_type, ":", average_data[key][name_map[data_type]])


###
# Functions for Part II are below here
###

def calc_distance(features1, features2):
    '''
        This function takes in two parameters:
        (1) features1 - wine features in a tuple
        (2) features2 - wine features in a tuple
        
        This function returns a value that is the absolute value of the difference between floating point numbers at the same indices in two tuples
    '''
    
    dist = 0
    
    #looping through tuples to find the absolute value of difference between same indicies in two tuples
    for idx in range(len(features1)):

        value1 = features1[idx]
        value2 = features2[idx]
        #finding the positive distance between value 1 and 2
        dist += abs(value1 - value2)

    return(dist)


def read_mystery(mystery):
    '''
    Reads a mystery file and returns a list of tuples.
    
    Parameters:
    mystery (string) - the name of the myster file to read.
    
    Returns:
    data (list) - a list of tuples of size two. Each tuple
    represent one mystery wine.  The first entry in the tuple
    is the quality of the wine.  The second entry in the tuple
    is a tuple with the feature scores (for eleven features)
    for the wine.
    '''
    file = open(mystery, 'r')
    mystery_data = file.readlines()
    file.close()

    data = []
    
    for line in mystery_data[1:]:
        line = line.rstrip() #remove trailing newline
        vals = line.split(';')
        
        # quality is 12th (last) column and is key
        num_cols = len(vals)
        quality = int(vals[num_cols - 1])
        
        # create tuple of features for data
        features = tuple([float(x) for x in vals[0:num_cols -  1]])
        
        data.append((quality, features)) 
    return data


def analyze_mystery(data, avg_red, avg_white):
    '''
    This function will analyze the wines and data
    and determine if they are red or white wine.
    This function uses calc_distance(). 
    
    Parameters:
    data (list) - a list of tuples with info about mystery wines.  
    The first value in the tuple is the quality of the wine.  The
    second value in the tuple is a tuple of features.
    
    avg_red (dictionary) - keys are quality scores and values are 
    tuples of averages of features.
    
    avg_white (dictionary) -  keys are quality scores and values are 
    tuples of averages of features'''
    
    wine_num = 1
    for wine in data:
        quality = wine[0]
        features = wine[1]
        
        #finding a tuple of values associated with the different qualities for each wine
        red_vals = avg_red[quality]
        white_vals = avg_white[quality]
        
        #calling calc_distance to find the distance between the mystery wine data and red and white wine data
        red_dist = calc_distance(features, red_vals)
        white_dist = calc_distance(features, white_vals)
        
        #if/elif statement to determine whether mystery wine is red or white
        if red_dist < white_dist:
            print("Wine", wine_num, ":", "Red wine")
        elif white_dist < red_dist:
            print("Wine", wine_num, ":", "White wine")
        
        wine_num += 1

def personal_distance(features1, features2):
    '''
    This function takes in two parameters:
    (1) features1 - wine features in a tuple
    (2) features2 - wine features in a tuple
        
    This function returns a value of the distance from the pH, index 8, of one tuple from another tuple because
    pH is one of the most defining features between red and white wines. The lower pH is more acidic and tends to be
    in white wines where as the higher pH tends to be in red wines
    '''

    dist = 0
    
    #analyzing the distance for the citric acid, chlorides and pH in both red and white wine
    value1 = features1[2] + features1[4] + features1[8]
    value2 = features2[2] + features2[4] + features2[8]
    
    #an alternative to using absolute value to find distance
    dist += math.sqrt((value1 - value2) ** 2)
    
    return(dist)

def analyze_mystery2(data, avg_red, avg_white):
    '''
    This function is the same as analyze_mystery, but instead of calling calc_distance(), it calls personal_distance()'''
    
    wine_num = 1
    for wine in data:
        quality = wine[0]
        features = wine[1]
        
        #finding a tuple of values associated with the different qualities for each wine
        red_vals = avg_red[quality]
        white_vals = avg_white[quality]
        
        #calling personal_distance to find the distance between the mystery wine data and red and white wine data
        red_dist = personal_distance(features, red_vals)
        white_dist = personal_distance(features, white_vals)
        
        #if/elif statement to determine whether mystery wine is red or white
        if red_dist < white_dist:
            print("Wine", wine_num, ":", "Red wine")
        elif white_dist < red_dist:
            print("Wine", wine_num, ":", "White wine")
        
        wine_num += 1


def main():
    
    name_map = get_name_mapping()
    
    ###
    # Printing Info about Red Wines
    ###
    red_data = read_wine_data('winequality-red.csv')
    avg_red = get_averages(red_data)
    print("Red wine data:")
    print_average(avg_red, name_map, 'fixed acidity')
    print("=======\n")
    
    ###
    # Printing Info about White Wines
    ###
    white_data = read_wine_data('winequality-white.csv')
    avg_white = get_averages(white_data)
    print("White wine data:")
    print_average(avg_white, name_map, 'fixed acidity')
    print("=======\n")
 
    ###
    # Printing Info about classifying mystery wines
    ###


    data = read_mystery("mystery_data.csv")
    
    print("Analyze Mystery data: Absolute Distance")
    analyze_mystery(data, avg_red, avg_white)
    print("=======\n")

    print("Analyze Mystery data: Personal Distance")
    analyze_mystery2(data, avg_red, avg_white)
    print("=======\n")


if __name__ == '__main__':
    main()
