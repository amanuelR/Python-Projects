import tkinter 

class  AirQuality:
    def  __init__(self):
        self.__population_percentage = {"China":36.17 ,"India":33.62 ,\
         "Pakistan":5.37 ,"Nigeria":5.00 , "Bangladesh": 4.12}
        
        self.__pm10 = {"China":84.4,"India":107.43 , "Pakistan":338.6 ,\
        "Nigeria":202.17 ,"Bangladesh":140.5}
        
        self.__countries  =["China","India","Pakistan","Nigeria","Bangladesh"]

    def  get_percent_population(self):
        return  self.__population_percentage

    def  get_pm10(self):
        return  self.__pm10

    def  get_countries(self):
        return  self.__countries;
    def convertToRGB(self):
        rgbValues = []
        for i in self.__pm10:
            if self.__pm10[i] > 255:
                self.__pm10[i] = 255
            rgbValue = int(self.__pm10[i]) #coverts each float values to int

            #code to cover int value to rgb and then to hex color value
            blue = rgbValue
            green = rgbValue
            red = rgbValue
            rgbValue = "#%02x%02x%02x" % (red,green,blue)
            rgbValues.append(rgbValue)
        
        return rgbValues #returns list of int values

class  PLUI:
    def  __init__(self):
        self.__CANVAS_WIDTH = 320 # Canvas  width
        self.__CANVAS_HEIGHT = 240 # Canvas  height
        self.__aqd = AirQuality ()
        self.__pop_percentage = self.__aqd.get_percent_population ()
        self.__pm10 = self.__aqd.get_pm10 () #can  use  for  color
        self.__country_list = self.__aqd.get_countries ()

        # Create  the  main  window.
        self.main_window = None
        self.canvas = None
                       
    def  draw_piechart(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("Population Pie Chart")
        # Create  the  Canvas  widget.
        self.canvas = tkinter.Canvas(self.main_window ,
                                     width=self.__CANVAS_WIDTH ,
                                     height=self.__CANVAS_HEIGHT)
        
        #create an instance of AirQuality class to access its attributes and behaviors
        airQuality = AirQuality()
        countries_population = airQuality.get_percent_population() #assigns a dictionary to 'countries_population'
        
        PCP= [] #an empty list of population pie chart percent for each country

        #assign the returned list of hex values to a colorData container
        colorData = airQuality.convertToRGB()
        print(colorData)
        #add each countries contribution to the pie chart to the empty list
        for c in countries_population:
            countries_population[c] = (countries_population[c]/100) * 360
            PCP.append(countries_population[c])

        #draw pie chart on the canvas 
        coord = 60,20, 260, 230
        self.canvas.create_arc(coord, start=0, extent=PCP[0], fill=colorData[0])
        self.canvas.create_arc(coord, start=PCP[0], extent=PCP[1], fill=colorData[1])
        self.canvas.create_arc(coord, start=PCP[0] + PCP[1], extent=PCP[2], fill=colorData[2])
        self.canvas.create_arc(coord, start=PCP[0]+ PCP[1] + PCP[2], extent=PCP[3], fill=colorData[3])
        self.canvas.create_arc(coord, start=PCP[0] + PCP[1]+ PCP[2] + PCP[3], extent=PCP[4], fill=colorData[4])
        self.canvas.create_arc(coord, start=PCP[0] + PCP[1]+ PCP[2]+PCP[3] + PCP[4], extent=360 - sum(PCP), fill="Orange")
        
        self.canvas.pack()
        tkinter.mainloop ()
# Create  an  instance  of the  Plot UIclass.
plui = PLUI()
plui.draw_piechart ()
