import csv

firstline = True

def modnormalize(modname):
    modnormnames = dict({
                         'Alternate Terrain Generation [Http://Www.Minecraftforum.Net/Topic/1932156-16X-Atg-Alternate-Terrain-Generation/]':'Alternate Terrain Generation',
                         'A.E.':'Applied Energistics',
                         'Ae':'Applied Energistics',
                         'Ae1':'Applied Energistics',
                         'Applied Energestics':'Applied Energistics',
                         'Applied Enegistics':'Applied Energistics',
                         'Applied Energestic':'Applied Energistics',
                         'Applied Energetics':'Applied Energistics',
                         'Applied Energistic':'Applied Energistics',
                         'Applied Energistic (Or)':'Applied Energistics',
                         'Applied Energitics':'Applied Energistics',
                         'Appliedenergistics':'Applied Energistics',
                         'Applied Enegetics':'Applied Energistics',
                         'Applied Energistigs':'Applied Energistics',
                         'Applied Engestics':'Applied Energistics',
                         'Appliedenergetics':'Applied Energistics',
                         'App. Ener.':'Applied Energistics',
                         '3. Applied Energetics':'Applied Energistics',
                         'Advanced Solars':'Advanced Solar Panels',
                         'Advanced Solar':'Advanced Solar Panels',
                         'Advanced Solar Panel':'Advanced Solar Panels',
                         'Advsolarpanels':'Advanced Solar Panels',
                         'Archimede\'S Ships':'Archimedes Ships',
                         'Archimedes\' Ships':'Archimedes Ships',
                         'Archimedes Ship':'Archimedes Ships',
                         'Ars Magica':'Ars Magica 2',
                         'Ars Magicia':'Ars Magica 2',
                         'Ars Magicka':'Ars Magica 2',
                         'Ars Magika':'Ars Magica 2',
                         'Ars Magicka 2':'Ars Magica 2',
                         'Ars Magica Ii':'Ars Magica 2',
                         'Arsmagica':'Ars Magica 2',
                         'Arsmagica2':'Ars Magica 2',
                         'Arsmagicka':'Ars Magica 2',
                         'Balkons Weapon Mod':'Balkon\'S Weapons',
                         'Balkon\'S Weapon Mod':'Balkon\'S Weapons',
                         'Biblio Craft':'Bibliocraft',
                         'Bibilocraft':'Bibliocraft',
                         'Biblocraft':'Bibliocraft',
                         'Bibliocraft (Bop, Forestry, And Natura Addons)':'Bibliocraft',
                         'Bibliocraftwoods (Addons For Bop,Natura,Forestry Etc..)':'Bibliowoods',
                         'Binnies Mod':'Binnies Mods',
                         'Binnie\'S Mods (Extra Bees/Trees)':'Binnies Mods',
                         'Binnie\'S Mods':'Binnies Mods',
                         'Binnies Bees & Trees':'Binnies Mods',
                         'Binnie':'Binnies Mods',
                         'Binnie Mods (Extra Trees & Bees)':'Binnies Mods',
                         'Binnie\'S Extra Bees/Trees':'Binnies Mods',
                         'Bonnie\'S Mods':'Binnies Mods',
                         'Biomes O Penty':'Biomes O Plenty',
                         'Biomes \'O Plenty':'Biomes O Plenty',
                         'Biomes \'O\' Plenty':'Biomes O Plenty',
                         'Biomes O Pleanty':'Biomes O Plenty',
                         'Biomes O\' Plenty':'Biomes O Plenty',
                         'Biomes O\'Plenty':'Biomes O Plenty',
                         'Biomes-O-Plenty':'Biomes O Plenty',
                         'Biomes\'A\'Plenty':'Biomes O Plenty',
                         'Biomesoplenty':'Biomes O Plenty',
                         'Blenty O Biomes':'Biomes O Plenty',
                         'Bop':'Biomes O Plenty',
                         'Bop(Biomes O Plenty)':'Biomes O Plenty',
                         'Bo\'P':'Biomes O Plenty',
                         'Plenty O\' Biomes':'Biomes O Plenty',
                         'Biomes\'O Plenty':'Biomes O Plenty',
                         'Biomes\'O\'Plenty':'Biomes O Plenty',
                         'Bloodmagic':'Blood Magic',
                         'Bc':'Buildcraft',
                         'Bc3':'Buildcraft',
                         'Build Craft':'Buildcraft',
                         'Build Craft (Just Want Gates And Quarry)':'Buildcraft',
                         'Buildcraft 3':'Buildcraft',
                         'Build Craft (Latest)':'Buildcraft',
                         'Build Craft 3':'Buildcraft',
                         'Buildcraft 4':'Buildcraft',
                         'Buildcraft And Extras':'Buildcraft',
                         'Buildcraft,':'Buildcraft',
                         '2. Buildcraft':'Buildcraft',
                         'Carpenters':'Carpenter\'S Blocks',
                         'Carpenters Blocks':'Carpenter\'S Blocks',
                         'Carpentry Blocks':'Carpenter\'S Blocks',
                         'Carpenter Mod':'Carpenter\'S Blocks',
                         'Chickekchunks':'Chickenchunks',
                         'Chicken Chunks':'Chickenchunks',
                         '-Chickenchunks':'Chickenchunks',
                         'Cc':'Chickenchunks',
                         'Chickenchuncks':'Chickenchunks',
                         'Chickenchunks':'Chickenchunks',
                         'Chiesel':'Chisel',
                         'Compact Solars':'Compact Solar Panels',
                         'Computer Craft':'Computercraft',
                         'Compercraft (With Peripherals)':'Computercraft',
                         'Computercraft Must Have':'Computercraft',
                         'Damageindications':'Damage Indicators',
                         'Damageindicators':'Damage Indicators',
                         'Dart Craft':'Dartcraft',
                         'Dartcart':'Dartcraft',
                         'Dimensional Doorways':'Dimensional Doors',
                         '-Dyetrees':'Dyetrees',
                         'Enchanting+':'Enchanting Plus',
                         'Ee3 (Hopefully)':'Equivalent Exchange 3',
                         'Ee 3':'Equivalent Exchange 3',
                         'Ee1':'Equivalent Exchange 3',
                         'Ee2':'Equivalent Exchange 3',
                         'Ee3':'Equivalent Exchange 3',
                         'Ee3 When It\'S Fully Released':'Equivalent Exchange 3',
                         'Ee4':'Equivalent Exchange 3',
                         'Ee5':'Equivalent Exchange 3',
                         'Equivalant Exchange 3':'Equivalent Exchange 3',
                         'Equivelentexchange3':'Equivalent Exchange 3',
                         'Equivalent Exchange':'Equivalent Exchange 3',
                         'Enhanced Portals 3':'Enhanced Portals',
                         'Engineers Toolbox':'Engineer\'s Toolbox',
                         'Ender I/O':'Enderio',
                         'Ender Io':'Enderio',
                         'Ender Chests':'Ender Storage',
                         'Enderchest':'Ender Storage',
                         'Enderstorage':'Ender Storage',
                         '-Ender Storage':'Ender Storage',
                         '7. Ender Storage':'Ender Storage',
                         'Enderchests':'Ender Storage',
                         '-Enderforest':'Enderforest',
                         'Extra Cells Addon For Ae':'Extra Cells',
                         'Extra Cells (Ae Addon)':'Extra Cells',
                         'Extra Utils':'Extra Utilities',
                         'Extrautilies':'Extra Utilities',
                         'Extrautils':'Extra Utilities',
                         'Extra Utility\'S':'Extra Utilities',
                         'Extra Utlities':'Extra Utilities',
                         'Extra-Utils':'Extra Utilities',
                         'Extra. Utils':'Extra Utilities',
                         'Exstra Utl':'Extra Utilities',
                         'Extrautil':'Extra Utilities',
                         'Extra Utilities.':'Extra Utilities',
                         'Extrautilities':'Extra Utilities',
                         'Extra Bees/Trees':'Extra Bees',
                         'Extra Bees\Trees':'Extra Bees',
                         'Extrabees':'Extra Bees',
                         'Extratrees':'Extra Trees',
                         'Extrabiomes Xl':'Extrabiomesxl',
                         'Factorazation':'Factorization',
                         'Factorisation':'Factorization',
                         'Flan\'S Weapon Mod Or Balkon\'S Weapon Mod':'Weapon Mod',
                         'Flans Or Other Modern Weapon Mod':'Weapon Mod',
                         'Forestry (W/All The Bee Mods Xd)':'Forestry',
                         'Forestry    Beeeeeeeess!!':'Forestry',
                         'Forestry/Extra Bees':'Forestry',
                         'Foresty':'Forestry',
                         '6. Forestry':'Forestry',
                         'Forestry + Addons':'Forestry',
                         'Forestry --Bees':'Forestry',
                         'Forestry With Extra Bees/Trees And Magic Bees':'Forestry',
                         'Forge Multipart':'Forgemultipart',
                         'Forge Multiparts':'Forgemultipart',
                         '-Forgemultipart':'Forgemultipart',
                         'Galactic Craft':'Galacticraft',
                         'Galaticraft':'Galacticraft',
                         'Galacticcraft':'Galacticraft',
                         'Gascraft':'Gas Craft',
                         '-Geostrata':'Geostrata',
                         'Gravitation Suite':'Gravisuite',
                         'Gravitational Suite':'Gravisuite',
                         'Gravsuite':'Gravisuite',
                         'Gravisuit':'Gravisuite',
                         'Gravitationsuite':'Gravisuite',
                         'Gravi Suit':'Gravisuite',
                         'Greg Tech':'Gregtech',
                         'Gregtech (I Know, I\'M Sorry)':'Gregtech',
                         'Gregtech, Please, For The Love Of God':'Gregtech',
                         'Harvestcraft':'Harvest Craft',
                         'Hats Mod':'Hats',
                         'Pam\'S Harvest Craft':'Harvest Craft',
                         'Pam\'S Harvestcraft':'Harvest Craft',
                         'Pams Harvestcraft':'Harvest Craft',
                         'Industrial Craft 2 (3?)':'Industrial Craft',
                         'Industrialcraft (2?)':'Industrial Craft',
                         'Industrialcraft 2 (Experimental)':'Industrial Craft',
                         'Industrialcraft 2 Experimental':'Industrial Craft',
                         'Industrialcraft Ii':'Industrial Craft',
                         'Ic 2':'Industrial Craft',
                         'Ic 2.':'Industrial Craft',
                         'Ic2 + Addons':'Industrial Craft',
                         'Ic2/3':'Industrial Craft',
                         'Ic3':'Industrial Craft',
                         'Indusrialcraft':'Industrial Craft',
                         'Industrialcraft2':'Industrial Craft',
                         'Ic2':'Industrial Craft',
                         'Ic2 Exp.':'Industrial Craft',
                         'Ic2 Experimental':'Industrial Craft',
                         'Industrial Craft 2':'Industrial Craft',
                         'Industrial Craft 2Exp':'Industrial Craft',
                         'Industrialcraft':'Industrial Craft',
                         'Industrialcraft 2':'Industrial Craft',
                         '2. Industrialcraft':'Industrial Craft',
                         'Ic2-Experimental':'Industrial Craft',
                         'The New Ic2':'Industrial Craft',
                         'Ironchests':'Iron Chests',
                         'Inv Tweaks':'Inventory Tweaks',
                         'Inv. Tweaks':'Inventory Tweaks',
                         'Invent Tweaks':'Inventory Tweaks',
                         'Inventory Tweaks!!':'Inventory Tweaks',
                         'Inventorytweaks':'Inventory Tweaks',
                         'Involved Tweaks':'Inventory Tweaks',
                         'Invtweaks':'Inventory Tweaks',
                         'Invtweeks':'Inventory Tweaks',
                         '1. Inventory Tweaks':'Inventory Tweaks',
                         'Iron Chest':'Iron Chests',
                         'Ironchests (Or Similar)':'Iron Chests',
                         'Ironchest':'Iron Chests',
                         'Logistic Pipes':'Logistics Pipes',
                         'Magic Bees\'N\'Trees':'Magic Bees',
                         'Magicbees':'Magic Bees',
                         'Map Writer':'Mapwriter',
                         'Map Writer/Opis':'Mapwriter',
                         'Mechanism':'Mekanism',
                         'Metallurgy 3':'Metallurgy',
                         'Metalurgy':'Metallurgy',
                         'Mff...':'Modular Force Field Systems',
                         'Mffs':'Modular Force Field Systems',
                         'Mffs (Calclavia)':'Modular Force Field Systems',
                         'Mffs Calclavia':'Modular Force Field Systems',
                         'Mfr':'Mine Factory Reloaded',
                         'Microblocks':'Micro Blocks',
                         'Microblocks (Any Kind)':'Micro Blocks',
                         'Minefactory':'Mine Factory Reloaded',
                         'Minefactory Reloaded':'Mine Factory Reloaded',
                         'Minefactoryreloaded':'Mine Factory Reloaded',
                         'Minefactory Reload':'Mine Factory Reloaded',
                         'Misc Peripherals':'Miscperipherals',
                         'Miscpheriphals':'Miscperipherals',
                         'Mo\' Creatures Or Other Mob Mod':'Mo\' Creatures',
                         'Mo\' Creatures(Guessing Permission Issues Though)':'Mo\' Creatures',
                         'Mo\'Creatures':'Mo\' Creatures',
                         'Mo Animals':'Mo\' Creatures',
                         'Modular Force Feilds':'Modular Force Field Systems',
                         'Modular Forcefield Systems':'Modular Force Field Systems',
                         'Modular Power Suits':'Modular Powersuits',
                         'Modular Powersuit':'Modular Powersuits',
                         'Modular Powersuits,':'Modular Powersuits',
                         'Moduler Powersuits':'Modular Powersuits',
                         'Modular Power Suit':'Modular Powersuits',
                         'Modular Powersuit + Addons':'Modular Powersuits',
                         'Mmmps':'Modular Powersuits',
                         'Mmps (+ Addons)':'Modular Powersuits',
                         'Mps':'Modular Powersuits',
                         'Mps Power Suits':'Modular Powersuits',
                         'Modular Power Suites':'Modular Powersuits',
                         'Powersuits':'Modular Powersuits',
                         'Morph (With Op Bat Flight)':'Morph',
                         'Morph Mod':'Morph',
                         'Morpheous':'Morpheus',
                         'Mystcraft!':'Mystcraft',
                         'Mystcrat':'Mystcraft',
                         '8. Mystcraft':'Mystcraft',
                         'Myst Craft':'Mystcraft',
                         'Neather Ore':'Nether Ores',
                         'Netherores':'Nether Ores',
                         'Nei (Plugins+Addons)':'Nei',
                         '-Nei':'Nei',
                         'Nei Addon':'Nei Addons',
                         '--Nei Addons':'Nei Addons',
                         'Neiaddons':'Nei Addons',
                         'Nei Plugin':'Nei Plugins',
                         'Neiplugins':'Nei Plugins',
                         '--Nei Plugins':'Nei Plugins',
                         'Nie':'Nei',
                         'Not Enough Items':'Nei',
                         'Notenoughitems':'Nei',
                         '1. Not Enough Items':'Nei',
                         'Nei :P':'Nei',
                         '10. Ic2Nuclearcontrol':'Nuclear Control',
                         'Adv Nuclear Control (Ic2 Addon)':'Nuclear Control',
                         'Ic2 Nuclear Control':'Nuclear Control',
                         'Nuclear Reactor Control':'Nuclear Control',
                         'Nuclearcontrol':'Nuclear Control',
                         'Obisidan Plates':'Obsidiplates',
                         'Obsidi Plates':'Obsidiplates',
                         'Obsidian Plates':'Obsidiplates',
                         'Obsidian Pressure Plates':'Obsidiplates',
                         'Open Blocks!':'Openblocks',
                         'Open Blocks':'Openblocks',
                         'Openperipheral':'Openperipherals',
                         'Open Peripherals':'Openperipherals',
                         'Open Peripheral':'Openperipherals',
                         'Open Peripherals/Misc Peripherals':'Openperipherals',
                         'Optifine    Doesn\'T Have To Be Installed Just Compatable':'Optifine',
                         'Portal Guns':'Portal Gun',
                         'Portalgun':'Portal Gun',
                         'Portal And Gravity Guns':'Portal Gun',
                         'Powerconverters':'Power Converters',
                         'Project: Red':'Project Red',
                         'Project:Red':'Project Red',
                         'Projectred':'Project Red',
                         'Project Red Power':'Project Red',
                         '9. Project Red':'Project Red',
                         'Project-Red':'Project Red',
                         'Q Craft':'Qcraft',
                         'Quarries+':'Quarry Plus',
                         'Quarryplus':'Quarry Plus',
                         'Rail Craft':'Railcraft',
                         '4. Railcraft':'Railcraft',
                         'Reactorcraft':'Reactor Craft',
                         'Reactor Craft (If Rotarycraft Is Added)':'Reactor Craft',
                         'Redpower2':'Red Power',
                         'Redpower :(':'Red Power',
                         'Redpower':'Red Power',
                         'Red Power Replacement':'Red Power',
                         'Red Power 2':'Red Power',
                         'Redpower 2':'Red Power',
                         'Remote Io':'Remoteio',
                         'Reseonent Induction':'Resonant Induction',
                         'Rotary Craft':'Rotarycraft',
                         'Rotorycraft':'Rotarycraft',
                         '-Rotary Craft':'Rotarycraft',
                         'Soul Shard':'Soul Shards',
                         'Soul Shards 1':'Soul Shards',
                         'Soul Shards 2':'Soul Shards',
                         'Soulshards 2':'Soul Shards',
                         'Soulshards':'Soul Shards',
                         '-Spiderpet':'Spiderpet',
                         'Steve\'S Cart':'Steve\'S Carts',
                         'Stevecarts':'Steve\'S Carts',
                         'Stevescarts':'Steve\'S Carts',
                         'Steve\'S Carts 2':'Steve\'S Carts',
                         'Stevecart':'Steve\'S Carts',
                         'Steves Carts':'Steve\'S Carts',
                         'Steves Carts 2':'Steve\'S Carts',
                         'Tc4':'Thaumcraft',
                         'Thaumcraft 4':'Thaumcraft',
                         'Thaumcraft 4,':'Thaumcraft',
                         'Thaumcraft4':'Thaumcraft',
                         '5. Thaumcraft':'Thaumcraft',
                         'Thaumic Tinkererer':'Thaumic Tinkerer',
                         'Te3':'Thermal Expansion',
                         'Te':'Thermal Expansion',
                         'Te3,':'Thermal Expansion',
                         'Tf4':'Thermal Expansion',
                         'Thermal Expansion 3':'Thermal Expansion',
                         'Thermal Exspasnion':'Thermal Expansion',
                         'Thermalexpansion':'Thermal Expansion',
                         'Thermal Exp':'Thermal Expansion',
                         'Thermal Expansion 4':'Thermal Expansion',
                         'Thermal Expantion':'Thermal Expansion',
                         'Thermal Expension':'Thermal Expansion',
                         '2. Thermal Expansion':'Thermal Expansion',
                         'Cofh (+ Anything Related)':'Thermal Expansion',
                         'Themalexpansion':'Thermal Expansion',
                         'Thermal Expansio':'Thermal Expansion',
                         'Thuamcraft':'Thaumcraft',
                         'Thaumcraf':'Thaumcraft',
                         'Thaumcraft + Addons':'Thaumcraft',
                         'Thaumcraft 3':'Thaumcraft',
                         'Thuaumcraft 4':'Thaumcraft',
                         'Thaumcraft Or Similar':'Thaumcraft',
                         'Thaumcraft 4 + Thaumic Tinkerer (!!!)':'Thaumcraft',
                         'Thaumic Tinker':'Thaumic Tinkerer',
                         'Thaumictinkerer':'Thaumic Tinkerer',
                         'Tc':'Tinker\'S Construct',
                         'Tconstruct':'Tinker\'S Construct',
                         'Tinkerer\'S Construct':'Tinker\'S Construct',
                         'Tinkers Construct':'Tinker\'S Construct',
                         'Tinkers Constuct':'Tinker\'S Construct',
                         'Tinkers Contract':'Tinker\'S Construct',
                         'Tinkers\' Construct':'Tinker\'S Construct',
                         'Tic':'Tinker\'S Construct',
                         'Tico':'Tinker\'S Construct',
                         'Tinker\'S Constructs':'Tinker\'S Construct',
                         'Tinkerer\'S Constuct':'Tinker\'S Construct',
                         'Tinkerers Construct':'Tinker\'S Construct',
                         'Tinkers Construct,':'Tinker\'S Construct',
                         'Tinkers Constructs':'Tinker\'S Construct',
                         'Tinkers\'S Construct':'Tinker\'S Construct',
                         'Tinkersconstruct':'Tinker\'S Construct',
                         'Tinker\'Sconstruct':'Tinker\'S Construct',
                         'Tinkers Construct+Addons':'Tinker\'S Construct',
                         'Tinkerer':'Tinker\'S Construct',
                         'Tinkers Mechwork':'Tinker\'S Mechworks',
                         'Tinker\'S Construct: Mechworks':'Tinker\'S Mechworks',
                         'Tic Mech':'Tinker\'S Mechworks',
                         'Tinkers Mechworks':'Tinker\'S Mechworks',
                         'Trailmix Mod':'Trail Mix',
                         'Translocator':'Translocators',
                         'Translocatot':'Translocators',
                         'Trecapitator':'Treecapitator',
                         'Treecapitate':'Treecapitator',
                         'Tropicraft (Probably Not Possible Tho ):)':'Tropicraft',
                         'Twighlight Forest':'Twilight Forest',
                         'Twilight':'Twilight Forest',
                         'Twilight Forest Or Something With More Challenges':'Twilight Forest',
                         'Twilight Mod':'Twilight Forest',
                         'Undergroundbiomes':'Underground Biomes',
                         'Waila Nei Extension':'Waila',
                         'Walia':'Waila',
                         'Wrcbe':'Wr-Cbe',
                         'Wireless Redstone Cbe':'Wr-Cbe',
                         'Wirelessredstone':'Wr-Cbe',
                         'Wr Cbe':'Wr-Cbe',
                         'Xact Crafting Table':'Xact',
                         'Xenos Relinquary':'Xeno\'S Reliquary',
                         'Xeno\'S Requilary':'Xeno\'S Reliquary',
                         'Xenos Reliquary':'Xeno\'S Reliquary',
                         'Zans/Voxel Minimap':'Zan\'S Minimap',
                         'Voxelmap (Zan\'S)':'Zan\'S Minimap',
                         'Voxelmod (Or Equally Good Minimap)':'Zan\'S Minimap',
                         })
    if modname in modnormnames:
        print("Replacing: "+modname+" with "+modnormnames[modname])
        return modnormnames[modname]
    else:
        return modname
    
with open('Poll 1 Form Responses.csv') as csvfile:
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
            reqmod = modnormalize(reqmod.strip().lower().title())
            if len(reqmod)>0:
                if reqmod in counts['reqmods']:
                    counts['reqmods'][reqmod] += 1
                else:
                    counts['reqmods'][reqmod] = 1
            
        nicemods = row[8]
        nicemodslist = nicemods.splitlines()
        for nicemod in nicemodslist:
            nicemod = modnormalize(reqmod.strip().lower().title())
            if len(nicemod)>0:
                if nicemod in counts['nicemods']:
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
    #if key1 == 'reqmods' or key1 == 'nicemods':
        #Sort by key
        #for key2 in sorted(counts[key1]):
        #    print("  "+key2+"\t"+str(counts[key1][key2]))
        #    f.write("\""+key2+"\","+str(counts[key1][key2])+"\n")
    #else:
        #This sorts by the number of occurances for each key
    for key2 in sorted(counts[key1], key=counts[key1].get, reverse=True):
        print(key2 + "\t" + str(counts[key1][key2]))
        f.write("\""+key2+"\","+str(counts[key1][key2])+"\n")
    print("\n\n")