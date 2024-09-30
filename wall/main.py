import re
import lines, setwall, wall, view,  enlarge

def main():
    while True:
        print('__'*34)
        ln = input("\033[92m_")
        if len(ln) == 0:                                break
        elif ln=="di":                                  lines.dn("."     )
        elif ln=="su":                                  lines.set_up(    )
        elif lm:=re.match(r"sw (\w+)",ln):              setwall.main(      lm.group(1))
        elif lm:=re.match(r"vw (\w+)",ln):              view.main(         lm.group(1))
        elif lm:=re.match(r"wl (\w+) (\w+) (\w+)",ln):  wall.main(         lm.group(1),     lm.group(2), lm.group(3))
        elif lm:=re.match(r"en (\w+) (\d+)",ln):        enlarge.main(      lm.group(1), int(lm.group(2))            )
        else:                                           print("\033[93m_")

try:
    main()
except Exception as e:
    print(e)
    print("\033[93m_")
