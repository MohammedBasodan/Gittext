cars = ["bmw" , "mearcedes" , "maserati" , "alfaromeo" , "honda" , "ferrari"]
print (cars[-2])
print (cars[1])
print (cars[-1])
print (cars[:2])
print (cars[2:])
print (cars[1:3])
cars[2] = "kia"
print (cars[2])

speed = [20 , 50 , 80 , 120 , 170 , 250]
print (cars)
print (speed)
cars.extend(speed)
print (cars)
cars = ["bmw" , "mearcedes" , "maserati" , "alfaromeo" , "honda" , "ferrari"]
cars.insert(2, "bentley")
cars.append("bentley")
print (cars)
cars = ["bmw" , "mearcedes" , "maserati" , "alfaromeo" , "honda" , "ferrari"]
cars.insert(2, "bentley")
print (cars)
cars = ["bmw" , "mearcedes" , "maserati" , "alfaromeo" , "honda" , "ferrari"]
cars.remove("alfaromeo")
print (cars)
cars = ["bmw" , "mearcedes" , "maserati" , "alfaromeo" , "honda" , "ferrari"]
cars.clear()
print (cars)
cars = ["bmw" , "mearcedes" , "maserati" , "alfaromeo" , "honda" , "ferrari"]
cars.pop()
print (cars)
print (cars.index("bmw"))

h = cars.index("honda")
print (h)

cars = ["bmw" , "mearcedes" , "maserati" , "bmw" , "alfaromeo" , "honda" , "ferrari"]
count = cars.count("bmw")
print (count)
cars.sort()
print (cars)
speed = [18 , 17 , 8 , 5 , 20 , 10 ]
speed.sort()
print (speed)

cars.reverse()
speed.reverse()
print (cars)
print (speed)

cars = ["bmw" , "mearcedes" , "maserati" , "alfaromeo" , "honda" , "ferrari"]
cars2 = cars.copy()
print (cars2)




















