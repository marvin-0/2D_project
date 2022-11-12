# def char_ground():
#     global rockman
#     for i in range(ground_amount):
#         if rockman.y - 25 <= ground[i].y + 25 and rockman.y - 25 >= ground[i].y - 25:
#             if (rockman.x + 10 > ground[i].x - 25 and rockman.x + 10 < ground[i].x + 25) or (rockman.x - 10 > ground[i].x - 25 and rockman.x - 10 < ground[i].x + 25):
#                 if i == 55:
#                     ground[i].x = 10000
#                 if i == 57:
#                     spike_up[6].shot = 1
#                 if i == 61:
#                     spike_up[6].shot = 3
#                 if i == 62:
#                     spike_up[16].shot = 2
#                 rockman.y += 4
#                 if rockman.jump_on != 0 and i != 55:
#                     rockman.jump_on = 0
#                     rockman.jump = 0
#                     rockman.jump_dis = 0
#                 break
#         if rockman.y + 25 >= ground[i].y - 25 and rockman.y + 25 <= ground[i].y + 25:
#             if (rockman.x + 10 > ground[i].x - 25 and rockman.x + 10 < ground[i].x + 25) or (rockman.x - 10 > ground[i].x - 25 and rockman.x - 10 < ground[i].x + 25):
#                 if rockman.jump == 1:
#                     rockman.jump_on = 2
#                 break
#
#         if rockman.x + 20 <= ground[i].x + 25 and rockman.x + 20 >= ground[i].x - 25:
#             if (rockman.y + 20 >= ground[i].y - 25 and rockman.y + 20 <= ground[i].y + 25) or (rockman.y - 20 >= ground[i].y - 25 and rockman.y - 20 <= ground[i].y + 25):
#                 # rockman.x -= rockman.dir * character_class.RUN_SPEED_PPS * game_framework.frame_time
#                 rockman.Stop()
#                 break
#         if rockman.x - 20 <= ground[i].x + 25 and rockman.x - 20 >= ground[i].x - 25:
#             if (rockman.y + 20 >= ground[i].y - 25 and rockman.y + 20 <= ground[i].y + 25) or (rockman.y - 20 >= ground[i].y - 25 and rockman.y - 20 <= ground[i].y + 25):
#                 # rockman.x += rockman.dir * character_class.RUN_SPEED_PPS * game_framework.frame_time
#                 rockman.Stop()
#                 break
#     if rockman.y + 25 <= 0:
#         rockman.hp -= 50
#     if rockman.x > spike_up[11].x and spike_up[16].shot != 0:
#         spike_up[12].shot = 1
#
# def char_spike():
#     for s in spike_up[:]:
#         if rockman.x >= s.x - 25 and rockman.x <= s.x + 25:
#             if rockman.y >= s.y - 25 and rockman.y <= s.y + 25:
#                 rockman.hp -= 50


# if ba <= tb and ba >= bb:
#     if (la + 5 > lb and la + 5 < rb) or (ra - 5 > lb and ra - 5 < rb):
#         a.ground_collision(1, b)
#         b.ground_collision(1, a)
# # 땅 아랫면
# if ta >= bb and ta <= tb:
#     if (la + 5 > lb and la + 5 < rb) or (ra - 5 > lb and ra - 5 < rb):
#         a.ground_collision(2, b)
#         b.ground_collision(2, a)
# # 땅 왼면
# if ra <= rb and ra >= lb:
#     if (ta - 5 <= tb and ta - 5 >= bb) or (ba + 5 <= tb and ba + 5 >= bb):
#         a.ground_collision(3, b)
#         b.ground_collision(3, a)
# # 땅 오른면
# if la >= lb and la <= rb:
#     if (ta - 5 <= tb and ta - 5 >= bb) or (ba + 5 <= tb and ba + 5 >= bb):
#         a.ground_collision(4, b)
#         b.ground_collision(4, a)
