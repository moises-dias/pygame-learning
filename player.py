from player_sprite import PlayerSprite

class Player:
    def __init__(self, pos, isometric_pos, starting_directon, spriteflyweight):
        self.sprite = PlayerSprite(spriteflyweight.get_image("assets/player_with_idle.png"))
        self.border = 15
        self.pos = pos
        self.isometric_pos = isometric_pos
        self.square_reference = [
            (-self.border, -self.border), 
            (-self.border, self.border), 
            (self.border, self.border), 
            (self.border, -self.border)]
        self.isometric_reference = [
            (0, -self.border), 
            (-2 * self.border, 0), 
            (0, self.border), 
            (2 * self.border, 0)
        ]
        self.speed = 2
        self.speed_reducer = 0.5
        # TODO direction e walking e usado na sprite, mas e atributo do player, onde deixar?
        self.walking = False
        self.direction = starting_directon

        # TODO talvez isso fique melhor dentro da classe sprite
        self.direction_dict = {
            (1, 0, 0, 0): "N",
            (0, 1, 0, 0): "S",
            (0, 0, 1, 0): "O",
            (0, 0, 0, 1): "E",
            (1, 0, 1, 0): "NO",
            (1, 0, 0, 1): "NE",
            (0, 1, 1, 0): "SO",
            (0, 1, 0, 1): "SE",
        }

    
    #TODO walk tem que atualizar os atributos da sprite
    def walk(self, up, down, left, right, floor_bboxes):

        if (up - down) != 0 or (left - right) != 0:
            self.walking = True
        else:
            self.walking = False
            return

        self.update_direction(up, down, left, right)

        d_x = 0
        d_y = 0
        isometric_d_x = 0
        isometric_d_y = 0

        updated = False

        d_x = (right - left) * self.speed + (down - up) * self.speed
        d_y = (left - right) * self.speed + (down - up) * self.speed
        isometric_d_x = 2 * (right - left) * self.speed
        isometric_d_y = (down - up) * self.speed

        if left == 1 or right == 1:
            d_x *= self.speed_reducer
            d_y *= self.speed_reducer
            isometric_d_x *= self.speed_reducer
            isometric_d_y *= self.speed_reducer
        
        for bbox in floor_bboxes:
            x1 = bbox[0][0]
            y1 = bbox[0][1]
            x2 = bbox[2][0]
            y2 = bbox[2][1]


            if  x1 <= self.pos[0] + d_x <= x2 and y1 <= self.pos[1] + d_y <= y2:

                self.pos[0] += d_x
                self.pos[1] += d_y
                self.isometric_pos[0] += isometric_d_x
                self.isometric_pos[1] += isometric_d_y

                updated = True
                break

        if not updated and (up + down + left + right) == 1:
            for bbox in floor_bboxes:
                x1 = bbox[0][0]
                y1 = bbox[0][1]
                x2 = bbox[2][0]
                y2 = bbox[2][1]


                # movendo só em x ou movendo só em y eu to dentro de algum quadrado?
                if (x1 <= self.pos[0] + d_x <= x2 and y1 <= self.pos[1] <= y2) or (x1 <= self.pos[0] <= x2 and y1 <= self.pos[1] + d_y <= y2):

                    if x1 <= self.pos[0] + d_x <= x2:
                        if left == 1:
                            up = 1
                        elif right == 1:
                            down = 1
                        elif up == 1:
                            left = 1
                        elif down == 1:
                            right = 1
                    elif y1 <= self.pos[1] + d_y <= y2:
                        if left == 1:
                            down = 1
                        elif right == 1:
                            up = 1
                        elif up == 1:
                            right = 1
                        elif down == 1:
                            left = 1

                    up *= self.speed_reducer
                    down *= self.speed_reducer
                    left *= self.speed_reducer
                    right *= self.speed_reducer

                    d_x = (right - left) * self.speed + (down - up) * self.speed
                    d_y = (left - right) * self.speed + (down - up) * self.speed
                    isometric_d_x = 2 * (right - left) * self.speed
                    isometric_d_y = (down - up) * self.speed

                    if  x1 <= self.pos[0] + d_x <= x2 and y1 <= self.pos[1] + d_y <= y2:

                        self.pos[0] += d_x
                        self.pos[1] += d_y
                        self.isometric_pos[0] += isometric_d_x
                        self.isometric_pos[1] += isometric_d_y
                        break  

    def get_isometric_position_square(self):
        isometric_position_vertices = []
        for v in self.isometric_reference:
            isometric_position_vertices.append((self.isometric_pos[0] + v[0], self.isometric_pos[1] + v[1]))
        return isometric_position_vertices

    def get_position_square(self):
        position_vertices = []
        for v in self.square_reference:
            position_vertices.append((self.pos[0] + v[0], self.pos[1] + v[1]))
        return position_vertices

    def get_sprite_position(self):
        return [
            self.isometric_pos[0] - self.sprite.offset_x, 
            self.isometric_pos[1] - self.sprite.offset_y
        ]

    def update(self):
        self.sprite.update(self.direction, self.walking)

    def update_direction(self, up, down, left, right):
        if up == down:
            up = 0
            down = 0
        if left == right:
            left = 0
            right = 0
        
        if (up, down, left, right) in self.direction_dict:
            self.direction = self.direction_dict[(up, down, left, right)]
        
    def reset_position(self, pos, isometric_pos, direction):
        self.pos = pos
        self.isometric_pos = isometric_pos
        self.walking = False
        self.direction = direction
        # TODO se o player ja estivesse parado e olhando nessa direcao pode dar ruim?
        self.sprite.update(self.direction, self.walking)