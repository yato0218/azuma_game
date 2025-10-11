import pyxel

screen_width = 180
screen_height = 160


player_size_x = 16
player_size_y = 16
player_first_position_x = 20
player_first_position_y = 104
player_speed = 2
player_jump = 7
player_frame_interval = 1
player_frame_num = 8

gravity_switch = True


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
        self.ground_y = 140
        self.gravity = 2
        self.dt = 0.4
        
    def update(self):
        self.world_x += player_speed
        # if pyxel.btn(pyxel.KEY_RIGHT):
        #         self.world_x += player_speed
        # if pyxel.btn(pyxel.KEY_LEFT):
        #     self.world_x = max(self.world_x - player_speed, 0)
        #カメラを更新することで、ワールドが動いたように見える
        self.camera_x = self.world_x
            
    def draw(self):
        for i in range(20):
            x = i * 16 - self.camera_x
            #pyxel.rect(x, self.ground_y, 16, 16, 11)
            
class Background:
    def __init__(self, world):
        self.world = world
    
    def update(self):
        pass

    def draw(self, camera_x):
        # #地面
        #pyxel.blt(100 - camera_x, self.world.ground_y, 1, 0, 0, 16, 8, pyxel.COLOR_BLACK)
        #pyxel.blt(表示させるゲーム画面のx座標, 表示させるゲーム画面のy座標, イメージバンクのインデックス番号, イメージバンク内のx座標, イメージバンク内のy座標, ピクセルアートの幅, ピクセルアートの高さ, 透明として扱うカラー)
        
        pyxel.bltm(0 - camera_x, 0, 0, 0, 0, 2047, screen_height, pyxel.COLOR_PINK)

        # for i in range(10):
        #     x = i * 80 - camera_x * 0.5
        #     pyxel.tri(x, 104, x + 40, 60, x + 80, 104, 3)
            #pyxel.rect(x, 0, 16, 16, 11)


class Player:
    def __init__(self, world):
        self.player_x = player_first_position_x
        self.player_y = player_first_position_y
        self.world = world
        self.velocity_y = 0
        self.jump_count = 0
        
        
        
    def update(self):
        if (self.jump_count < 1 and pyxel.btnp(pyxel.KEY_UP)
        or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_A)
        or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_B)
        or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_X)
        or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_Y)
        ):
            self.velocity_y -= player_jump
            self.jump_count += 1
        
        #ここで重力計算しておく
        self.velocity_y += self.world.gravity * self.world.dt
        
        if gravity_switch:
            
            #playerの座標を計算
            self.player_y += self.velocity_y
        
        #print(f"self.player_y: {self.player_y}")
                
        tile_x = (self.player_x + self.world.camera_x + player_size_x // 2 ) // 8
        tile_y = (self.player_y + player_size_y) // 8
        
        tile = pyxel.tilemap(0).pget(tile_x, tile_y)
        print(f"tile: {tile}")
                
            
        if tile == (0, 4):
            if self.velocity_y > 0:#速度が正の値ということは落下状態ということ.
                self.player_y = tile_y * 8 - player_size_y
                self.velocity_y = 0
                self.jump_count = 0
        
    
    def draw(self):
        self.frame_index = (pyxel.frame_count // player_frame_interval) % player_frame_num
        self.u = self.frame_index * 16 + 16
        pyxel.blt(self.player_x, self.player_y, 0, self.u, 0, player_size_x, player_size_y, pyxel.COLOR_BLACK)
        #pyxel.text(10, 50, f"frame_index: {self.frame_index}", pyxel.COLOR_PINK)

    
        
class App:
    def __init__(self):
        pyxel.init(screen_width, screen_height, title = "Azuma_game")
        pyxel.load("my_resource.pyxres")
        pyxel.mouse(True)
        pyxel.playm(0, loop = True)
        #pyxel.stop()
        self.world = World()
        self.background = Background(self.world)
        self.player = Player(self.world)
        
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
        pyxel.cls(3)
        
        #描画
        self.background.draw(self.world.camera_x)
        self.world.draw()
        self.player.draw()
        
        self.debug.draw(pyxel.mouse_x, pyxel.mouse_y)
        self.debug.draw(pyxel.mouse_x, pyxel.mouse_y, self.world.world_x)
        
        
App()
        