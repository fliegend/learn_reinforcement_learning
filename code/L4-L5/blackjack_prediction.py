# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 14:50:42 2020

@author: lijiancong
"""

'''''''''''
蒙特卡洛预测
'''''''''''
from blackjack import Player, Dealer, Arena
from utils import set_dict,get_dict
from utils import draw_value

A=["继续叫牌","停止叫牌"]
display = False
# 创建一个玩家一个庄家，玩家使用原始策略，庄家使用其固定的策略
player = Player(A = A, display = display)
dealer = Dealer(A = A, display = display)
# 创建一个场景
arena = Arena(A = A, display=display)
# 生成num个完整的对局
arena.play_games(dealer, player, num=20000)
    
# 统计个状态的价值，衰减因子为1，中间状态的即时奖励为0，递增式蒙特卡洛评估
def policy_evaluate(episodes, V, Ns):
    for episode, r in episodes:
        for s, a in episode:
            ns = get_dict(Ns, s)
            v = get_dict(V, s)
            set_dict(Ns, ns+1, s)
            set_dict(V, v+(r-v)/(ns+1), s)

V = {} # 状态价值字典
Ns = {} # 状态被访问的次数节点
policy_evaluate(arena.episodes, V, Ns) # 学习V值
#print(V)

draw_value(V, useable_ace = True, A = A) # 绘制状态价值图
draw_value(V, useable_ace = False, A = A) # 绘制状态价值图

# 观察几局对局信息
display = True
player.display, dealer.display, arena.display = display, display, display
arena.play_games(dealer, player, num =2)



