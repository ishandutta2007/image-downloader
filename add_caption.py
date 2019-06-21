#coding=utf-8

import xlrd,os,random
tags = "#fashion #fashionblogger #fashionista #fashionable #fashionstyle #fashionblog #fashiongram #FashionAddict #fashionweek #fashiondiaries #fashionpost #fashionphotography #FashionDesigner #fashionlover #fashionshow #fashionmodel #fashiondesign #fashionkids #fashiondaily #fashionstylist #fashiongirl #fashionjewelry #fashioninspo #fashionillustration #fashions #fashioninsta #fashionart #fashionmen #fashionphotographer #fashionbloggers #style #styles #styleblogger #styleinspiration #styleblog #styleoftheday #stylegram #styleinspo #stylediaries #styled #styleformen #styleguide #styleartists #styleaddict #stylebloggers #styleiswhat #styleicon #stylemen #stylelife #stylemepretty #stylediary #stylefashion #stylefile #styledbyme #styletips #StyleGoals #stylenanda #styledshoot #styleseat #styleinfluencer #luxury #luxurylife #luxurylifestyle #luxurycars #luxuryhomes #luxuryliving #luxurytravel #luxurystyle #luxuryrealestate #luxurycar #luxuryhome #luxuryfashion #luxurydesign #luxurywatch #luxuryhotel #luxurybrand #luxury4play #luxurywedding #LuxuryHouse #luxurywatches #luxuryinteriors #luxuryworldtraveler #luxurybag #luxurygoods #luxuryhotels #luxuryfurniture #luxuryshoes #luxuryjewelry #luxurylifestylemagazine #luxurylistings #clothing #clothingline #clothingbrand #CLOTHINGSTORE #clothingcompany #clothingdesigner #clothingbandung #clothinglabel #ClothingLines #clothingdesign #clothingforcarpeople #clothingboutique #clothings #clothingindonesia #clothingforsale #clothingbrands #clothingsale #clothingco #clothingshop #clothingph #clothingbali #ClothingStores #clothingapparel #clothingoptional #clothingjakarta #clothingonline #clothingan #clothingmodel #clothingmaker #clothingstyle #woman #womanstyle #womanpower #womanfashion #womancrushwednesday #womans #womancrush #womansfashion #womanswear #womanentrepreneur #womanofgod #womaninbusiness #womanempowerment #womanowned #womanpreneur #womanportrait #womanhood #womanslook #womanshoes #womanwear #Womanism #womantattoo #womancrusheveryday #womansRights #Womanist #womansbestfriend #womanboss #womanshealth #womaninbiz #WomanOwnedBusiness #vogue #VogueMagazine #vogueitalia #vogueparis #vogueliving #vogueRussia #voguebrasil #VogueIndia #voguearabia #vogueuk #voguejapan #voguestyle #VogueSpain #vogueitaly #voguekids #voguethreads #vogueaustralia #voguemodel #voguefollow #voguetalents #voguenails #voguechina #voguehommes #voguekorea #voguemexico #voguefashion #vogueusa #voguerunway #VogueMen #vogueclips #art #artist #artwork #arte #artoftheday #artistic #artsy #artofvisuals #artistsoninstagram #arts #artgallery #artists #artistsofinstagram #artlife #artlovers #artstagram #artista #artisan #artistoninstagram #artworks #artshow #artcollector #artforsale #artshub #artlover #artofinstagram #artphotography #Artstudio #artcollective #artdeco #makeup #makeupartist #makeupaddict #makeuplover #makeupjunkie #makeuptutorial #makeupforever #makeupbyme #makeupoftheday #makeuplook #makeupart #makeupblogger #makeuplove #makeupartistsworldwide #makeupgeek #makeupmafia #makeupvideo #makeuplovers #makeupvideos #makeupblog #makeupartistworldwide #makeupgoals #Makeupdolls #makeupporn #makeuplife #makeupgirl #makeupobsessed #makeuptalk #makeupph #makeupmurah"

def write_txt():
    global tags
    workbook = xlrd.open_workbook("C://Users//wu//Downloads//quotes.xlsx")
    sheet = workbook.sheet_by_index(0)

    quote_list = []
    for rowx in range(sheet.nrows):
        cols = sheet.row_values(rowx)
        quote =  cols[0]
        quote_list.append(quote)
    tag_list = tags.split(" ")
    tags = random.sample(tag_list, 10)

    print len(quote_list)
    count = 0
    for path, directories, files in os.walk('F://instagram//instagram-scraper'):

        for index,name in enumerate(files):
            if name.lower().endswith("mp4"):
                print os.path.join(path, os.path.splitext(name)[0]+".txt")
                f = open(os.path.join(path, os.path.splitext(name)[0]+".txt"),"w")
                caption = random.choice(quote_list)
                content = " ".join(tags) + " #ootd #ootdshare"
                full_content =  caption +" " + content
                f.write(full_content.encode('utf-8'))
                f.close()

if __name__ == "__main__":
    write_txt()