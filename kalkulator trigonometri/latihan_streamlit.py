import math

def menu():
    print("Kalkulator Trigonometri")
    print("1. Sinus (sin)")
    print("2. Kosinus (cos)")
    print("3. Tangen (tan)")
    print("4. Cotangen (cot)")
    print("5. Secan (sec)")
    print("6. Cosecan (csc)")
    print("7. Keluar")

def trigonometri():
    while True:
        menu()
        choice = input("Pilih fungsi trigonometri (1/2/3/4/5/6/7): ")

        if choice == '7':
            print("Terima kasih telah menggunakan kalkulator trigonometri!")
            break
        
        angle = float(input("Masukkan sudut dalam derajat: "))
        angle_rad = math.radians(angle)  # Mengonversi sudut derajat ke radian

        if choice == '1':
            print(f"sin({angle}) = {math.sin(angle_rad)}")
        elif choice == '2':
            print(f"cos({angle}) = {math.cos(angle_rad)}")
        elif choice == '3':
            print(f"tan({angle}) = {math.tan(angle_rad)}")
        elif choice == '4':
            if math.tan(angle_rad) != 0:
                print(f"cot({angle}) = {1 / math.tan(angle_rad)}")
            else:
                print("Error: Tangen dari sudut ini adalah 0, cotangen tidak terdefinisi.")
        elif choice == '5':
            if math.cos(angle_rad) != 0:
                print(f"sec({angle}) = {1 / math.cos(angle_rad)}")
            else:
                print("Error: Kosinus dari sudut ini adalah 0, secan tidak terdefinisi.")
        elif choice == '6':
            if math.sin(angle_rad) != 0:
                print(f"csc({angle}) = {1 / math.sin(angle_rad)}")
            else:
                print("Error: Sinus dari sudut ini adalah 0, cosecan tidak terdefinisi.")
        else:
            print("Pilihan tidak valid. Coba lagi.")

if __name__ == "__main__":
    trigonometri()
