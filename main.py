class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name: str, age: int, tracks: list, score: float):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score

    def change_name(self, name):
        self.name = name
        return self.name

    def change_age(self, age):
        if not isinstance(age, int):
            raise Exception(f"{age} is an invalid input type.")

        self.age = age
        return self.age

    def add_tracks(self, track):
        self.tracks.append(track)
        return self.tracks

    def get_score(self):
        return self.score


Bob = Student(name="Bob", age=26, tracks=["FE", "BE"], score=20.90)
print(Bob.__dict__)

# Expected methods
new_name = Bob.change_name("Peter")
new_age = Bob.change_age(34)
new_track = Bob.add_tracks("UI/UX")
bob_score = Bob.get_score()

print("name:", new_name, ",", "age:", new_age, ",", "tracks:", new_track, ",", "score:", bob_score)
