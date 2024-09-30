import pickle
from PIL import Image
def main(s):
    for k in range(6):
        with open(f"textures/{s}/{k}.ciu", 'rb') as file: ciu = pickle.load(file)
        cube = Image.new("RGBA", (13, 13), (0, 0, 0, 0))
        cube.putdata([i for j in ciu for i in j])
        cube_e = cube.resize((cube.width * 10, cube.height * 10), Image.NEAREST)
        cube_e.show()
if __name__ == '__main__':
    s = input("name\033[92m_")
    main(s)