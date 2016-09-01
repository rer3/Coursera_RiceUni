import random
import simplegui

CANVAS_WIDTH = 540
CANVAS_HEIGHT = 180
CONTROL_WIDTH = 100
CENTER_VERT = 0.3
CENTER_HORIZ = 0.8

MIN_DOORS = 3
MAX_DOORS = 10
SHOW = 2

class MontyHallGUI:
    
    def __init__(self):
        self.frame = simplegui.create_frame("MHP", CANVAS_WIDTH,
                                            CANVAS_HEIGHT, CONTROL_WIDTH)
        self.frame.set_canvas_background("White")
        self.frame.add_button("Clear", self.clear, CONTROL_WIDTH)
        self.frame.add_button("Add Door", self.add_door, CONTROL_WIDTH)
        self.frame.set_mouseclick_handler(self.click)
        self.frame.add_label("")
        self.win_label = self.frame.add_label("Wins = 0")
        self.lose_label = self.frame.add_label("Losses = 0")
        self.clear()
        self.frame.set_draw_handler(self.draw)
        self.frame.start()
        
    def clear(self):
        self.game_state = SELECT
        self.wins = 0
        self.losses = 0
        self.num_doors = MIN_DOORS
        self.win_label.set_text("Wins = " + str(self.wins))
        self.lose_label.set_text("Losses = " + str(self.losses))
        self.prize_door = random.randrange(self.num_doors)
        
    def click(self, pos):
        door_width = CANVAS_WIDTH / self.num_doors
        door_num = min(pos[0] / door_width, self.num_doors)
        if self.game_state == SELECT:
            self.process_door(door_num)
        elif self.game_state == CHOOSE:
            if door_num == self.selected_door or door_num == self.show_door:
                self.process_door(door_num)
        elif self.game_state == SHOW:
            self.process_door(door_num)
            
    def process_door(self, door_num):
        if self.game_state == SELECT:
            self.game_state = CHOOSE
            self.selected_door = door_num
            if door_num == self.prize_door:
                show_doors = range(self.num_doors)
                self.show_door = random.choice(show_doors)
            else:
                self.show_door = self.prize_door
        elif self.game_state == CHOOSE:
            if door_num == self.prize_door:
                self.wins += 1
                self.win_label.set_text("Wins = " + str(self.wins))
            else:
                self.losses += 1
                self.lose_label.set_text("Losses = " + str(self.losses))
            self.game_state = SHOW
        elif self.game_state == SHOW:
            self.prize_door = random.randrange(self.num_doors)
            self.game_state = SELECT
            
    def add_door(self):
        self.num_doors = min(self.num_doors + 1, MAX_DOORS)
        
    def draw_door(self, canvas, door_pos, color):
        

MontyHallGUI()
        