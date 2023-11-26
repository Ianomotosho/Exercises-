'''imagine  a lost hiker on a trail that has come to a fork in the road how does she decide what path to takes to join the rest of the party. We can guessthe hikerwill try to do any of the following'
1. call her freinds
2 find out footprints in the sand/snow
3. ask others that may br hanging ount in the vicinity if they hve see her party
4. call out to the group
5. light a flare
6. call emergercy  number'''



print('imagine you are a lost hiker on  54 trail that has come to a fork in the road.How does she decide which path to take?   choose betweem 6 things')
while True:
  choice=input('what do choose(1 = call your freinds/2 = find out footprints in the sand/snow/3 = ask others that may br hanging ount in the vicinity if they hve see her party/4 = call out to the group / 5 = light a flare / 6 =  call emergercy  number)')
  if choice in ('1','2','3','4','5','6'):
    if choice=='1':
      print('you call your freinds and they come with a big party bus with the man city squad on it and she climb aon the top of the bus and party all night')
    elif choice=='2':
      print('you look forn the footprints in the sand then you later reach a party bus with your freind and the man ciyty squad so you party all night')
    elif choice=='3':
      print('there are people having a party so you ask ifn you can go in their party and you go in and get drunk then get killed')
    elif choice=='4':
      print('she called out to the group and she asked them if they had seen a party bus and they found it and loads of LEBRON JAMES  things happened in their')
    elif choice=='5':
      print('')
    elif choice=='6': 
      print('')
    
''' write a phython program to find those numbers which are divisible by 7 and 5 between 1500 and 2700 '''

for numbers in range(1500,2700):
  if numbers %7==0 and numbers %5==0:
   print(numbers)
  else:
    print('nope this is not a divable by seven or five')

'''trying to find numbers that are divisable by 7 and five'''
for num in range(1,100):
  if num %2==0 and num %5==0:
    print(num)
  else:
    print('no')

''' write a python progam that interates the integers from 1-50 for multiples of 3 print fizz instead of the number for multiples of 5 print buzz and for number that are multiples of fizzbuzz'''

'''using a for loop'''
for num in range(1,101):
  if num %3==0 and num %5==0:
     print ('fizzbuzz')
  elif num  %5==0:
    print('buzz')
  elif num %3==0:
    print('fizz')
  else:
    print(num)

    ''' using a while loop'''
items=0
while items<101:
    if items %3==0 and items%5==0:
     print('fizz buzz')
    elif items%5==0:
     print('buzz')
    elif items%3==0:
     print('fizz')
    else:
     print(items)
    items=items+1
     