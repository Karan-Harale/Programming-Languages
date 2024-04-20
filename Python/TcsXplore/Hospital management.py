'''During the COVID19 pandemic, the status of beds availability is to be tracked

Create a class City with the below attributes:
city_id of type Number
state_name of type String
city_name of type String
covidbeds of type Number
avlblcovbeds of type Number
ventilbeds of type Number
avlblventilbeds of type Number


Attribute description:
city_id represents Unique ID for the city
state_name represents the state name
city_name represents the city name

covidbeds represents the total covid beds in the city
avlblcovbeds represents the total available covid beds in the city
ventilbeds represents the total ventilator beds in the city
avlblventilbeds represents the total available ventilator beds in the city


Create the __init__ method which takes all parameters in the above sequence. The method should set the value of attributes to parameter values .

Create another class CovBedsAnalysis with the below attributes:
analysis_name of type String
city_list of type List having city objects

Create the __init__ method which takes all parameters in the above sequence. The method should set the value of attributes to parameter values inside the method.

Create another method inside the class with the name get_StateWiseAvlblBedStats

This method is used to find the state wise available covid beds and available ventilator beds and returns a list of tuples with State name,total available covid beds and total available ventilator beds for each state, sorted by state name.


Note: A state contains multiple cities. Total number of available beds for a respective category (covid or ventilator beds) in a state is the sum of the available beds of all the cities in that state for the respective category(covid or ventilator). Refer testcase output for more clarity.


Create another method with the name get_CiitesWithMoreThanAvgOccupiedbeds, which takes state as argument and returns the dictionary with city as the key and tuple of occupied covid beds and occupied ventilator beds as value, where number of covid beds occupied and ventilator beds occupied are more than the state average for the respective category of beds .


i.e. the City(cities) in the given state to be recorded/resulted( with the data mentioned), should satisfy the below conditions:

Whose occupied covid beds count is more than the "average of Occupied covid beds of all the cities of the given state" and the respective City should also contain the Occupied ventilator beds count more than the "average of occupied ventilator beds of all cities of the given state".

For more clarity , please refer the Sample test case Input and Output in below section

If no city is found with the occupied beds more than state average as mentioned above, then return None and display ‘No city available' (Without quotes) in main function.


Please note that the search operations(if any as per the requirement ..) should be case insensitive.

Instructions to write main function:

Instructions to write main section of the code
a. You would require to write the main section completely, hence please follow the below instructions for the same.
b. You would require to write the main program which is inline to the "sample input description section" mentioned below and to read the data in the same sequence.
c. Create the respective objects(City and CovBedsAnalysis ) with the given sequence of arguments to fulfill the __init__ method requirement defined in the respective classes referring to the below instructions.

i. Create a City object after reading the data related to it and add the object to the list of city objects which will be provided to the CovBedsAnalysis object while creation.
This point repeats for the number of city objects(considered in the first line of input data) .

ii. Create CovBedsAnalysis object by passing the CovBedsAnalysis name(you can hard-code any name you want) and List of city objects ( created as mentioned in above
point# c.i ) as the arguments.
d. Take a string value as input depicting the state which is passed to the get_CiitesWithMoreThanAvgOccupiedbeds
e. Call the method get_StateWiseAvlblBedStats mentioned above from the main section.
f. Display the State,total available covid beds and total available ventilator beds received from the method, with a single space in between as shown in sample testcase output,
g. Call the method get_CiitesWithMoreThanAvgOccupiedbeds mentioned above from the main section
h. Display the city name, occupied covid beds and occupied ventilator beds with a single space in between as shown in the sample testcase output.
I. If None is returned by the method get_CiitesWithMoreThanAvgOccupiedbeds, display the message ‘No city available' (excluding the quotes).


You can use/refer the below given sample input and output to verify your solution using ' Test against Custom Input ' option in Hackerrank.


Input format for Custom Testing:

a.The 1st input taken in the main section is the number of city objects to be added to the list of cities.
b.The next set of inputs are the values for the attribtes: city_id,state_name,city_name, covidbeds,avlblcovbeds,ventilbeds,avlblventilbeds respectively for each city taken one after other and is repeated for number of objects given in the first line of testcase input
c.The last line of input refers the state name which is passed to the function: get_CiitesWithMoreThanAvgOccupiedbeds


Sample Testcase1:

Input:
5
101
Delhi
Delhi
100000
20000
5000
2000
102
Telangana
Hyderabad
200000
40000
1000
500
103
Telangana
Warangal
100000
30000
2000
1000
104
AndhraPradesh
Vijayawada
800000
300000
30000
2500
105
AndhraPradesh
Vizag
500000
100000
6000
1000
AndhraPradesh


Output:

AndhraPradesh 400000 3500
Delhi 20000 2000
Telangana 70000 1500
Vijayawada 500000 27500



Sample TestCase2:

Input:

6
101
Delhi
Delhi
100000
20000
8000
3000
102
Telangana
Hyderabad
200000
100000
12000
6000
103
Telangana
Warangal
100000
50000
1000
500
104
AndhraPradesh
Vijayawada
800000
400000
7500
3750
105
AndhraPradesh
Vizag
500000
100000
11000
8500
106
Maharashtra
Mumbai
1000000
0
12500
0
maharashtra


Output:

AndhraPradesh 500000 12250
Delhi 20000 3000
Maharashtra 0 0
Telangana 150000 6500
No city available'''

