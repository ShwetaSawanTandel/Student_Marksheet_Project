name=input('Enter your Name:')
address=input('Enter your Address:')
print('Enter your Marks of given Subjects out of 100')
while True:
    Maths=int(input('Enter your Marks of Maths:'))
    if Maths<0 or Maths>100:
        print('Invallid Marks')
    else:
        physics=int(input('Enter your Marks of Physics:'))
        if physics<0 or physics>100:
            print('invalid Marks')
        else:
            Chemistry=int(input('Enter your Marks of Chemistry:'))
            if Chemistry<0 or Chemistry>100:
                print('invalid Marks')
            else: 
              Biology=int(input('Enter your Marks of Biology:'))
              if Biology<0 or Biology>100:
                  print('invalid Marks')
              else:
                English=int(input('Enter your Marks of English:'))
                if English<0 or English>100:
                     print('invalid Marks')
                else:
                    Total=int(Maths+physics+Chemistry+Biology+English)
                    percentage=((Total/500)*100)
                    print('your name=',name)
                    print('your address=',address)
                    print(Total)
                    print('=============================================================================')
                    print('SUBJECT         |Total Marks      |Obt marks            |Percentage')
                    print('=============================================================================')
                    print('Maths           |100              |',Maths,            '|',Maths)
                    print('Physics         |100              |',physics,          '|',physics)
                    print('Chemistry       |100              |',Chemistry,        '|',Chemistry)
                    print('Biology         |100              |',Biology,          '|',Biology)
                    print('English         |100              |',English,          '|',English)
                    print('=============================================================================')
                    print('Total           |500              |',Total,            '|',percentage)
                    print('=============================================================================')
                    print(Total)       
                    break

   
        













































    
