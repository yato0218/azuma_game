import pyxel

screen_width = 180
screen_height = 120
player_frame_interval = 1
player_frame_num = 8
#pyxel.frame_count

class Player:
    def __init__(self):
        pass
    def update(self):
        pass
    
    def draw(self):
        frame_index = (pyxel.frame_count // player_frame_interval) % player_frame_num
        u = frame_index * 16 - 16
        pyxel.blt(screen_width // 5, screen_height * 4 // 5, 0, u, 0, 16, 16, pyxel.COLOR_BLACK)
        #pyxel.text(10, 10, f"frame_index: {frame_index}", pyxel.COLOR_GREEN)
            

class App:
    def __init__(self):
        pyxel.init(screen_width, screen_height, title = "char")
        pyxel.load("my_resource.pyxres")
        pyxel.mouse(True)
        self.player = Player()
        
        
        
        
        
        pyxel.run(self.update, self.draw)
        
    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        
        
        
    def draw(self):
        pyxel.cls(0)
        self.player.draw()

App()