#
class City:

    def __init__(self,city_id,state_name,city_name,covidbeds,avlblcovbeds,ventilbeds,avlblventilbeds):
        self.city_id = city_id
        self.state_name = state_name
        self.city_name = city_name
        self.covidbeds=covidbeds
        self.avlblcovbeds=avlblcovbeds
        self.ventilbeds=ventilbeds
        self.avlblventilbeds=avlblventilbeds

        # print(f"{self.city_id} , {self.state_name} , {self.city_name} , {self.covidbeds} , {self.avlblcovbeds} , {self.ventilbeds} , { self.avlblventilbeds}")


class CovBedsAnalysis:

    def __init__(self,analysis_name , city_list ):
        self.analysis_name=analysis_name
        self.city_list=city_list

    def get_StateWiseAvlblBedStats(self):

        state_stats={ }

        for city in self.city_list:
            state_name=city.state_name.lower()

            if state_name in state_stats:
                state_stats[state_name][0] += city.avlblcovbeds
                state_stats[state_name][1] += city.avlblventilbeds

            else:

                state_stats[state_name] = [city.avlblcovbeds , city.avlblventilbeds]

            state_stats = sorted(state_stats.items())

            result = []

            for state, stats in state_stats:
                result.append((state.capitalize(), stats[0], stats[1]))

            return result


    def get_CiitesWithMoreThanAvgOccupiedbeds(self , state):

        state = state.lower()
        state_cities = [city for city in self.city_list if city.state_name.lower() == state]

        if not state_cities:
            return None

        total_avlbl_covbeds = sum(city.avlblcovbeds for city in state_cities)

        total_avlbl_ventilbeds = sum(city.avlblventilbeds for city in state_cities)

        avg_covbeds = total_avlbl_covbeds / len(state_cities)

        avg_ventilbeds = total_avlbl_ventilbeds / len(state_cities)

        city_data = { }

        for city in state_cities:
            if city.avlblcovbeds > avg_covbeds and city.avlblventilbeds > avg_ventilbeds:
                city_data[city.city_name] = (city.covidbeds - city.avlblcovbeds, city.ventilbeds - city.avlblventilbeds)

        if not city_data:
            return None

        return city_data



if __name__ == '__main__':



    noofCities=int(input("Enter number of Cities: "))

    city_objects=[]

    if noofCities == 0:
        print("Invalid Entry !!! \n try Again")

    for city in range(noofCities):
        city_id = int(input(f"Enter City {city+1} id   : "))
        state_name = input(f"Enter State {city+1} name : ")
        city_name = input(f"Enter City {city+1} name   : ")
        covidbeds = int(input("Enter total \n covid beds : "))
        avlblcovbeds = int(input("Enter Availbale \n covid beds : "))

        ventilbeds = int(input("Enter total \n Ventil beds : "))
        avlblventilbeds = int(input("Enter Available \n ventil beds : "))


        city=City(city_id,state_name,city_name,covidbeds,avlblcovbeds,ventilbeds,avlblventilbeds)

        city_objects.append(city)

    analysis_name = input("Enter Analysis name : ")

    Analysis = CovBedsAnalysis(analysis_name , city_objects )

    state_name = input("Enter State Name : ").strip()

    statewisebedstat = Analysis.get_StateWiseAvlblBedStats()

    f = open(f"{analysis_name} Data.txt", "a+")

    f.write("   State    avlbl_covbeds    avlbl_ventilbeds\n")

    count=0

    for state, avlbl_covbeds, avlbl_ventilbeds in statewisebedstat:

        print(f"{state} {avlbl_covbeds} {avlbl_ventilbeds}")

        count+=1

        f.write(str(count))
        f.write("  ")
        f.write(state)
        f.write("  ")
        f.write("       ")
        f.write(str(avlbl_covbeds))
        f.write("                  ")
        f.write(str(avlbl_ventilbeds))
        f.write("\n")
        f.close()


    city_data = Analysis.get_CiitesWithMoreThanAvgOccupiedbeds(state_name)

    if city_data is None:
        print("No city Available")
    else:
        for city, (occupied_covbeds, occupied_ventilbeds) in city_data.items():
            print(f"{city} {occupied_covbeds} {occupied_ventilbeds}")







