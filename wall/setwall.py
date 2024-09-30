import pickle, os
from PIL import Image

def main(s):
    li = Image.open(s+".png")
    su = [[[[0,0,0,0] for i in range(13)] for j in range(13)] for n in range(6)]
    
    for v in range(2):
        for u in range(3):
            for j in range(13):
                for i in range(13):
                    su[u+3*v][j][i] = li.getpixel((13*u + i, 13*v + j))
        
    try:
        os.makedirs(f"textures/{s}")
    except FileExistsError:
        print("FileExistsError.")
    
    for n in range(6):
        with open(f"textures/{s}/{n}.ciu", 'wb') as file: pickle.dump(su[n], file)
    
    print("[setwall]done.")
    
if __name__ == "__main__":
    s = input("\033[92m_")
    main()