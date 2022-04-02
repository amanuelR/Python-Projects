
def  make_average_pm10_dictionary ():
    t = {}
    try:
        fin = open("who_air_data.tsv",'r')
        fin.readline();
        for line in fin:
            line_list = line.strip().split("\t")
            country = line_list[-1]
            ph10 = int (line_list[2])
            if country in t:
                t[country].append(ph10)
            else:
                t[country]= [ph10]
        fin.close()
    except FileNotFoundError as e:
        print(e)
    
    for country in t:
        ph10 = round (sum(t[country])/len(t[country]))
        t[country].clear()
        t[country].append(ph10)
        
    return  t# return a dictionary
#
# Function  that  takes a dictionary  of air  quality  for  each  country
# and  returns a dictionary  with  the  population  and air  quality  for  each  country
# if that  country  has air  quality  data
#
def  add_population_data(avg_pm10 ):

    try:
        fin = open("population.tsv",'r')
        for line in fin:
            line_list = line.strip().split("\t")
            country = line_list[1]
            population = int (line_list[2])
            if country in avg_pm10:
                avg_pm10[country].append(population)
    except FileNotFoundError as e:
        print(e)
    return  avg_pm10 # return a dictionary
#
# Print  out  country  name , population , and   pm10  values
# that  exceed  the WHO’s threshold (in ug/m3) for 1 year  pm10  levels
# that  increase  long -term  mortality  risk by 15%  from  figure 1
# Print  the  data  sorted  by the  population  of the  country
#
def print_exceeds_threshold(data ,threshold ):
    d = [[0 for y in range(3)]for x in range(len(data))]
    i = 0
    for country in data:
        if len(data[country]) == 2: #check if the country's population is provided
            d[i][0] = country
            d[i][1] = data[country][0]
            d[i][2] = data[country][1]
            i = i + 1
    d.sort(key=lambda x:x[2]) #sord the 2D list using the second element of inner list in decending order
    d.reverse() #ascendig order
    for k in range(len(d)): #iterate until the outor lope it reaches the lengeth of the 2d array
        space = " "
        second_sep = "\t\t"
        if d[k][1] >= threshold:
            if len(str (d[k][0])) == 22:
                space = " "
            else:
                for a in range(22 - len(str (d[k][0]))):
                    space = space + " "   
            print(d[k][0],space, d[k][2],second_sep,d[k][1])

def  main ():
    # Build  dictionary  from  air  quality file
    avg_pm10 = make_average_pm10_dictionary ()
    # Read in  population  and  create a dictionary
    # with  population  and  average  pm10  data  for  each
    country_data = add_population_data(avg_pm10)
    
    # print  countries  with  air  quality
    # exceeding  WHO’s guidelines  sorted  by population
    pm10_threshold = 70
    print_exceeds_threshold(country_data , pm10_threshold)
#
# run the  analysis
#
main()
