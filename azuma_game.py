import pyxel

player_first_position_x = 20
player_first_position_y = 100
player_speed = 5


class Debug:
    def __init__(self, mouse_x, mouse_y):
        self.mouse_x = mouse_x
        self.mouse_y = mouse_y
        
    def update(self, mouse_x, mouse_y):
        self.mouse_x = mouse_x
        self.mouse_y = mouse_y
    
    def draw(self, mouse_x, mouse_y, world_x = None):
        pyxel.text(10, 10, f"mousex: {mouse_x} mouse_y: {mouse_y}", pyxel.COLOR_GREEN)
        if world_x is not None:
            pyxel.text(10, 20, f"world_x: {world_x}", pyxel.COLOR_YELLOW)

class World:
    def __init__(self):
        self.world_x = 0
        self.camera_x = 0
        self.ground_y = 104
        
    def update(self):
            
        if pyxel.btn(pyxel.KEY_RIGHT):
                self.world_x += player_speed
        if pyxel.btn(pyxel.KEY_LEFT):
            self.world_x = max(self.world_x - player_speed, 0)
        #カメラを更新することで、ワールドが動いたように見える
        self.camera_x = self.world_x - 60
            
    def draw(self):
        for i in range(20):
            x = i * 16 - self.camera_x
            #pyxel.rect(x, self.ground_y, 16, 16, 11)
            
class Background:
    def __init__(self):
        pass
    
    def update(self):
        pass

    def draw(self, camera_x):
        #背景
        for i in range(10):
            x = i * 80 - camera_x * 0.5
            #pyxel.tri(x, 104, x + 40, 60, x + 80, 104, 3)
            pyxel.rect(x, 0, 16, 16, 11)


class Player:
    def __init__(self):
        self.player_x = player_first_position_x
        self.player_y = player_first_position_y
        
    def update(self):
        pass
    
    def draw(self):
        pass
        pyxel.blt(self.player_x, self.player_y, 0, 0, 0, 16, 16, pyxel.COLOR_BLACK)

    
        
class App:
    def __init__(self):
        pyxel.init(160, 120, title = "Azuma_game")
        pyxel.load("my_resource.pyxres")
        pyxel.mouse(True)
        self.world = World()
        self.background = Background()
        self.player = Player()
        
        self.debug = Debug(pyxel.mouse_x, pyxel.mouse_y)
        
        pyxel.run(self.update, self.draw)
        
        
    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        
        self.background.update()
        self.world.update()
        self.player.update()
        
        self.debug.update(pyxel.mouse_x, pyxel.mouse_y)
        
        
    def draw(self):
        pyxel.cls(12)
        
        #描画
        self.background.draw(self.world.camera_x)
        self.world.draw()
        self.player.draw()
        
        self.debug.draw(pyxel.mouse_x, pyxel.mouse_y)
        self.debug.draw(pyxel.mouse_x, pyxel.mouse_y, self.world.world_x)
        
        
App()
        