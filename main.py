import random

print("+-----------------------------------------+")
print("| Selamat datang pada Tebak tebakan angka |")
print("+-----------------------------------------+")

top_of_range = input("Ketik berapa angka: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Tolong masukkan angka yang lebih dari 0")
        quit()

else :
    print("Tolong masukkan angka!")
    quit()

random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guesses = input("Coba tebak: ")
    if user_guesses.isdigit():
        user_guesses = int(user_guesses)
    else :
        print("Tolong masukkan angka!")
        quit()
    
    if user_guesses == random_number:
        print("Selamat tebakan kamu benar")
        break
    elif user_guesses > random_number:
        print("Maaf tebakan kamu berada di atas angka! ")
    else:
        print("Maaf tebakan kamu di bawah angka! ")

print("Selamat kamu berhasil menebak pada tebakan ke", guesses, "tebakan")
