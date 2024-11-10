class User:
    def __init__(self, user_id, username):  #constructor
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
        
    def follow(self, user):   #always have self parameter
        user.followers += 1
        self.following += 1
        
user_1 = User("001", "rose")
user_2 = User("002", "jane")

#user_1.id = "001"   #creating an attribute
#user_1.username = "rose"

user_1.follow(user_2)




