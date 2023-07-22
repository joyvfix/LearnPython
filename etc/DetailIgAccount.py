# Import instaloader package
import instaloader

# creating an Instaloader() object
ig = instaloader.Instaloader()

# Taking the instagram username as input from user
usrname = input("Enter username:")

# Fetching the details of provided useraname using instaloder object
profile = instaloader.Profile.from_username(ig.context, usrname)

# Printing the fetched details and storing the profile pic of that account
print("Username: ", profile.username)
print("Number of Posts Uploaded: ", profile.mediacount)
print(profile.username+" is having " + str(profile.followers)+' followers.')
print(profile.username+" is following " + str(profile.followees)+' people')
print("Bio: ", profile.biography)
instaloader.Instaloader().download_profile(usrname, profile_pic_only=True)
# {:;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;}
# from instagram_private_api import Client, ClientCompatPatch


# def get_account_info(username, password):
#     api = Client(username, password)
#     current_user = api.current_user()
#     return current_user


# if __name__ == "__main__":
#     # Replace 'your_username' and 'your_password' with your Instagram account credentials.
#     account_info = get_account_info('your_username', 'your_password')
#     print("Account Info:")
#     print("Username:", account_info["user"]["username"])
#     print("Full Name:", account_info["user"]["full_name"])
#     print("Biography:", account_info["user"]["biography"])
#     print("Followers:", account_info["user"]["follower_count"])
#     print("Following:", account_info["user"]["following_count"])
#     print("Posts:", account_info["user"]["media_count"])
