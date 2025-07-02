def SingleTon(arg):
  l=[]
  def Inner():
    if len(l)==0:
      obj=arg()
      l.append(obj)
    return l[0]
  return Inner

# movie1
@SingleTon
class WAR2():
  def __init__(self):
    self.seats=200
  def Booking(self):
    print(f'Available Seats = {self.seats}')
    tickets=int(input("Enter number of tickets = "))
    if 0<tickets<=self.seats:
      self.seats-=tickets
      print(f"{tickets} Tickets Booked Succesfully...!")
    else:
      print("tickets unavailable...!")

#Dragon Movie
@SingleTon
class Dragon():
  def __init__(self):
    self.seats=200
  def Booking(self):
    print(f'Available Seats = {self.seats}')
    tickets=int(input("Enter number of tickets = "))
    if 0<tickets<=self.seats:
      self.seats-=tickets
      print(f"{tickets} Tickets Booked Succesfully...!")
    else:
      print("tickets unavailable...!")

#Coolie movie
@SingleTon
class Coolie():
  def __init__(self):
    self.seats=200
  def Booking(self):
    print(f'Available Seats = {self.seats}')
    tickets=int(input("Enter number of tickets = "))
    if 0<tickets<=self.seats:
      self.seats-=tickets
      print(f"{tickets} Tickets Booked Succesfully...!")
    else:
      print("tickets unavailable...!")



#BMs application
def BMs():
  print("1)WAR2\n2)Dragon\n3)Coolie")
  movie = int(input("Select the movie to watch : "))
  if movie==1:
    user = WAR2()
    user.Booking()
  elif movie==2:
    user=Dragon()
    user.Booking()
  elif movie==3:
    user = Coolie()
    user.Booking()
  else:
    print("invalid option...!")


#BMs users
user1 = BMs()
print('-----')
user2 = BMs()
print('------')
user3 =BMs()


#PTm application
def PTm():
  print("1)WAR2\n2)Dragon\n3)Coolie")
  movie = int(input("Select the movie to watch : "))
  if movie==1:
    user = WAR2()
    user.Booking()
  elif movie==2:
    user=Dragon()
    user.Booking()
  elif movie==3:
    user = Coolie()
    user.Booking()
  else:
    print("invalid option...!")


#PTm users
user1 = PTm()
print('------------')
user2 = PTm()
print('------------')
user3 = PTm()
print('------------')


