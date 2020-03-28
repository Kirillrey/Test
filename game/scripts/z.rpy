init -999 python:
    patched = False




init -997 python:

    if patched:
        mom = Character("Mom")
        dad = Character("Dad")
        mom_name = "Mom"
        aunt_name = "Aunt"

    else:
        mom = Character("Landlady")
        dad = Character("Landlord")
        mom_name = "Joyce"
        aunt_name = "Sofia"
        
        import re
        replace_dict = {
            "mom": "landlady",
            "moms": "landladies",
            "mommy": "landlady",
            "mother": "landlady",
            "mothers": "landladies",
            "dad": "landlord",
            "daddy": "landlord",
            "father": "landlord",
            "sister": "roommate",
            "sisters": "roommates",
            "sis": "roommate",
            "brother": "roommate",
            "brothers": "roommates",
            "bro": "roommate",
            "son": "tenant",
            "sons": "tenants",
            "child": "tenant",
            "children": "tenants",
            "daughter": "tenant",
            "daughters": "tenants",
            "sibling": "roommate",
            "siblings": "roommates",
            "aunt": "neighbor",
            "nephew": "neighbor",
            "newphews": "neighbors",
            "nieces": "neighbor",
            "niece": "neighbor",
            "aunty": "neighbor",
            "uncle": "neighbor",
            "auntie": "neighbor",
            "family": "household",
            "families": "households"
        }
        
        def game_text_mod(str):
            rc = re.compile('\\b|\\b'.join(map(re.escape, replace_dict)), re.I)
            def translate(match):
                key = match.group(0).lower()
                suffix = ""
                value = ""
                if "'s" in key:
                    key = key[:-2]
                    suffix = "'s"
                if match.group(0).isupper():
                    value = replace_dict[key].upper()
                elif match.group(0).istitle():
                    value = replace_dict[key].title()
                else:
                    value = replace_dict[key]
                return value + suffix
            return rc.sub(translate, str)
        
        config.say_menu_text_filter = game_text_mod
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
