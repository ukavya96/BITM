from atm import Kavya,Pinky,Bhavana

def main():
    kavya = Kavya(8792213683,"Union bank",5623)
    pinky = Pinky(9866512435, "SBI bank", 6644)
    bhavana = Bhavana(9465534753,"Axis bank", 9632)
    
    kavya.display_details()
    print("\n")
    pinky.display_details()
    print("\n")
    bhavana.display_details()
    
if __name__ == "__main__":
    main()