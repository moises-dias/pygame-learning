class Player:
    def __init__(self, pos, isometric_pos):
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
    
    def walk(self, up, down, left, right, floor_bboxes):
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
            print(self.pos) # debug
            if self.pos == [759.0, 219.0]: # debug
                print("here") # debug
            for bbox in floor_bboxes:
                x1 = bbox[0][0]
                y1 = bbox[0][1]
                x2 = bbox[2][0]
                y2 = bbox[2][1]


                # bug: entra nesse if pq ele ta dentro
                # 759, 219 está dentro do canto 760, 220
                if  not (x1 <= self.pos[0] <= x2 and y1 <= self.pos[1] <= y2):
                    continue

                print([self.pos[0] + d_x, self.pos[1] + d_y])
                # bug: NAO entra nesse if pq ao mover ele sai
                # 761, 221 NAO está dentro do canto 760, 220
                if  x1 <= self.pos[0] + d_x <= x2 or y1 <= self.pos[1] + d_y <= y2:
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

                    if self.pos == [759.0, 219.0]: # debug
                        print(up, down, left, right) # debug

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
