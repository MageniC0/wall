from PIL import Image

def main(n, e):
    _o = Image.open(n + ".png")
    _e = _o.resize((_o.width * e, _o.height * e), Image.NEAREST)
    _e.save(n + "_.png")
    _e.show()

if __name__ == "__main__":
    n = input("input path\033[92m_")
    e = int(input("enlarge\033[92m_"))
    main(n, e)