# class City:
#     def __init__(self, city_id, state_name, city_name, covidbeds, avlblcovbeds, ventilbeds, avlblventilbeds):
#         self.city_id = city_id
#         self.state_name = state_name
#         self.city_name = city_name
#         self.covidbeds = covidbeds
#         self.avlblcovbeds = avlblcovbeds
#         self.ventilbeds = ventilbeds
#         self.avlblventilbeds = avlblventilbeds
#
#
# class CovBedsAnalysis:
#     def __init__(self, analysis_name, city_list):
#         self.analysis_name = analysis_name
#         self.city_list = city_list
#
#     def get_StateWiseAvlblBedStats(self):
#         state_stats = {}
#         for city in self.city_list:
#             state_name = city.state_name.lower()
#             if state_name in state_stats:
#                 state_stats[state_name][0] += city.avlblcovbeds
#                 state_stats[state_name][1] += city.avlblventilbeds
#             else:
#                 state_stats[state_name] = [city.avlblcovbeds, city.avlblventilbeds]
#
#         state_stats = sorted(state_stats.items(), key=lambda x: x[0])
#
#         result = []
#         for state, stats in state_stats:
#             result.append((state.capitalize(), stats[0], stats[1]))
#
#         return result
#
#     def get_CiitesWithMoreThanAvgOccupiedbeds(self, state):
#         state = state.lower()
#         state_cities = [city for city in self.city_list if city.state_name.lower() == state]
#         if not state_cities:
#             return None
#
#         total_avlbl_covbeds = sum(city.avlblcovbeds for city in state_cities)
#         total_avlbl_ventilbeds = sum(city.avlblventilbeds for city in state_cities)
#         avg_covbeds = total_avlbl_covbeds / len(state_cities)
#         avg_ventilbeds = total_avlbl_ventilbeds / len(state_cities)
#
#         city_data = {}
#         for city in state_cities:
#             if city.avlblcovbeds > avg_covbeds and city.avlblventilbeds > avg_ventilbeds:
#                 city_data[city.city_name] = (city.covidbeds - city.avlblcovbeds, city.ventilbeds - city.avlblventilbeds)
#
#         if not city_data:
#             return None
#
#         return city_data
#
#
# # Main program
# if __name__ == "__main__":
#     num_cities = int(input())
#     city_objects = []
#
#     for _ in range(num_cities):
#         city_id = int(input())
#         state_name = input().strip()
#         city_name = input().strip()
#         covidbeds = int(input())
#         avlblcovbeds = int(input())
#         ventilbeds = int(input())
#         avlblventilbeds = int(input())
#
#         city = City(city_id, state_name, city_name, covidbeds, avlblcovbeds, ventilbeds, avlblventilbeds)
#         city_objects.append(city)
#
#     analysis = CovBedsAnalysis("CovidBedAnalysis", city_objects)
#
#     state_name = input().strip()
#
#     state_wise_stats = analysis.get_StateWiseAvlblBedStats()
#     for state, avlbl_covbeds, avlbl_ventilbeds in state_wise_stats:
#         print(f"{state} {avlbl_covbeds} {avlbl_ventilbeds}")
#
#     city_data = analysis.get_CiitesWithMoreThanAvgOccupiedbeds(state_name)
#     if city_data is None:
#         print("No city available")
#     else:
#         for city, (occupied_covbeds, occupied_ventilbeds) in city_data.items():
#             print(f"{city} {occupied_covbeds} {occupied_ventilbeds}")
