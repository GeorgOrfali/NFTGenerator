import random
from PIL import Image

#Initialize the array for propability
# 1 = Karpfen 75%, 2 = Lachs 25%
type = []
# 1 = Verdreckter tiefsee boden 50%, 2 = Meer 25%, 3 = Steinmeer boden 15%, 4 = Korallenriff 10%
background = []
# 1 = Normal 50%, 2 = Glitzern 35%, 3 = Neon 14%, 4 = Gold 1%
scale = []
# 1 = none 50%, 2 = free 25%, 3 = help 25%
branding = []
# 1 = none 40$ , 2 = all 60%
injury = []
# 1 = plastic = 15%, 2 = paper 15%, 3 = none 60%, 3 = zigarette 10%
mouth = []
# 1 = none = 50%, 2 = dose 25%, 3 = angelrute 24%, 4 = Krone 1%
hat = []

#add the data to array
def add_properties(array,value,num):
    for i in range(num):
        array.append(value)

#add the properties for type array
add_properties(type,'karpfen',1)
add_properties(type,'lachs',1)

#add the properties for background array
add_properties(background,'verdreckt',1)
add_properties(background,'meer',1)
add_properties(background,'stein',1)
add_properties(background,'korallen',1)

#add the properties for scale array
add_properties(scale,'normal',50)
add_properties(scale,'glitzern',35)
add_properties(scale,'neon',14)
add_properties(scale,'gold',1)

#add the properties for branding array
add_properties(branding,'none branding',50)
add_properties(branding,'free',25)
add_properties(branding,'help',25)

#add the properties for injury array
add_properties(injury,'all',60)
add_properties(injury,'none',40)

#add the properties for mouth array
add_properties(mouth,'none mouth',60)
add_properties(mouth,'plastic',15)
add_properties(mouth,'papier',15)
add_properties(mouth,'zigarette',10)

#add the properties for hat array
add_properties(hat,'none hat',50)
add_properties(hat,'dose',25)
add_properties(hat,'angelrute',24)
add_properties(hat,'krone',1)

#shuffle the array for randomizing

#random.shuffle(type)
#random.shuffle(background)
#random.shuffle(scale)
#random.shuffle(branding)
#random.shuffle(injury)
#random.shuffle(mouth)
#random.shuffle(hat)

#we need to pre generate the nft to also check if its unique
nft = []
allnfts = []

#nft index, 1 = background, 2 = type, 3 = scale, 4 = injury, 5 = branding, 6 = mouth, 7 = hat
#allnfts index, 1 = nft, 2 = nft ...
backgroundID = 0
typeID = 0
scaleID = 0
brandingID = 0
injuryID = 0
mouthID = 0
hatID = 0
#gesamt 3027
anzahl = {'verdreckt':1013,'meer':855,'stein':704,'korallen':454,'karpfen':1967,'lachs':1059}
counter = {'verdreckt': 0,'meer': 0,'stein':0,'korallen':0,'karpfen':0,'lachs':0}
for i in range(8):
    zwischenBG = backgroundID + 1
    if(zwischenBG <= len(background)):
        if(counter[background[backgroundID]] <= anzahl[background[backgroundID]] and
           counter[type[typeID]] <= anzahl[type[typeID]]):
            nft.append(background[backgroundID])
            counter[background[backgroundID]] = counter[background[backgroundID]] + 1
            nft.append(type[typeID])
            counter[type[typeID]] = counter[type[typeID]] + 1
            nft.append(scale[scaleID])
            nft.append(branding[brandingID])
            nft.append(injury[injuryID])
            nft.append(mouth[mouthID])
            nft.append(hat[hatID])
            backgroundID = backgroundID + 1
    else:
        backgroundID = 0
        typeID = typeID + 1
        zwischenType = typeID + 1
        if (zwischenType <= len(type)):
            if (counter[background[backgroundID]] <= anzahl[background[backgroundID]] and
                    counter[type[typeID]] <= anzahl[type[typeID]]):
                nft.append(background[backgroundID])
                counter[background[backgroundID]] = counter[background[backgroundID]] + 1
                backgroundID = backgroundID + 1
                nft.append(type[typeID])
                counter[type[typeID]] = counter[type[typeID]] + 1
                nft.append(scale[scaleID])
                nft.append(branding[brandingID])
                nft.append(injury[injuryID])
                nft.append(mouth[mouthID])
                nft.append(hat[hatID])
        else:
            typeID = 0
    if(nft != []):
        allnfts.append(nft)
    nft = []

print(allnfts)
print(counter)
bildverweis = {'meer':'res/background/meer.png','lachs':'res/type/lachs_normal.png','plastic_bag':'res/mouth/plastic.png','can':'res/hat/dose.png'}
def nft_generieren(nft,index):
    backgroundNFT = Image.open(bildverweis[nft[0]])
    typeNFT = Image.open(bildverweis[nft[1]])
    if(nft[5] != 'none_mouth'):
        mouthNFT = Image.open(bildverweis[nft[5]])
        typeNFT.paste(mouthNFT, (0, 0), mouthNFT)
    if(nft[6] != 'none_hat'):
        hatNFT = Image.open(bildverweis[nft[6]])
        typeNFT.paste(hatNFT, (0,0), hatNFT)
    backgroundNFT.paste(typeNFT , (0,0), typeNFT)
    backgroundNFT.save('generieren/'+str(index)+'.png')
allnftTest = [['meer','lachs','normal','none_branding','none_injury','none_mouth','none_hat'],['meer','lachs','normal','none_branding','none_injury','none_mouth','can'],['meer','lachs','normal','none_branding','none_injury','plastic_bag','none_hat'],['meer','lachs','normal','none_branding','none_injury','plastic_bag','can']]
for i in range(len(allnftTest)):
    nft_generieren(allnftTest[i],i)
