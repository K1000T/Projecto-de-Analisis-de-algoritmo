import instaloader


# Get instance
L = instaloader.Instaloader()

# Optionally, login or load session
L.login(username, password)        # (login)

profile = instaloader.Profile.from_username(L.context, 'gustavopetrourrego')

posts = profile.get_posts()

i = 0
for post in posts:
    i+=1
    print(post.caption)
    
    print("Comentarios de este post")
    comentarios = post.get_comments()
    for j, comentario in enumerate(comentarios):
        if j < 10:
            print(f"Autor: {comentario.owner}")
            print(f"Comentario: {comentario.text}")
            print()
        else:
            break
    if i > 10: break