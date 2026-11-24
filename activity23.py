anime_type = ["doraemon", "marvels", "onepunchman", "dragonball"]
anime_title = ["totatola"]

while True:
    ans = input("Do you know any anime? (yes/no): ")

    if ans.lower() == 'yes':
        print("what is its type -- ? select from the list ")
        for x in anime_type:
            print(x)
        anime_type = input("type: ")

        title = input("what is the title of the anime?: ")
        anime_title.append(title)
        continue
    else:
        print("Thanks.")
        print("So far you have encoded the following.")
        for x in anime_title:
            print(x)
        break