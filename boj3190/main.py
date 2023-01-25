import sys
import os

class bam():
    def __init__(self,ms,ap,tp):
        self.map_size = ms
        self.apple = ap
        self.apple_getsu = len(ap)
        self.tp = tp
        self.gt = 0 # output
        ## dont touch
        self.bam_l = 1
        self.bam_head = [1,1]
        self.bam_body = [[1,1]]
        
        
        self.mr = [0,1]
        self.ml = [0,-1]
        self.md = [1,0]
        self.mu = [-1,0]
        self.md_set = [self.mr,self.md,self.ml,self.mu]
        self.moving_dir = 0 # default

    def mover(self):
        #for kka in range(
        move_temp = [self.bam_head[i]+self.md_set[self.moving_dir][i] for i in range(2)]
        self.bam_body.append(move_temp)
        self.bam_head = move_temp
        print("head position : ", move_temp)
        
        if self.checker():
            return True
        return False

    def checker(self):
                
        if self.catch_body():
            return True
        if self.head_position_out():
            return True
        
        if self.apple_eat():
            del self.bam_body[0]
        
        print("body position : ", self.bam_body)

        return False

    def apple_eat(self):
        for kka in range(len(self.apple)):
            if self.bam_head == self.apple[kka]:
                self.bam_l += 1
                print("bam eat apple! bam length : ",self.bam_l)
                del self.apple[kka]
                if self.bam_l + len(self.apple) != self.apple_getsu+1:
                    print("bam length not same")
                return False
        
        return True

    def catch_body(self):
        te = len(self.bam_body) - 1
        for kka in range(te):
            if self.bam_head == self.bam_body[kka]:
                print("catch body")
                return True
        return False

    def head_position_out(self):
        for kka in range(2):
            if self.bam_head[kka] <= 0 or self.bam_head[kka] > self.map_size:
                print("head out")
                return True
        
        return False
        
    
    def run_game(self):
        turn_time = 0
        test_time = 100
        for tt in range(test_time):
            t = tt+1
            print('now t : ',t)

            if self.mover():
                print()
                print()
                print()
                print('end!!')
                print()
                print(t)
                return True


            if self.tp[-1][0] >= t:
                print('turn time :' , self.tp[turn_time][0])
                if t == self.tp[turn_time][0]:
                    if self.tp[turn_time][1] == 1:
                        self.moving_dir += 1
                    else:
                        self.moving_dir -= 1
                    turn_time += 1
                    print("turn!!")

def main():
    file_name = './input1.txt'
    dat = list()
    apple = list()
    turn_point = list()
    map_size = 0
    with open(file_name,'r') as f:
        line = 1
        while(True):
            aa = f.readline().strip()
            if not aa:
                break
            print(aa)
            dat.append(aa)
    print()
    print()
    print()
    ap = 100
    for kka in range(len(dat)):
        if kka == 0:
            map_size = int(dat[kka])
            continue
        if kka == 1:
            ap = int(dat[kka])
            for kki in range(ap):
                temp = dat[kka+kki+1].split(' ')
                #print(temp)
                apple.append([int(temp[0]),int(temp[1])])
            #print(kka+ap+1)
            tp = int(dat[kka+ap+1])
            for kki in range(tp):
                temp = dat[kka+kki+1+ap+1].split(' ')
                print(temp)
                if temp[1] == 'D':
                    turn_point.append([int(temp[0]),1])
                else :
                    turn_point.append([int(temp[0]),0])
            break
    print(map_size)
    print(apple)
    print(turn_point)

    ## game start ##
    bam_sim = bam(map_size,apple,turn_point)
    bam_sim.run_game()


if __name__ == "__main__":
    main()
