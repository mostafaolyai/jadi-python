genres={
    "Horror": 0, "Romance": 0, "Comedy": 0, "History": 0 , "Adventure": 0 , "Action": 0
}

count = int(input())
for i in range(count):
    name, genre1, genre2, genre3 = [part.strip() for part in input().split(',')]
    
    #we can validate genre1, genre2, genre3

    genres[genre1] = genres[genre1] + 1
    genres[genre2] = genres[genre2] + 1
    genres[genre3] = genres[genre3] + 1

sorted_genres = dict(
    sorted(genres.items(), key=lambda item: item[1], reverse=True)
)

print(sorted_genres)