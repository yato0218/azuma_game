import pyxel


screen_width = 160
screen_height = 120
stone_interval = 30
start_scene = "start"
play_scene = "play"
game_over_display_time = 60

class Debug:
    def __init__(self, mouse_x, mouse_y):
        self.mouse_x = mouse_x
        self.mouse_y = mouse_y
        
    def update(self, mouse_x, mouse_y):
        self.mouse_x = mouse_x
        self.mouse_y = mouse_y
    
    def draw(self):
        pyxel.text(10, 10, f"マウスの位置 {self.mouse_x}, {self.mouse_y}", pyxel.COLOR_YELLOW)
        
        


class Stone:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def update(self):
        if self.y < screen_height:
            self.y += 1
            
    def draw(self):
        #玉
        pyxel.blt(self.x, self.y, 0, 8, 0, 8, 8, pyxel.COLOR_BLACK)
        #pyxel.blt(表示させるゲーム画面のx座標, 表示させるゲーム画面のy座標, イメージバンクのインデックス番号, イメージバンク内のx座標, イメージバンク内のy座標, ピクセルアートの幅, ピクセルアートの高さ, 透明として扱うカラー)
        
        

class App:
    def __init__(self): #処理や定義を以下のinit関数とrun関数のなかに書いていく 
        pyxel.init(screen_width, screen_height, title = "俺のゲーム")
        pyxel.mouse(True)
        pyxel.load("my_resource.pyxres")
        self.jp_font = pyxel.Font("umplus_j10r.bdf")
        pyxel.playm(0, loop = True)
        self.debug = Debug(pyxel.mouse_x, pyxel.mouse_y)
        #シーン切り替え
        self.current_scene = start_scene
        
        pyxel.run(self.update, self.draw) # メソッドなのでselfがつく?
    
    def reset_play_scene(self):
        self.player_x = screen_width // 2
        self.player_y = screen_height * 4/5
        self.stones = []
        self.is_collision = False
        self.game_over_display_timer = game_over_display_time
        
    def update_start_scene(self):
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            self.reset_play_scene()
            self.current_scene = play_scene
        
    def update_play_scene(self):
        
        if self.is_collision:
            if self.game_over_display_timer > 0:
                self.game_over_display_timer -= 1
            else:
                self.current_scene = start_scene
            return
            
        #マウスの位置
        self.debug.update(pyxel.mouse_x, pyxel.mouse_y)
        
        #プレーヤーの移動
        if pyxel.btn(pyxel.KEY_RIGHT) and self.player_x < screen_width -16:
            self.player_x += 1
        elif pyxel.btn(pyxel.KEY_LEFT) and self.player_x > 0:
            self.player_x -= 1
         #石の追加
        if pyxel.frame_count % stone_interval == 0:#pyxel.frame_count % stone_interval == 0:
            self.stones.append(Stone(pyxel.rndi(0, screen_width - 8), 0))
        
        
        #石の落下
        for stone in self.stones.copy():
            stone.update()        
            #石とプレーヤーの衝突
            if (self.player_x <= stone.x <= self.player_x + 16 and self.player_y <= stone.y <= self.player_y + 16):
                self.is_collision = True
                
            #画面外にでた石を削除
            if stone.y >= screen_height:
                self.stones.remove(stone)
        
    def update(self):
        if pyxel.btnp(pyxel.KEY_ESCAPE):
            pyxel.quit()
            
        if self.current_scene == start_scene:
            self.update_start_scene()
        elif self.current_scene == play_scene:
            self.update_play_scene()
    
    def draw_start_scene(self):
        pyxel.blt(0, 0, 0, 8, 16, 180, 119)
        pyxel.text(screen_width // 10, screen_height // 10, "Click to start", pyxel.COLOR_GREEN, self.jp_font)
        
        
    def draw_play_scene(self):
        pyxel.cls(pyxel.COLOR_DARK_BLUE)
        
        #マウスの位置
        self.debug.draw()
        
        #石
        for stone in self.stones:
           stone.draw() 
        
        #pyxel.blt(表示させるゲーム画面のx座標, 表示させるゲーム画面のy座標, イメージバンクのインデックス番号, イメージバンク内のx座標, イメージバンク内のy座標, ピクセルアートの幅, ピクセルアートの高さ, 透明として扱うカラー)
        #キャラクター
        #pyxel.blt(self.player_x, screen_height * 4 // 5, 0, 16, 0, 16, 16, pyxel.COLOR_BLACK)
        
        pyxel.blt(self.player_x, self.player_y, 0, 32, 0, 16, 16, pyxel.COLOR_BLACK)
        # pyxel.text(70, 60, f"{self.number}", pyxel.COLOR_YELLOW) # pyxel.text(x座標, y座標, 表示させたい文字, 文字カラー)
        
        if self.is_collision:
            pyxel.text(screen_width // 2 -20, screen_height // 2, "Game Over", pyxel.COLOR_YELLOW)
    
    def draw(self):
        if self.current_scene == start_scene:
            self.draw_start_scene()
        elif self.current_scene == play_scene:
            self.draw_play_scene()
        
        


App()        
        

