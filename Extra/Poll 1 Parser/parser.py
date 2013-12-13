import csv

firstline = True
with open('Form Responses.csv') as csvfile:
    fp = csv.reader(csvfile, delimiter=',')
    next(fp) #Skip the first line with header information
    counts = dict({
                  'name':dict(),
                  'gregtech':dict(),
                  'difficulty':dict(),
                  'rotarycraft':dict(),
                  'dartcraft':dict(),
                  'minimap':dict(),
                  'reqmods':dict(),
                  'nicemods':dict(),
                  'ore':dict(),
                  'gregtechdiff':dict(),
                  'packtype':dict()
                  })
    for row in fp:
        date = row[0]
        name = row[1].strip()
        print(row)
        if(len(name)>0):
            if name in counts['name']:
                counts['name'][name] += 1
            else:
                counts['name'][name] = 1
            
        gregtech = row[2].strip()
        if(len(gregtech)>0):
            if gregtech in counts['gregtech']:
                counts['gregtech'][gregtech] += 1
            else:
                counts['gregtech'][gregtech] = 1
            
        difficulty = row[3].strip()
        if(len(difficulty)>0):
            if difficulty in counts['difficulty']:
                counts['difficulty'][difficulty] += 1
            else:
                counts['difficulty'][difficulty] = 1
            
        rotarycraft = row[4].strip()
        if(len(rotarycraft)>0):
            if rotarycraft in counts['rotarycraft']:
                counts['rotarycraft'][rotarycraft] += 1
            else:
                counts['rotarycraft'][rotarycraft] = 1
            
        dartcraft = row[5].strip()
        if(len(dartcraft)>0):
            if dartcraft in counts['dartcraft']:
                counts['dartcraft'][dartcraft] += 1
            else:
                counts['dartcraft'][dartcraft] = 1
            
        minimap = row[6].strip()
        if(len(minimap)>0):
            if minimap in counts['minimap']:
                counts['minimap'][minimap] += 1
            else:
                counts['minimap'][minimap] = 1
            
        reqmods = row[7]
        reqmodslist = reqmods.splitlines()
        for reqmod in reqmodslist:
            reqmod = reqmod.strip().lower().title()
            if len(reqmod)>0:
                if reqmods in counts['reqmods']:
                    counts['reqmods'][reqmod] += 1
                else:
                    counts['reqmods'][reqmod] = 1
            
        nicemods = row[8]
        nicemodslist = nicemods.splitlines()
        for nicemod in nicemodslist:
            nicemod = nicemod.strip().lower().title()
            if len(nicemod)>0:
                if nicemods in counts['nicemods']:
                    counts['nicemods'][nicemod] += 1
                else:
                    counts['nicemods'][nicemod] = 1

        ore = row[10].strip()
        if(len(ore)>0):
            if ore in counts['ore']:
                counts['ore'][ore] += 1
            else:
                counts['ore'][ore] = 1
            
        gregtechdiff = row[11].strip()
        if(len(gregtechdiff)>0):
            if gregtechdiff in counts['gregtechdiff']:
                counts['gregtechdiff'][gregtechdiff] += 1
            else:
                counts['gregtechdiff'][gregtechdiff] = 1
            
        packtype = row[12].strip()
        if(len(packtype)>0):
            if packtype in counts['packtype']:
                counts['packtype'][packtype] += 1
            else:
                counts['packtype'][packtype] = 1
    

for key1 in iter(counts):
    print(key1)
    f = open('responses_'+key1+'.csv','w')
    if key1 == 'reqmods' or key1 == 'nicemods':
        for key2 in sorted(counts[key1]):
            print("  "+key2+"\t"+str(counts[key1][key2]))
            f.write(key2+"\t"+str(counts[key1][key2])+"\n")
    else:
        #This sorts by the number of occurances for each key
        for key2 in sorted(counts[key1], key=counts[key1].get, reverse=True):
            print(key2 + "\t" + str(counts[key1][key2]))
            f.write(key2+"\t"+str(counts[key1][key2])+"\n")
    print("\n\n")