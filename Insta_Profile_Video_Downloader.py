import instaloader

L = instaloader.Instaloader()

# Login
username = input('Please enter your Instagram username: ')
password = input('Please enter your Instagram password: ')
L.context.log("Logging in...")
L.context.session = instaloader.Session()
L.context.session.login(username, password)

# Get user input for profile name, target file, and number of videos to download
profile_name = input('Please insert the user profile name: ') #e.g: 'sejutasunnah'
target_file = input('Please insert the target file name: ')
num_videos = int(input('Please insert the number of videos you want to download: '))

profile = instaloader.Profile.from_username(L.context, profile_name)
posts = profile.get_posts()

num_videos_downloaded = 0
num_videos_available = sum(1 for post in posts if post.is_video)

if num_videos_available == 0:
    print(f"No videos found in {profile_name}'s profile.")
else:
    for post in posts:
        try:
            if post.is_video:
                L.download_post(post, target=target_file)
                num_videos_downloaded += 1

                if num_videos_downloaded == num_videos:
                    break

                print('\n')
        except Exception as e:
            print(f"An error occurred while downloading {post.url}. Error message: {str(e)}")

    if num_videos_downloaded < num_videos:
        print(f"Only {num_videos_downloaded} out of {num_videos} videos found and downloaded.")

