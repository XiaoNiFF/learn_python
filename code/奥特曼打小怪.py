from random import randint, randrange


class role(object):
    '''
    创建角色类，包含：
    属性：血量
    方法：是否活着
    方法：普通攻击，对其他角色    
    '''

    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def isalive(self):
        return self.hp > 0

    def attack(self, other):
        '''other：被攻击的对象'''
        pass


class Ultraman(role):
    '''奥特曼'''

    def __init__(self, name, hp, mp, mp_max):
        super().__init__(name, hp)
        self.mp = mp
        self._mp_max = mp_max

    def attack(self, other):
        '''普通攻击'''
        other.hp -= randint(15, 25)

    def huge_attack(self, other):
        '''
        大招，消耗50点mp，若mp不够则普攻，触发概率1/10
        打掉对方3/4的
        当前血量，或者50点血量
        '''
        if self.mp >= 50:
            self.mp -= 50
            harm = other.hp * (3 / 4)
            harm = harm if harm >= 50 else 50
            other.hp -= harm
            return True
        else:
            self.attack(other)
            return False

    def magic_attack(self, others):
        '''
        魔法攻击：群里攻击，消耗20点mp
        others：包含若干个对象的列表
        '''
        if self.mp >= 20:
            self.mp -= 20
            for other in others:
                if other.isalive():
                    other.hp -= randint(10, 15)
            else:
                return True
        else:
            return False

    def resume_mp(self):
        resume_value = randint(1, 10)
        if self.mp + resume_value <= self._mp_max:
            self.mp += resume_value            
            return resume_value
        else:
            return self._mp_max - self.mp

    def __str__(self):
        return '~~~{}奥特曼~~~\n 生命值：{}\n 魔法值：{}' \
            .format(self.name, self.hp, self.mp)


class Monster(role):
    '''小怪兽'''

    def attack(self, other):
        other.hp -= randint(10, 20)

    def __str__(self):
        return '~~~{}小怪兽~~~\n 生命值：{}' \
            .format(self.name, self.hp)


def is_any_alive(monsters):
    for monster in monsters:
        if monster.isalive():
            return True
    else:        
        return False

def select_alive_monster(monsters):
    monsters_len = len(monsters)
    while True:
        index = randrange(monsters_len)
        if monsters[index].isalive():
            return monsters[index]

def display_info(ultraman, monsters):
    print(ultraman)
    for monster in monsters:
        print(monster)

fights_total_count = 100
ultraman_win_count = 0
monster_win_count = 0

def main():
    u = Ultraman('辛克', 1800, 120, 120)
    m1 = Monster('猫', 250)
    m2 = Monster('狗', 500)
    m3 = Monster('老虎', 750)
    ms = [m1, m2, m3]
    fight_round = 1
    while u.isalive() and is_any_alive(ms):
        # input('回车开始战斗，Ctrl+C结束战斗')
        print('\n=====第{:2d}回合====='.format(fight_round))
        m = select_alive_monster(ms)
        # 奥特曼开始攻击：
        skill = randint(1, 10) #通过随机数字选择Ultraman用那种技能
        if skill <= 6:
            u.attack(m)
            print('{0}使用普通攻击打了{1}\n{0}的魔法恢复了{2}点' \
                .format(u.name, m.name,u.resume_mp()))
        elif skill <= 9:
            if u.magic_attack(ms):
                print('{}使用了魔法攻击'.format(u.name))
            else:
                print('{}使用魔法失败'.format(u.name))
        else:
            if u.huge_attack(m):
                print('{}使用究极大招虐杀了{}'.format(u.name, m.name))
            else:
                print('{}没蓝放大招了,普攻打了{}，恢复了{}魔法' \
                    .format(u.name, m.name, u.resume_mp()))
        
        # 小怪兽开始攻击
        for m in ms:
            if m.isalive():
                m.attack(u)
                print('{}回击了奥特曼{}'.format(m.name, u.name))
        display_info(u, ms)
        fight_round += 1
    print ('\n=====战斗结束=====\n')
    global ultraman_win_count, monster_win_count
    if u.isalive():
        print('{}奥特曼胜利'.format(u.name))
        ultraman_win_count += 1
    else:
        print('小怪兽胜利')
        monster_win_count += 1


if __name__ == "__main__":
    for fight in range(fights_total_count):main()
    print('\n=====统计=====\n共进行了{}场战斗，其中：\n奥特曼赢了{}场\n小怪兽赢了{}场' \
        .format(fights_total_count,ultraman_win_count,monster_win_count))
    # main()