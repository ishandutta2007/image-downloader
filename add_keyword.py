#codingutf-8

def write_to_file(name,content):
    f = open('C:\Users\wu\Desktop\instagram\%s' % name,'w')
    content_lines = "\n".join(content.split("#")).strip()
    f.write(content_lines)
    f.close()
    
if __name__ ==  "__main__":
    #name = "animal_hashtag.txt"
    #content = "#animals #nature #animal #love #pets #wildlife #cute #photography #pet #photooftheday #art #animallovers #dog #cat #beautiful #dogs #wild #zoo #instagram #bird #naturephotography #instagood #cats #macro #ig #animalphotography #picoftheday #naturelovers #like"
    #name = "night_hashtag.txt"
    #content = "#night #photography #love #like #beautiful #light #instagood #picoftheday #party #nature #travel #sky #photooftheday #art #instagram #nightphotography #city #photo #black #follow #blackandwhite #music #red #followme #girl #sunset #day #sun #goodnight"
    #name = "black_and_white_hashtag.txt"
    #content = "#blackandwhite #bnw #art #inktober #drawing #blackandwhitephotography #photography #bw #ink #sketch #instagood #artist #illustration #portrait #black #love #monochrome #photooftheday #instagram #instaart #street #painting #photo #universe #artoftheday #draw #bear #streetphotography #blancoynegro"
    peopel_name = "people_hashtag.txt"
    people_content = "#people #life #love #photography #portrait #street #streetphotography #photo #instagood #art #nature #travel #city #instagram #bnw #happy #fun #summer #friends #blackandwhite #beautiful #black #girl #smile #food #photooftheday #music #fashion #photographer"

    cel_name = "celebrities.txt"
    cel_content = "#celebrities #celebrity #hollywood #fashion #follow #shoes #beauty #shopping #bollywood #accessories #style #instagram #love #music #entertainment #bags #model #actor #news #tv #followforfollowback #like #models #actress #celeb #indian #photography #sale #celebritynews"

    per_arts_name = "performing_arts.txt"
    per_arts_content = "#performingarts #theatre #dance #art #acting #performance #actor #music #drama #musicaltheatre #stage #performing #theater #musical #performer #dancer #theatrelife #singing #artist #arts #director #performanceart #actress #dancing #studio #dramaschool #actors #singer #instagood"


    city_arch_name = "city_arch.txt"
    city_arch_content = "#cityarchitecture #architecture #city #beautiful #bestoftheday #optimism #modernistarchitecture #awesome #mk #love #minimal #instafollow #architectureofoptimism #museum #thebeginning #kaunas #citycenter #howitisdone #photooftheday #modernism #lithuania #citycreation #lovely #bekind #beloving #behappy #lithuanian #loveyourself"

    sport_name = "sport.txt"
    sport_content ="#sport #fitness #motivation #gym #fit #love #training #workout #sports #bodybuilding #like #fitnessmotivation #nike #healthy #football #follow #instagood #muscle #fun #soccer #l #fight #mma #strong #sportlife #dance #personaltrainer #body #fashion"

    commercial_name = "commercial.txt"
    commercial_content = "#commercial #residential #model #photography #realestate #fashion #photoshoot #homedecor #interiordesign #interior #architecture #video #dubai #film #production #luxury #facade #kuwait #director #home #advertising #uae #privatevilla #saudiarabia #structure #architectural #decor #villa #structural"

    still_life_name = "still_life.txt"
    still_lift_content = "#stilllife #art #photography #painting #photographer #stilllifephotography #productphotography #artist #commercialphotography #d #foodphotography #design #flowers #contemporaryart #c #photo #autumn #photooftheday #lifestyle #instagood #drawing #fashion #still #creative #photoshop #flatlay #vintage #productdesign #nature"
    concert_name = "concert.txt"
    concert_content = "#concert #music #livemusic #singer #live #love #concertphotography #musician #photography #guitar #nyc #jazz #metal #rock #performance #dance #concertphoto #band #pop #rocknroll #art #songwriter #party #show #blues #nightlife #friends #concertphotographer #festival"
    street_name = "street.txt"
    street_content = "#street #photography #streetphotography #streetstyle #city #style #photo #art #like #fashion #instagood #travel #urban #love #streetart #spb #sky #follow #architecture #life #instagram #beautiful #graffiti #photographer #photooftheday #e #ig #picoftheday #vsco #bhfyp"

    family_name = "family.txt"
    family_content = "#family #love #friends #photography #happy #instagood #life #mobilestudioarchitects #like #music #model #kitchen #art #design #food #summer #photooftheday #london #live #young #fun #education #dream #bogota #pasion #siempre #engagement #space #galerias"
    transportation_name ="transportation.txt"
    transportation_content = "#transportation #transport #travel #car #bus #train #art #trucks #cars #business #railroad #truck #auto #road #love #city #cargo #technology #scooter #trains #buses #logistics #urban #losangeles #food #photo #fitness #tv #california"

    fashion_name = "fashion.txt"
    fashion_content = "#fashion #style #love #instagood #photography #model #fashionista #fashionable #photooftheday #picoftheday #ootd #fashionblogger #shopping #beauty #instafashion #instastyle #portrait #like #moda #luxury #tshirt #dress #makeup #luxurybrand #streetstyle #outfit #video #beautiful #women #bhfyp"

    film_name = "film.txt"
    film_content = "#film #movie #cinema #filmphotography #mm #movies #love #photography #s #actor #cinematography #filmisnotdead #films #filmmaking #blackandwhite #analog #like #analogphotography #action #art #picoftheday #street #vsco #portrait #life #horror #filmfeed #photo #fuji #bhfyp"

    underwater_name = "underwater.txt"
    underwater_content = "#underwater #underwaterphotography #diving #sea #nature #ocean #scubadiving #scuba #fish #photography #dive #underwaterworld #travel #uwphotography #water #underwaterphoto #gopro #underwaterlife #freediving #coral #sealife #reef #marinelife #canon #padi #photooftheday #ig #naturephotography #snorkeling #bhfyp"

    fine_art_name = "fine_art.txt"
    fine_art_content = "#fineart #art #painting #artist #portrait #contemporaryart #photography #modernart #artwork #abstractart #drawing #fineartphotography #artgallery #illustration #artcollector #sketch #instaart #blackandwhite #artistsoninstagram #bnw #gallery #visualart #arte #artforsale #sketchbook #artphotography #ink #contemporary #contemporarypainting #bhfyp"

    urban_exploration_name = "urban_exploration.txt"
    urban_exploration_content = "#urbex #urbanexploration #abandoned #decay #abandonedplaces #urban #urbexworld #urbandecay #photography #urbanexplorer #lostplaces #jj #ig #urbanart #urbanexploring #graffiti #urbanphotography #urbexphotography #architecture #urbexpeople #explore #lost #world #utopia #streetphotography #junkies #city #kings #grime #bhfyp"

    food_name = "food.txt"
    food_content = "#food #foodporn #foodie #instafood #love #yummy #foodphotography #eat #delicious #foodblogger #foodgasm #instagood #healthyfood #foodstagram #foodlover #like #travel #vegan #art #yum #dinner #photography #pasta #chef #pizza #organic #foodpic #wine #lunch"

    journalism_name = "journalism.txt"
    journalism_content = "#journalism #journalist #news #media #photography #photooftheday #magazine #music #bw #photojournalism #tv #reporter #writer #art #work #bnw #website #reportage #losangeles #blogger #streetphotography #blackandwhite #instagood #journalists #blog #politics #love #picoftheday #photographer #bhfyp"

    landscapes_name = "landscapes.txt"
    landscapes_content = "#landscapes #landscape #nature #landscapephotography #sunset #photography #ig #naturephotography #sky #travel #lovers #captures #naturelovers #photographer #mountains #landscapelovers #photooftheday #canon #view #amazing #lover #clouds #instagood #trees #sunrise #picoftheday #trip #travelblogger #sunsets"
    
    l = [{"name":peopel_name,"content":people_content},{"name":cel_name,"content":cel_content},
         {"name":per_arts_name,"content":per_arts_content},{"name":city_arch_name,"content":city_arch_content},
         {"name":city_arch_name,"content":city_arch_content},{"name":sport_name,"content":sport_content},
         {"name":commercial_name,"content":commercial_content},{"name":still_life_name,"content":still_lift_content},
         {"name":concert_name,"content":concert_content},{"name":street_name,"content":street_content},
         {"name":family_name,"content":family_content},{"name":transportation_name,"content":transportation_content},
         {"name":fashion_name,"content":fashion_content},{"name":film_name,"content":fashion_content},
         {"name":film_name,"content":film_content},{"name":underwater_name,"content":underwater_content},
         {"name":fine_art_name,"content":fine_art_content},{"name":urban_exploration_name,"content":urban_exploration_content},
         {"name":food_name,"content":food_content},{"name":journalism_name,"content":journalism_content},
         {"name":landscapes_name,"content":landscapes_content}]
    for item in l:
        write_to_file(item.get("name"),item.get("content"))
