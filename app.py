from bs4 import BeautifulSoup

# Load followers from HTML file
def extract_usernames_from_file(filename):
    with open(filename, "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "html.parser")
        links = soup.find_all("a", href=True)
        usernames = {link.get_text().strip() for link in links if link.get("href").startswith("https://www.instagram.com/")}
        return usernames

followers_file = "followers_1.html"
following_file = "following.html"

followers = extract_usernames_from_file(followers_file)
following = extract_usernames_from_file(following_file)

# Users you follow but who don't follow you back
not_following_back = sorted(following - followers)

# Output result
print("Accounts not following you back:")
for user in not_following_back:
    print(user)

# Optional: Save to a file
with open("not_following_back.txt", "w", encoding="utf-8") as f:
    for user in not_following_back:
        f.write(user + "\n")

print(f"\nTotal: {len(not_following_back)} users not following you back.")
