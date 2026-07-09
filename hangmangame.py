import random

movies = [
    "DRISHYAM", "LUCIFER", "PREMAM", "PULIMURUGAN", "CHARLIE",
    "BANGALORE DAYS", "KUMBALANGI NIGHTS", "ROMANCHAM", "HRIDAYAM", "AAVESHAM",
    "MANJUMMEL BOYS", "2018", "NERU", "JAN E MAN", "HOME",
    "ANDROID KUNJAPPAN", "MINNAL MURALI", "MALIK", "JAYA JAYA JAYA JAYA HE",
    "THALLUMAALA", "RDX", "KANNUR SQUAD", "MEMORIES", "OPERATION JAVA",
    "JOSEPH", "UYARE", "HELEN", "VIRUS", "NAYATTU", "TRANCE",
    "THE GREAT INDIAN KITCHEN", "AYYAPPANUM KOSHIYUM", "CIA", "EZRA", "ISHQ",
    "DRIVING LICENCE", "KURUP", "BHEESHMA PARVAM", "VARSHANGALKKU SHESHAM",
    "GURUVAYOOR AMBALANADAYIL", "ARM", "KISHKINDHA KAANDAM", "THUDARUM",
    "PAVADA", "MAHESHINTE PRATHIKARAM", "USTAD HOTEL", "DIAMOND NECKLACE",
    "SPIRIT", "INDIAN RUPEE", "TRAFFIC", "SALT N PEPPER",
    "THATTATHIN MARAYATH", "OM SHANTI OSHANA", "NERAM", "BANGLORE DAYS",
    "ANARKALI", "ENNU NINTE MOIDEEN", "KALI", "TAKE OFF",
    "KOODE", "CAPTAIN", "LOVERS DAY", "MARAKKAR", "KAYAMKULAM KOCHUNNI",
    "PATHONPATHAM NOOTTANDU", "KING OF KOTHA", "GARUDAN", "IRATTA",
    "NNA THAAN CASE KODU", "PACHUVUM ATHBHUTHA VILAKKUM", "FALIMY", "REKHACHITHRAM",
    "THINKALAZHCHA NISHCHAYAM", "SUDANI FROM NIGERIA", "MOOTHON",
    "KAPPELA", "LOVE", "CU SOON", "FORENSIC", "ANJAAM PATHIRAA",
    "THE PRIEST", "COLD CASE", "KOOMAN", "MUKUNDAN UNNI ASSOCIATES",
    "PHILIPS", "VIKRITHI", "KANAKKANE", "NIZHAL", "BRO DADDY",
    "TWELFTH MAN", "MALAIKOTTAI VAALIBAN", "JANAKI V VERSUS STATE OF KERALA",
    "PADAKKALAM", "ALAPPUZHA GYMKHANA", "MARCO", "OFFICER ON DUTY"
]

word = random.choice(movies)

guess = ["_" if ch != " " else " " for ch in word]
attempts = 5

while attempts > 0 and "_" in guess:
    print("\nWord:", " ".join(guess))

    choice = input("Enter L for Letter or W for Whole Movie: ").upper()

    if choice == "L":
        letter = input("Enter a letter: ").upper()

        if letter in word:
            for i in range(len(word)):
                if word[i] == letter:
                    guess[i] = letter
        else:
            attempts -= 1
            print("Wrong Guess!")

    elif choice == "W":
        movie = input("Enter the movie name: ").upper()

        if movie == word:
            guess = list(word)
            break
        else:
            attempts -= 1
            print("Wrong Movie Name!")

    else:
        print("Invalid Choice!")

    print("Attempts Left:", attempts)

if "_" not in guess:
    print("\nCongratulations! You guessed:", word)
else:
    print("\nGame Over!")
    print("The movie was:", word)