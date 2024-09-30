#laer wall 0.6.2 copyright dvclv 2024
import pickle
from PIL import Image
class _maps:
    def __init__(self, st):
        self.st = st
        with open(f"terrain/{self.st}.trr", 'rb') as file: self.trr = pickle.load(file)
        self.trh = [[[0 for x in range(6)] for y in range(6)] for z in range(6)]
        for z in range(4):
            for y in range(4):
               for x in range(4):
                   self.trh[z+1][y+1][x+1] = self.trr[z][y][x]
    def lin(self, x, y, z):
        return [self.trh[z+1][y+1][x+2],
                self.trh[z+1][y+1][ x ],
                self.trh[z+1][y+2][x+1],
                self.trh[z+1][ y ][x+1]]
class _graph:
    def __init__(self, n2, n3):
        self.n2 = n2
        self.n3 = n3
        self.pixels = [[(0,0,0,0) for i in range(49)] for j in range(49)]
        self.ciu = [0,0,0,0,0,0]
        for k in range(6):
            with open(f"textures/{self.n2}/{k}.ciu", 'rb') as file: self.ciu[k] = pickle.load(file)
    def drew(self, k, m, n):
        for j in range(13):
            for i in range(13):
                if self.ciu[k][j][i][3] != 0:
                    self.pixels[n+j][m+i] = self.ciu[k][j][i]
    def done(self):
        self.image = Image.new("RGBA", (49, 49), (0, 0, 0, 0))
        self.image.putdata([i for j in self.pixels for i in j])
        self.image.save(self.n3 + ".png")
        print("[wall]done.")

def main(nt, n2, n3):
    maps = _maps(nt) 
    graph = _graph(n2, n3)
    for z in range(4):
        for y in range(4):
            for x in range(4):
                if maps.trr[z][y][x] == 1:
                    m = 18 - 6*x + 6*y
                    n = 24 + 2*x + 2*y - 8*z
                    lin = maps.lin(x, y, z)
                    if lin[0] == 0 and lin[2] == 0:
                        graph.drew(0, m, n)
                    if lin[0] == 1 and lin[2] == 0:
                        if lin[1] == 1 and lin[3] == 0:
                            graph.drew(1, m, n)
                        else:
                            graph.drew(2, m, n)
                    if lin[0] == 0 and lin[2] == 1:
                        if lin[1] == 0 and lin[3] == 1:
                            graph.drew(3, m, n)
                        else:
                            graph.drew(4, m, n)
                    if lin[0] == 1 and lin[2] == 1:
                        graph.drew(5, m, n)
    graph.done()

    
if __name__ == "__main__":
    nt = input("terrain\033[92m_")
    n2 = input("textures\033[92m_")
    n3 = input("save as\033[92m_")
    main(nt, n2, n3)