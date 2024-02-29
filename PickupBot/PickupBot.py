#seed = 0x191F
#pickupMons = 1

def rngAdvance(prev):
    rng = ((prev * 0x41c64e6d) + 0x6073) 
    return rng % 0x100000000

def findPickupItem(item):
    if(item <= 29):
            return("Super Potion")
    elif(item >= 30 and item <= 39):
            return("Full Heal")
    elif(item >= 40 and item <= 49):
            return("Ultra Ball")
    elif(item >= 50 and item <= 59):
            return("Rare Candy")
    elif(item >= 60 and item <= 69):
            return("Full Restore")
    elif(item >= 70 and item <= 79):
            return("Revive")
    elif(item >= 80 and item <= 89):
            return("Nugget")
    elif(item >= 90 and item <= 94):
            return("Protein")
    elif(item >= 95 and item <= 98):
            return("PP Up")
    elif(item == 99):
            return("King's Rock")

def findPickupItemFRLG(item):
    if(item <= 14):
        return("Oran Berry")
    elif(item >= 15 and item <= 24):
        return("Cheri Berry")
    elif(item >= 25 and item <= 34):
        return("Chesto Berry")
    elif(item >= 35 and item <= 44):
        return("Pecha Berry")
    elif(item >= 45 and item <= 54):
        return("Rawst Berry")
    elif(item >= 55 and item <= 64):
        return("Aspear Berry")
    elif(item >= 65 and item <= 74):
        return("Persim Berry")
    elif(item >= 75 and item <= 79):
        return("TM 10")
    elif(item >= 80 and item <= 84):
        return("PP Up")
    elif(item >= 85 and item <= 89):
        return("Rare Candy")
    elif(item >= 90 and item <= 94):
        return("Nugget")
    elif(item == 95):
        return("Spelon Berry")
    elif(item == 96):
        return("Pamtre Berry")
    elif(item == 97):
        return("Watmel Berry")
    elif(item == 98):
        return("Durin Berry")
    else:
        return("Belue Berry")
while(True):
    temp = int(input("Enter Seed (in Integer NOT hexidecimal): " ))
    pickupMons = int(input("Enter Number of Zigzagoons: " ))
    frameRange = int(input("Enter Frame Range: "))
    for i in range(0, frameRange):
        itemList = ""
        temp = rngAdvance(temp)
        temp1 = temp
        #print(hex(temp >> 16))
    
        temp1 = rngAdvance(temp1)
        temp1 = rngAdvance(temp1)
        temp1 = rngAdvance(temp1)
        iv1 = temp1 >> 16
        goodItems = 0
        if((iv1 % 10) == 0):
            temp1 = rngAdvance(temp1)
            iv2 = temp1 >> 16
            item = iv2 % 100
            itemList = "Pickup Mon 1" + ": " + str(findPickupItem(iv2 % 100)) + " | "
        for j in range(0, pickupMons - 1):
            temp1 = rngAdvance(temp1)
            iv3= temp1 >> 16
            if(iv3 % 10 == 0):
                temp1 = rngAdvance(temp1)
                iv4 = temp1 >> 16
                item = iv4 % 100
                itemList = itemList + "Pickup Mon " + str(j + 2) + " : " + str(findPickupItem(iv4 % 100)) + " | "
            
            if(itemList != ""):
                print("Frame: " + str(i) + " " + itemList) #
                
    
        
    
