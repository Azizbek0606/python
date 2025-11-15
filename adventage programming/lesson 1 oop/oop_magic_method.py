class Facebook:
    def __init__(self, first_name, last_name, id, balcklist = [], friends = []):
        self.first_name = first_name
        self.last_name = last_name
        self.id = id
        self.balcklist = []
        self.friends = []
        self.posts = []

    def add_friend(self, friend_id):
        if friend_id in self.friends:
            print(f"{friend_id.first_name} is already in your friends list!")
            return
        if friend_id not in self.balcklist:
            self.friends.append(friend_id)
            print(f"{friend_id.first_name} added to friends list!")
        else:
            print(f"{friend_id.first_name} is in your blacklist!")

    def remove_friend(self, friend_id):
        if friend_id in self.friends:
            self.friends.remove(friend_id)
            print(f"for {self.full_name()} : {friend_id.first_name} removed from friends list!")
        else:
            print(f"{self.full_name()} : {friend_id.first_name} is not in your friends list!")
    
    def add_to_blacklist(self, user_id):
        if user_id in self.friends:
            self.friends.remove(user_id)
        if user_id not in self.balcklist:
            self.balcklist.append(user_id)
            print(f"for {self.full_name()} : {user_id.first_name} added to blacklist!")
        else:
            print(f"{self.full_name()}'s friend: {user_id.first_name} is already in your blacklist!")

    
    def get_friends(self):

        if not self.friends:
            print("Friends list is empty!")
        else:
            print(f"Friends list for {self.first_name} {self.last_name}:")
            for friend in self.friends:
                print(friend.get_full_name())
    
    def get_blacklist(self):
        if not self.balcklist:
            print("Blacklist is empty!")
        else:
            print(f"Blacklist for {self.first_name} {self.last_name}:")
            for user in self.balcklist:
                print(f"{user.id} - {user.first_name} {user.last_name}")
    
    def create_post(self, content):
        self.posts.append(content)
        print("Post created successfully!")
    

    def get_posts(self):
        if not self.posts:
            print("No posts available!")
        else:
            print(f"Posts by {self.first_name} {self.last_name}:")
            for idx, post in enumerate(self.posts, 1):
                print(f"{idx}. {post}")
            
            print("================ Your Friends' Posts ================")
            for friend in self.friends:
                if friend.posts:
                    print(f"Posts by {friend.first_name} {friend.last_name}:")
                    for idx, post in enumerate(friend.posts, 1):
                        print(f"{idx}. {post}")
                else:
                    print(f"{friend.first_name} {friend.last_name} has no posts.")
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def friend_recommendations(self):
        if not self.friends:
            print("No friends to base recommendations on.")
            return
        if len(self.friends) <= 0:
            print("Not enough friends to provide recommendations.")
            return
        print("Friend recommendations")
        for rec_friend in self.friends:
            for friend_of_friend in rec_friend.friends:
                if (friend_of_friend not in self.friends and 
                    friend_of_friend != self and 
                    friend_of_friend not in self.balcklist):
                    print(f"{friend_of_friend.id} - {friend_of_friend.first_name} {friend_of_friend.last_name}")



# Create 5 instances of the Facebook class
user1 = Facebook("Ali", "Valiyev", 1)
user2 = Facebook("Nodira", "Ahmedova", 2)
user3 = Facebook("Bobur", "Mirzayev", 3)
user4 = Facebook("Zilola", "Yusupova", 4)
user5 = Facebook("Shaxzod", "Karimov", 5)

# Test all methods for each instance
print("=== Testing all methods for each user ===\n")

# Test for user1
print("=== Testing for User 1 (Ali Valiyev) ===")
print("1. Full Name:")
print(user1.full_name())
print("\n2. Add Friends:")
user1.add_friend(user2)  # Add Nodira
user1.add_friend(user3)  # Add Bobur
user1.add_friend(user2)  # Try adding Nodira again (should show already in list)
print("\n3. Get Friends:")
user1.get_friends()
print("\n4. Create Posts:")
user1.create_post("Hello, this is my first post!")
user1.create_post("Enjoying a great day!")
print("\n5. Get Posts:")
user1.get_posts()
print("\n6. Add to Blacklist:")
user1.add_to_blacklist(user4)  # Blacklist Zilola
user1.add_to_blacklist(user4)  # Try blacklisting Zilola again
user1.add_friend(user4)  # Try adding Zilola (should be blocked by blacklist)
print("\n7. Get Blacklist:")
user1.get_blacklist()
print("\n8. Remove Friend:")
user1.remove_friend(user2)  # Remove Nodira
user1.remove_friend(user2)  # Try removing Nodira again
print("\n9. Friend Recommendations:")
user1.friend_recommendations()  # Should show no recommendations yet
print("\n")

