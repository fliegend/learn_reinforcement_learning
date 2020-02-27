# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 15:08:20 2020

@author: lijiancong
"""

'''''''''''
蒙特卡洛控制
'''''''''''
from blackjack import Dealer, Arena, MC_Player
from utils import draw_value, draw_policy
from utils import epsilon_greedy_policy
import math


A=["继续叫牌","停止叫牌"]
display = False
player = MC_Player(A = A, display = display)
dealer = Dealer(A = A, display = display)
# 创建一个场景
arena = Arena(A = A, display=display)

arena.play_games(dealer = dealer, player = player,num = 20000, show_statistic = True)
#print(player.Q)
#print(player.A)
  
draw_value(player.Q, useable_ace = True, is_q_dict=True, A = player.A)
draw_policy(epsilon_greedy_policy, player.A, player.Q, epsilon = 1e-10, useable_ace = True)
draw_value(player.Q, useable_ace = False, is_q_dict=True, A = player.A)
draw_policy(epsilon_greedy_policy, player.A, player.Q, epsilon = 1e-10, useable_ace = False)

'''
display = False
arena.display = display
player.display = display
dealer.display = display
arena.play_games(dealer,player,num=10000, show_statistic = True)

display = True
arena.display = display
player.display = display
dealer.display = display
arena.play_games(dealer,player,num=10, show_statistic = True)
'''
