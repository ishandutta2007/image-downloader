#coding=utf-8
import os
import fnmatch

dir_list = [
"thuy_film",
"mandy_transportation",
"risa_food23",
"dona_nature",
"allyn_animal",
"peg_aerial",
"maye_celebrities",
"lory_art23",
"nola_commercial",
"milda_street",
"roxy_city23",
"tarra_performing",
"remona_sport23",
"neda_family23",
"eula_macro",
"kylie_abstract",
"caron_concert",
"fanny_journalism",
"tyler_landscapes",
"sasha_travel23",
"lucy_travel23",
"kia_travel23",
"belva_black23",
"un_underwater",
"rona_art23",
"fe_luxury",
"elane_girl23",
"belen_woman23",
"tina_model23",
"ella_pretty233",
"ida_color23",
"alix_malys",
"karo_loyer",
"hee_prall",
"jene_ronn",
"jani_dorst",
]
def begin_remove():
    print "-----"
    for root, dir, files in os.walk("F:/500px3"):
        print "~~~~"
        print root.split("\\")[-1]

        if root.split("\\")[-1] not in dir_list:
            continue
        print root
        print ""
        for items in fnmatch.filter(files, "*.txt"):
            print "..." + items
            with open(os.path.join(root,items))  as f:
                lines = f.readlines()[0]
                str_list = "#".join(lines.split("#")[:11])
                f2 = open(os.path.join(root,items),"w")
                f2.writelines(str_list)
                f2.close()
        print ""

if __name__ == '__main__':
    begin_remove()