# Test for user2
print("=== Testing for User 2 (Nodira Ahmedova) ===")
print("1. Full Name:")
print(user2.full_name())
print("\n2. Add Friends:")
user2.add_friend(user3)  # Add Bobur
user2.add_friend(user4)  # Add Zilola
print("\n3. Get Friends:")
user2.get_friends()
print("\n4. Create Posts:")
user2.create_post("Loving the new features!")
print("\n5. Get Posts:")
user2.get_posts()
print("\n6. Add to Blacklist:")
user2.add_to_blacklist(user5)  # Blacklist Shaxzod
print("\n7. Get Blacklist:")
user2.get_blacklist()
print("\n8. Remove Friend:")
user2.remove_friend(user3)  # Remove Bobur
print("\n9. Friend Recommendations:")
user2.friend_recommendations()
print("\n")

# Test for user3
print("=== Testing for User 3 (Bobur Mirzayev) ===")
print("1. Full Name:")
print(user3.full_name())
print("\n2. Add Friends:")
user3.add_friend(user4)  # Add Zilola
user3.add_friend(user5)  # Add Shaxzod
print("\n3. Get Friends:")
user3.get_friends()
print("\n4. Create Posts:")
user3.create_post("Just joined the platform!")
user3.create_post("Excited to connect!")
print("\n5. Get Posts:")
user3.get_posts()
print("\n6. Add to Blacklist:")
user3.add_to_blacklist(user1)  # Blacklist Ali
print("\n7. Get Blacklist:")
user3.get_blacklist()
print("\n8. Remove Friend:")
user3.remove_friend(user4)  # Remove Zilola
print("\n9. Friend Recommendations:")
user3.friend_recommendations()
print("\n")

# Test for user4
print("=== Testing for User 4 (Zilola Yusupova) ===")
print("1. Full Name:")
print(user4.full_name())
print("\n2. Add Friends:")
user4.add_friend(user5)  # Add Shaxzod
print("\n3. Get Friends:")
user4.get_friends()
print("\n4. Create Posts:")
user4.create_post("Happy to be here!")
print("\n5. Get Posts:")
user4.get_posts()
print("\n6. Add to Blacklist:")
user4.add_to_blacklist(user2)  # Blacklist Nodira
print("\n7. Get Blacklist:")
user4.get_blacklist()
print("\n8. Remove Friend:")
user4.remove_friend(user5)  # Remove Shaxzod
print("\n9. Friend Recommendations:")
user4.friend_recommendations()  # Should show no friends
print("\n")

# Test for user5
print("=== Testing for User 5 (Shaxzod Karimov) ===")
print("1. Full Name:")
print(user5.full_name())
print("\n2. Add Friends:")
user5.add_friend(user1)  # Add Ali
user5.add_friend(user2)  # Try adding Nodira (should be blocked by blacklist)
print("\n3. Get Friends:")
user5.get_friends()
print("\n4. Create Posts:")
user5.create_post("New to the community!")
print("\n5. Get Posts:")
user5.get_posts()
print("\n6. Add to Blacklist:")
user5.add_to_blacklist(user3)  # Blacklist Bobur
print("\n7. Get Blacklist:")
user5.get_blacklist()
print("\n8. Remove Friend:")
user5.remove_friend(user1)  # Remove Ali
print("\n9. Friend Recommendations:")
user5.friend_recommendations()  # Should show no friends
print("\n")

# Additional test for friend recommendations with mutual friends
print("=== Testing Friend Recommendations with Mutual Connections ===")
user1.add_friend(user5)  # Ali adds Shaxzod
user5.add_friend(user3)  # Shaxzod adds Bobur (not blacklisted now)
user3.add_friend(user2)  # Bobur adds Nodira
print("\nUser 1 (Ali) Friend Recommendations after new connections:")
user1.friend_recommendations()  # Should recommend friends of Shaxzod and Bobur