

movies = [
    {"name": "Forrest Gump",       "year": 1994, "duration": 142,
     "genres": ["Drama", "Romance"]},
    {"name": "Avengers: Endgame",  "year": 2019, "duration": 181,
     "genres": ["Action", "Adventure", "Drama"]},
    {"name": "Back to the Future", "year": 1985, "duration": 114,
     "genres": ["Adventure", "Comedy", "Sci-Fi"]}
]

print("Welcome to Movie Admin!")

while True:
    print("\nChoose [a]dd, [l]ist, [s]earch, [v]iew, [d]elete or [q]uit.")
    choice = input("Your choice: ").strip().lower()          
    
    if choice == "a":
       
        name = input("Movie name: ").strip()
        while not name:
            name = input("Name cannot be blank. Movie name: ").strip()

        
        year = input("Release year: ").strip()
        while not (year.isdigit() and int(year) >= 1):
            year = input("Enter a valid year (integer ≥ 1): ").strip()
        year = int(year)

      
        duration = input("Duration in minutes: ").strip()
        while not (duration.isdigit() and int(duration) >= 1):
            duration = input("Enter a valid duration (integer ≥ 1): ").strip()
        duration = int(duration)

       
        genres_line = input("Enter genre(s) (comma-separated): ").strip()
        while not genres_line:
            genres_line = input("At least one genre required: ").strip()
        genres = [g.strip() for g in genres_line.split(",") if g.strip()]

        movies.append({"name": name, "year": year,
                       "duration": duration, "genres": genres}) 
        print("Movie added.")

   
    elif choice == "l":
        if not movies:
            print("No movies saved.")
        else:
            for idx, m in enumerate(movies, 1):              
                print(f"{idx}) {m['name']} ({m['year']})")

    
    elif choice == "s":
        if not movies:
            print("No movies saved.")
        else:
            term = input("Search term: ").strip().lower()   
            hits = [(i, m) for i, m in enumerate(movies, 1)
                    if term in m["name"].lower()]            
            if hits:
                for i, m in hits:
                    print(f"{i}) {m['name']} ({m['year']})")
            else:
                print("No matching movies found.")

   
    elif choice == "v":
        if not movies:
            print("No movies saved.")
        else:
            idx = input("Index to view: ").strip()
            while not (idx.isdigit() and 1 <= int(idx) <= len(movies)):
                idx = input("Invalid index. Try again: ").strip()
            m = movies[int(idx) - 1]
            print(f"\nName     : {m['name']}")
            print(f"Year     : {m['year']}")
            print(f"Duration : {m['duration']} minutes")
            print("Genres   :", ", ".join(m['genres']))

    
    elif choice == "d":
        if not movies:
            print("No movies saved.")
        else:
            idx = input("Index to delete: ").strip()
            while not (idx.isdigit() and 1 <= int(idx) <= len(movies)):
                idx = input("Invalid index. Try again: ").strip()
            removed = movies.pop(int(idx) - 1)               
            print(f"Deleted: {removed['name']}")

    
    elif choice == "q":
        print("Goodbye!")
        break                                                

    
    else:
        print("Invalid choice.")                             
