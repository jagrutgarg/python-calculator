print("Welcome to our J calculator")

while True:
  y=str(input("What do you want to perform - \nConversions  \nArithematic Operators \nStandard Formulas : "))
  
  if (y)=="conversions" or (y)=="Conversions" or (y)=="CONVERSIONS":
    print("Which conversion would you like to perform - \nCurrency \nTemperature \nLength")
    conversion=str(input("Enter the Conversion you want to perform : "))
    
    if str(conversion)=="Currency" or (conversion)=="currency" or (conversion)=="currency":
      print("Which Currency would you like to convert - \nEuro €\nCanadian Dollar \nRupees ₨\nYen ¥\nYuan ¥\nAmerican Dollar")
      currency=str(input("Enter the currency which you like to convert : "))

      if (currency)=="Euro" or (currency)=="euro" or (currency)=="EURO":
                   euro=str(input("Enter the currency to which you want to convert Euro : "))

                   if (euro)=="Rupees" or (euro)=="rupees" or (euro)=="RUPEES":
                     num1=float(input("Enter the Euros € : "))
                     result=num1*82.01
                     print("The answer is : ",result," ₨ ")

                   elif (euro)=="Yen" or (euro)=="yen" or (euro)=="YEN":
                     num1=float(input("Enter the Euros € : "))
                     result=num1*115.76
                     print("The answer is : ",result," ¥")
                     
                   elif (euro)=="Yuan" or (euro)=="yuan" or (euro)=="YUAN":
                     num1=float(input("Enter the Euros € : "))
                     result= num1*7.68
                     print("The answer is : ",result," ¥")
                                
                   elif (euro)=="Canadian Dollar" or (euro)=="Canadian dollar" or (euro)=="CANADIAN DOLLAR" or (euro)=="canadian dollar":
                     num1=float(input("Enter the Euros € : "))
                     result=num1*1.526
                     print("The answer is : ",result," Dollars")

                   elif (euro)=="American Dollar" or (euro)=="American dollar" or (euro)=="AMERICAN DOLLAR" or (euro)=="american dollar":
                     num1=float(input("Enter the Euros € : "))
                     result=num1*1.0817
                     print("The answer is : ",result," Dollars")
                      
                   else:
                     print("Invalid")
                     
      elif (currency)=="Canadian Dollar" or (currency)=="Canadian dollar" or (currency)=="CANADIAN DOLLAR" or (currency)=="canadian dollar":
        euro=str(input("Enter the currency to which you want to convert Canadian dollar : "))

        if (euro)=="Rupees" or (euro)=="rupees" or (euro)=="RUPEES":
          num1=float(input("Enter the Canadian Dollars : "))
          result=num1*55.34
          print("The answer is : ",result," ₨ ")

        elif (euro)=="Yen" or (euro)=="yen" or (euro)=="YEN":
          num1=float(input("Enter the Canadian Dollars : "))
          result=num1*75.8577
          print("The answer is : ",result," ¥")
                     
        elif (euro)=="Yuan" or (euro)=="yuan" or (euro)=="YUAN":
          num1=float(input("Enter the Canadian Dollars : "))
          result=num1*5.0335
          print("The answer is : ",result," ¥")
                                
        elif (euro)=="Euro" or (euro)=="euro" or (euro)=="EURO":
          num1=float(input("Enter the Canadian Dollar: "))
          result=num1*0.6553
          print("The answer is : ",result," €")

        elif (euro)=="American Dollar" or (euro)=="American dollar" or (euro)=="AMERICAN DOLLAR" or (euro)=="american dollar":
          num1=float(input("Enter the Canadian Dollar : "))
          result=num1*0.7088
          print("The answer is : ",result," Dollars")

        else:
          print("Invalid")

      elif (currency)=="rupees" or (currency)=="Rupees" or (currency)=="RUPEES":
        euro=str(input("Enter the currency to which you want to convert rupees : "))

        if (euro)=="Euro" or (euro)=="euro" or (euro)=="EUROS":
          
          num1=float(input("Enter the Rupees ₨ : "))
          result=num1*0.01219
          print("The answer is : ",result," €")

        elif (euro)=="Yen" or (euro)=="yen" or (euro)=="YEN":
          num1=float(input("Enter the Rupees ₨ : "))
          result=num1*1.4116
          print("The answer is : ",result," ¥")
                     
        elif (euro)=="Yuan" or (euro)=="yuan" or (euro)=="YUAN":
          num1=float(input("Enter the Rupees ₨ : "))
          result=num1*0.09336
          print("The answer is : ",result," ¥")
                                
        elif (euro)=="Canadian Dollar" or (euro)=="Canadian dollar" or (euro)=="CANADIAN DOLLAR" or (euro)=="canadian dollar":
          num1=float(input("Enter the Rupees ₨ : "))
          result=num1*0.01861
          print("The answer is : ",result," Dollars")

        elif (euro)=="American Dollar" or (euro)=="American dollar" or (euro)=="AMERICAN DOLLAR" or (euro)=="american dollar":
          num1=float(input("Enter the Rupees ₨ : "))
          result=num1*0.01319
          print("The answer is : ",result," Dollars")
                 
        else:
          print("Invalid")

      elif (currency)=="American Dollar" or (currency)=="American dollar" or (currency)=="AMERICAN DOLLAR" or (currency)=="american dollar":
        euro=str(input("Enter the currency to which you want to convert American dollar : "))

        if (euro)=="Rupees" or (euro)=="rupees" or (euro)=="RUPEES":
          num1=float(input("Enter the American Dollar : "))
          result=num1*75.817
          print("The answer is : ",result," ₨ ")

        elif (euro)=="Yen" or (euro)=="yen" or (euro)=="YEN":
          num1=float(input("Enter the American Dollars : "))
          result=num1*107.02
          print("The answer is : ",result," ¥")
                     
        elif (euro)=="Yuan" or (euro)=="yuan" or (euro)=="YUAN":
          num1=float(input("Enter the American Dollars : "))
          result=num1*7.1013
          print("The answer is : ",result," ¥")
                                
        elif (euro)=="Euro" or (euro)=="euro" or (euro)=="EURO":
          num1=float(input("Enter the American Dollar: "))
          result=num1*0.9245
          print("The answer is : ",result," €")

        elif (euro)=="Canadian Dollar" or (euro)=="Canadian dollar" or (euro)=="Canadian DOLLAR" or (euro)=="Canadian dollar":
          num1=float(input("Enter the American Dollar : "))
          result=num1*1.4108
          print("The answer is : ",result," Dollars")

        else:
          print("Invalid")

      elif (currency)=="Yen" or (currency)=="yen" or (currency)=="YEN":
        euro=str(input("Enter the currency to which you want to convert yen : "))

        if (euro)=="Euro" or (euro)=="euro" or (euro)=="EUROS":
          
          num1=float(input("Enter the Yen ¥ : "))
          result=num1*0.008639
          print("The answer is : ",result," €")

        elif (euro)=="Rupees" or (euro)=="RUPEES" or (euro)=="rupees":
          num1=float(input("Enter the Yen ¥ : "))
          result=num1*0.7084
          print("The answer is : ",result," ₨")
                     
        elif (euro)=="Yuan" or (euro)=="yuan" or (euro)=="YUAN":
          num1=float(input("Enter the Yen ¥ : "))
          result=num1*0.06635
          print("The answer is : ",result," ¥")
                                
        elif (euro)=="Canadian Dollar" or (euro)=="Canadian dollar" or (euro)=="CANADIAN DOLLAR" or (euro)=="canadian dollar":
          num1=float(input("Enter the Yen ¥ : "))
          result=num1*0.01318
          print("The answer is : ",result," Dollars")

        elif (euro)=="American Dollar" or (euro)=="American dollar" or (euro)=="AMERICAN DOLLAR" or (euro)=="american dollar":
          num1=float(input("Enter the Yen ¥ : "))
          result=num1*0.009344
          print("The answer is : ",result," Dollars")
                 
        else:
          print("Invalid")

      elif (currency)=="Yuan" or (currency)=="yuan" or (currency)=="YUAN":
        euro=str(input("Enter the currency to which you want to convert Yuan : "))

        if (euro)=="Euro" or (euro)=="euro" or (euro)=="EUROS":
          
          num1=float(input("Enter the Yuan ¥ : "))
          result=num1*0.1302
          print("The answer is : ",result," €")

        elif (euro)=="Rupees" or (euro)=="RUPEES" or (euro)=="rupees":
          num1=float(input("Enter the Yuan ¥ : "))
          result=num1*10.6765
          print("The answer is : ",result," ₨")
                     
        elif (euro)=="Yen" or (euro)=="yen" or (euro)=="YEN":
          num1=float(input("Enter the Yuan ¥ : "))
          result=num1*15.0705
          print("The answer is : ",result," ¥")
                                
        elif (euro)=="Canadian Dollar" or (euro)=="Canadian dollar" or (euro)=="CANADIAN DOLLAR" or (euro)=="canadian dollar":
          num1=float(input("Enter the Yuan ¥ : "))
          result=num1*0.1987
          print("The answer is : ",result," Dollars")

        elif (euro)=="American Dollar" or (euro)=="American dollar" or (euro)=="AMERICAN DOLLAR" or (euro)=="american dollar":
          num1=float(input("Enter the Yuan ¥ : "))
          result=num1*0.1408
          print("The answer is : ",result," Dollars")
                 
        else:
          print("Invalid")

    elif (conversion)=="Temperature" or (conversion)=="temperature" or (conversion)=="TEMPERATURE":
      temperature=str(input("Which unit would you like to convert \nCelsius \nFahrenheit \nKelvin : "))

      if (temperature)=="Celsius" or (temperature)=="CELSIUS" or (temperature)=="celsius":
        unit=str(input("Enter the unit in which you want to convert ℃ : "))

        if (unit)=="Fahrenheit" or (unit)=="FAHRENHEIT" or (unit)=="fahrenheit":
          num1=float(input("Enter the number of ℃ : "))
          result=num1*33.8
          print("The answer is : ",result," ℉")

        elif (unit)=="kelvin" or (unit)=="KELVIN" or (unit)=="kelvin":
          num1=float(input("Enter the number of ℃ : "))
          result=num1*274.15
          print("The answer is : ",result," kelvin")

        else:
          print("Invalid input")

      elif (temperature)=="Fahrenheit" or (temperature)=="fahrenheit" or (temperature)=="FAHRENHEIT":
        unit=str(input("Enter the unit in which you want to convert ℉ : "))

        if (unit)=="Kelvin" or (unit)=="KELVIN" or (unit)=="kelvin":
          num1=float(input("Enter the number of ℉ : "))
          result=num1*255.9278
          print("The answer is : ",result," kelvin")

        elif (unit)=="Celsius" or (unit)=="CELSIUS" or (unit)=="celsius":
          print("Not possible")

        else:
          print("Invalid Input")

      elif (temperature)=="kelvin" or (temperature)=="KELVIN" or (temperature)=="Kelvin":
        print("Unable to perform")

      else:
        print("Invalid Input")

    elif (conversion)=="Length" or (conversion)=="LENGTH" or (conversion)=="length":
      inch=str(input("Which unit would you like to convert \nNanometres (Nm)\nKilometres (Km)\nCentimetres (Cm)\nMillimetres (Mm)\nInches \nFeet \nMetres (M): "))

      if (inch)=="Nanometres" or (inch)=="NANOMETRES" or (inch)=="nanometres" or (inch)=="Nm" or (inch)=="NM" or (inch)=="nm":
        unit=str(input("Enter the unit in which you want to convert the Nanometres : "))

        if (unit)=="kilometres" or (unit)=="KILOMETRES" or (unit)=="Kilometres" or (unit)=="km" or (unit)=="KM" or (unit)=="Km":
          num1=float(input("Enter the number of Nanometres : "))
          result=num1*0.000000000001
          print("The answer is : ",result," Km")

        elif (unit)=="CENTIMETRES" or (unit)=="Centimetres" or (unit)=="centimetres" or (unit)=="cm" or (unit)=="Cm" or (unit)=="CM":
          num1=float(input("Enter the number of Nanometres : "))
          result=num1*0.0000001
          print("The answer is : ",result," Cm")

        elif (unit)=="millimetres" or (unit)=="MILLIMETRES" or (unit)=="Millimetres" or (unit)=="MM" or (unit)=="Mm" or (unit)=="mm":
          num1=float(input("Enter the number of Nanometres : "))
          result=num1*0.000001
          print("The answer is : ",result," Mm")

        elif (unit)=="Metres" or (unit)=="METRES" or (unit)=="metres" or (unit)=="M" or (unit)=="m":
          num1=float(input("Enter the number of Nanometres : "))
          result=num1*0.000000001
          print("The answer is : ",result," M")

        elif (unit)=="Inches" or (unit)=="INCHES" or (unit)=="inches":
          num1=float(input("Enter the number of Nanometres : "))
          result=num1*0.000000039370079
          print("The answer is : ",result," Inches")

        elif (unit)=="FEET" or (unit)=="Feet" or (unit)=="feet":
          num1=float(input("Enter the number of nanometres : "))
          result=num1*0.00000000328084
          print("The answer is : ",result," Feet")

        else:
          print("Invalid Input")

      elif (inch)=="Kilometres" or (inch)=="kilometres" or (inch)=="KILOMETRES" or (inch)=="KM" or (inch)=="km" or (inch)=="Km":
        unit=str(input("Enter the unit in which in which you want to convert the kilometres : "))

        if (unit)=="Nanometres" or (unit)=="nanometres" or (unit)=="NANOMETRES" or (unit)=="nm" or (unit)=="NM" or (unit)=="Nm":
          num1=float(input("Enter the number of Kilometres : "))
          result=num1*1000000000000
          print("The answer is : ",result," Nm")

        elif (unit)=="CENTIMETRES" or (unit)=="Centimetres" or (unit)=="centimetres" or (unit)=="cm" or (unit)=="Cm" or (unit)=="CM":
          num1=float(input("Enter the number of Kilometres : "))
          result=num1*100000
          print("The answer is : ",result," Cm")

        elif (unit)=="millimetres" or (unit)=="MILLIMETRES" or (unit)=="Millimetres" or (unit)=="MM" or (unit)=="Mm" or (unit)=="mm":
          num1=float(input("Enter the number of Kilometres : "))
          result=num1*1000000
          print("The answer is : ",result," Mm")

        elif (unit)=="Metres" or (unit)=="METRES" or (unit)=="metres" or (unit)=="M" or (unit)=="m":
          num1=float(input("Enter the number of Kilometres : "))
          result=num1*1000
          print("The answer is : ",result," M")

        elif (unit)=="Inches" or (unit)=="INCHES" or (unit)=="inches":
          num1=float(input("Enter the number of Kilometres : "))
          result=num1*39370.08
          print("The answer is : ",result," Inches")

        elif (unit)=="FEET" or (unit)=="Feet" or (unit)=="feet":
          num1=float(input("Enter the number of kilometres : "))
          result=num1*3280.84
          print("The answer is : ",result," Feet")

        else:
          print("Invalid Input")

      elif (inch)=="CENTIMETRES" or (inch)=="centimetres" or (inch)=="Centimetres" or (inch)=="CM" or (inch)=="Cm" or (inch)=="cm":
        unit=str(input("Enter the unit in which in which you want to convert the Centimetres : "))

        if (unit)=="Nanometres" or (unit)=="nanometres" or (unit)=="NANOMETRES" or (unit)=="nm" or (unit)=="NM" or (unit)=="Nm":
          num1=float(input("Enter the number of Centimetres : "))
          result=num1*10000000
          print("The answer is : ",result," Nm")

        elif (unit)=="KILOMETRES" or (unit)=="Kilometres" or (unit)=="kilometres" or (unit)=="km" or (unit)=="Km" or (unit)=="KM":
          num1=float(input("Enter the number of Centimetres : "))
          result=num1*0.00001
          print("The answer is : ",result," Km")

        elif (unit)=="millimetres" or (unit)=="MILLIMETRES" or (unit)=="Millimetres" or (unit)=="MM" or (unit)=="Mm" or (unit)=="mm":
          num1=float(input("Enter the number of Centimetres : "))
          result=num1*10
          print("The answer is : ",result," Mm")

        elif (unit)=="Metres" or (unit)=="METRES" or (unit)=="metres" or (unit)=="M" or (unit)=="m":
          num1=float(input("Enter the number of Centimetres : "))
          result=num1*0.01
          print("The answer is : ",result," M")

        elif (unit)=="Inches" or (unit)=="INCHES" or (unit)=="inches":
          num1=float(input("Enter the number of Centimetres : "))
          result=num1*0.393701
          print("The answer is : ",result," Inches")

        elif (unit)=="FEET" or (unit)=="Feet" or (unit)=="feet":
          num1=float(input("Enter the number of Centimetres : "))
          result=num1*0.032808
          print("The answer is : ",result," Feet")

        else:
          print("Invalid Input")

      elif (inch)=="MILLIMETRES" or (inch)=="millimetres" or (inch)=="Millimetres" or (inch)=="MM" or (inch)=="Mm" or (inch)=="mm":
        unit=str(input("Enter the unit in which in which you want to convert the Millimetres : "))

        if (unit)=="Nanometres" or (unit)=="nanometres" or (unit)=="NANOMETRES" or (unit)=="nm" or (unit)=="NM" or (unit)=="Nm":
          num1=float(input("Enter the number of Millimetres : "))
          result=num1*10000000
          print("The answer is : ",result," Nm")

        elif (unit)=="KILOMETRES" or (unit)=="Kilometres" or (unit)=="kilometres" or (unit)=="km" or (unit)=="Km" or (unit)=="KM":
          num1=float(input("Enter the number of Millimetres : "))
          result=num1*0.00001
          print("The answer is : ",result," Km")

        elif (unit)=="centimetres" or (unit)=="CENTIMETRES" or (unit)=="Centimetres" or (unit)=="CM" or (unit)=="Cm" or (unit)=="cm":
          num1=float(input("Enter the number of Millimetres : "))
          result=num1*10
          print("The answer is : ",result," Cm")

        elif (unit)=="Metres" or (unit)=="METRES" or (unit)=="metres" or (unit)=="M" or (unit)=="m":
          num1=float(input("Enter the number of Millimetres : "))
          result=num1*0.01
          print("The answer is : ",result," M")

        elif (unit)=="Inches" or (unit)=="INCHES" or (unit)=="inches":
          num1=float(input("Enter the number of Millimetres : "))
          result=num1*0.393701
          print("The answer is : ",result," Inches")

        elif (unit)=="FEET" or (unit)=="Feet" or (unit)=="feet":
          num1=float(input("Enter the number of Millimetres : "))
          result=num1*0.032808
          print("The answer is : ",result," Feet")

        else:
          print("Invalid Input")

      elif (inch)=="METRES" or (inch)=="metres" or (inch)=="metres" or (inch)=="M" or (inch)=="m":
        unit=str(input("Enter the unit in which in which you want to convert the Metres : "))

        if (unit)=="Nanometres" or (unit)=="nanometres" or (unit)=="NANOMETRES" or (unit)=="nm" or (unit)=="NM" or (unit)=="Nm":
          num1=float(input("Enter the number of Metres : "))
          result=num1*1000000000
          print("The answer is : ",result," Nm")

        elif (unit)=="KILOMETRES" or (unit)=="Kilometres" or (unit)=="kilometres" or (unit)=="km" or (unit)=="Km" or (unit)=="KM":
          num1=float(input("Enter the number of Metres : "))
          result=num1*0.001
          print("The answer is : ",result," Km")

        elif (unit)=="centimetres" or (unit)=="CENTIMETRES" or (unit)=="Centimetres" or (unit)=="CM" or (unit)=="Cm" or (unit)=="cm":
          num1=float(input("Enter the number of Metres : "))
          result=num1*100
          print("The answer is : ",result," Cm")

        elif (unit)=="Millimetres" or (unit)=="MILLIMETRES" or (unit)=="millimetres" or (unit)=="MM" or (unit)=="mm" or (unit)=="Mm":
          num1=float(input("Enter the number of Metres : "))
          result=num1*1000
          print("The answer is : ",result," Mm")

        elif (unit)=="Inches" or (unit)=="INCHES" or (unit)=="inches":
          num1=float(input("Enter the number of Metres : "))
          result=num1*39.37008
          print("The answer is : ",result," Inches")

        elif (unit)=="FEET" or (unit)=="Feet" or (unit)=="feet":
          num1=float(input("Enter the number of Metres : "))
          result=num1*3.28084
          print("The answer is : ",result," Feet")

        else:
          print("Invalid Input")

      elif (inch)=="Inch" or (inch)=="INCH" or (inch)=="inch":
        unit=str(input("Enter the unit in which in which you want to convert the Inches : "))

        if (unit)=="Nanometres" or (unit)=="nanometres" or (unit)=="NANOMETRES" or (unit)=="nm" or (unit)=="NM" or (unit)=="Nm":
          num1=float(input("Enter the number of Inches : "))
          result=num1*25400000
          print("The answer is : ",result," Nm")

        elif (unit)=="KILOMETRES" or (unit)=="Kilometres" or (unit)=="kilometres" or (unit)=="km" or (unit)=="Km" or (unit)=="KM":
          num1=float(input("Enter the number of Inches : "))
          result=num1*0.000025
          print("The answer is : ",result," Km")

        elif (unit)=="centimetres" or (unit)=="CENTIMETRES" or (unit)=="Centimetres" or (unit)=="CM" or (unit)=="Cm" or (unit)=="cm":
          num1=float(input("Enter the number of Inches : "))
          result=num1*2.54
          print("The answer is : ",result," Cm")

        elif (unit)=="Millimetres" or (unit)=="MILLIMETRES" or (unit)=="millimetres" or (unit)=="MM" or (unit)=="mm" or (unit)=="Mm":
          num1=float(input("Enter the number of Inches : "))
          result=num1*25.4
          print("The answer is : ",result," Mm")

        elif (unit)=="Metres" or (unit)=="METRES" or (unit)=="metres" or (unit)=="M" or (unit)=="m":
          num1=float(input("Enter the number of Inches : "))
          result=num1*0.0254
          print("The answer is : ",result," M")

        elif (unit)=="FEET" or (unit)=="Feet" or (unit)=="feet":
          num1=float(input("Enter the number of Inches : "))
          result=num1*0.083333
          print("The answer is : ",result," Feet")

        else:
          print("Invalid Input")

      elif (inch)=="Feet" or (inch)=="feet" or (inch)=="FEET":
        unit=str(input("Enter the unit in which in which you want to convert the Feet : "))

        if (unit)=="Nanometres" or (unit)=="nanometres" or (unit)=="NANOMETRES" or (unit)=="nm" or (unit)=="NM" or (unit)=="Nm":
          num1=float(input("Enter the number of Feet : "))
          result=num1*304800000
          print("The answer is : ",result," Nm")

        elif (unit)=="KILOMETRES" or (unit)=="Kilometres" or (unit)=="kilometres" or (unit)=="km" or (unit)=="Km" or (unit)=="KM":
          num1=float(input("Enter the number of Feet : "))
          result=num1*0.000305
          print("The answer is : ",result," Km")

        elif (unit)=="centimetres" or (unit)=="CENTIMETRES" or (unit)=="Centimetres" or (unit)=="CM" or (unit)=="Cm" or (unit)=="cm":
          num1=float(input("Enter the number of Feet : "))
          result=num1*30.48
          print("The answer is : ",result," Cm")

        elif (unit)=="Millimetres" or (unit)=="MILLIMETRES" or (unit)=="millimetres" or (unit)=="MM" or (unit)=="mm" or (unit)=="Mm":
          num1=float(input("Enter the number of Feet : "))
          result=num1*304.8
          print("The answer is : ",result," Mm")

        elif (unit)=="Metres" or (unit)=="METRES" or (unit)=="metres" or (unit)=="M" or (unit)=="m":
          num1=float(input("Enter the number of Feet : "))
          result=num1*0.3048
          print("The answer is : ",result," M")

        elif (unit)=="Inch" or (unit)=="INCH" or (unit)=="inch":
          num1=float(input("Enter the number of Feet : "))
          result=num1*12
          print("The answer is : ",result," Inches")

        else:
          print("Invalid Input")

    else:
      print("Invalid Input")
   
  elif (y)=="Arithematic operators" or (y)=="Arithematic Operators" or (y)=="ARITHEMATIC OPERATORS" or (y)=="arithematic operators":
     print("Which operator would you like to perform. \n \n \n+ \n- \n* \n/ \n// \n% \n!= \n== \n< \n> \n<= \n>= \nsquare \ncube")
     print()
     print()
     operator=str(input("Enter the arithematic operator which u want to perform : "))
     if str(operator)=="+":
       num1=float(input("Enter the first number : "))
       num2=float(input("Enter the second number : "))           
       result=num1+num2
       print("The answer is : ",result)
 
   
     elif str(operator)=="-":
       num1=float(input("Enter the first number : "))
       num2=float(input("Enter the second number : "))           
       result=num1-num2
       print("The answer is : ",result)

 
     elif str(operator)=="*":
       num1=float(input("Enter the first number : "))
       num2=float(input("Enter the second number : "))           
       result=num1*num2
       print("The answer is : ",result)
  
   
     elif str(operator)=="/":
       num1=float(input("Enter the first number : "))
       num2=float(input("Enter the second number : "))           
       result=num1/num2
       print("The answer is : ",result)

 
     elif str(operator)=="//":
       num1=int(input("Enter the first number : "))
       num2=int(input("Enter the second number : "))           
       result=num1//num2
       print("The answer is : ",result)
  
 
     elif str(operator)=="%":
       num1=float(input("Enter the first number : "))
       num2=float(input("Enter the second number : "))           
       result=num1%num2
       print("The answer is : ",result)


     elif str(operator)=="<":
       num1=float(input("Enter the first number : "))
       num2=float(input("Enter the second number : "))           
       result=num1<num2
       print("The answer is : ",result)


     elif str(operator)=="<=":
       num1=float(input("Enter the first number : "))
       num2=float(input("Enter the second number : "))           
       result=num1<=num2
       print("The answer is : ",result)
 
 
     elif str(operator)==">":
       num1=float(input("Enter the first number : "))
       num2=float(input("Enter the second number : "))           
       result=num1>num2
       print("The answer is : ",result)
  

     elif str(operator)==">=":
       num1=float(input("Enter the first number : "))
       num2=float(input("Enter the second number : "))           
       result=num1>=num2
       print("The answer is : ",result)


     elif str(operator)=="==":
       num1=float(input("Enter the first number : "))
       num2=float(input("Enter the second number : "))           
       result=num1==num2
       print("The answer is : ",result)


     elif str(operator)=="!=":
       num1=float(input("Enter the first number : "))
       num2=float(input("Enter the second number : "))           
       result=num1!=num2
       print("The answer is : ",result)


     elif str(operator)=="square":
       num1=float(input("Enter the number whose sq. you want to know : "))
       result=num1*num1
       print("The answer is : ",result)

     elif str(operator)=="cube" or str(operator)=="Cube":
       num1=float(input("Enter the number whose cube you want to know : "))
       result=num1*num1*num1
       print("The answer is : ",result)

     else:
       print("The above entered operator is invalid.")

  elif (y)=="standard formulas" or (y)=="Standard formulas" or (y)=="Standard Formulas" or (y)=="STANDARD FORMULAS":
     a=str(input("Which kind of formulae would you like to perform - \nArea \nPerimeter \n: "))

     if (a)=="Area" or (a)=="area" or (a)=="AREA":
       area=str(input("Which shape's area would you like to find - \nCircle \nSquare \nRectangle \nParallelogram : "))

       if (area)=="Circle" or (area)=="CIRCLE" or (area)=="circle":
         num1=float(input("Enter the radius of the circle : "))
         result=3.14*num1*num1
         print("The answer is : ",result)

       elif (area)=="Square" or (area)=="SQUARE" or (area)=="square":
         num1=float(input("Enter the side of the square : "))
         result=num1*num1
         print("The answer is : ",result)

       elif (area)=="rectangle" or (area)=="Rectangle" or (area)=="RECTANGLE":
         num1=float(input("Enter the length of the rectangle : "))
         num2=float(input("Enter the breadth of the rectangle : "))
         result=num1*num2
         print("The answer is : ",result)

       elif (area)=="parallelogram" or (area)=="Parallelogram" or (area)=="PARALLELOGRAM":
         num1=float(input("Enter the base of the parallelogram : "))
         num=float(input("Enter the height of the parallelogram : "))
         result=num1*num
         print("The answer is : ",result)

       else:
         print("Invalid input")
       
     elif (a)=="Perimeter" or (a)=="PERIMETER" or (a)=="perimeter":
       area=str(input("Which shape's perimeter would you like to find - \nCircle \nSquare \nRectangle : "))
       
       if (area)=="Circle" or (area)=="CIRCLE" or (area)=="circle":
         num1=float(input("Enter the radius of the circle : "))
         result=2*3.14*num1
         print("The answer is : ",result)

       elif (area)=="Square" or (area)=="SQUARE" or (area)=="square":
         num1=float(input("Enter the side of the square : "))
         result=num1*4
         print("The answer is : ",result)

       elif (area)=="rectangle" or (area)=="Rectangle" or (area)=="RECTANGLE":
         num1=float(input("Enter the length of the rectangle : "))
         num2=float(input("Enter the breadth of the rectangle : "))
         r=num1+num2
         result=r*2
         print("The answer is : ",result)

       else:
         print("Invalid input")

     else:
         print("Invalid input")    

  hlo=str(input("Do you want to continue : "))
  if (hlo)=="y" or (hlo)=="yes" or (hlo)=="YES" or (hlo)=="Yes" or (hlo)=="Y":
    print("Hope you will be liking our calculator")
    print()
    print()
    print()
    print()
    print()
  else:
    print("Have a nice day")
    break
"""
Syntax errors
Logical errors
"""
