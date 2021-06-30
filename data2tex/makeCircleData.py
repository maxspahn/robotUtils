from robotSaver import CircleSaver

cv1 = CircleSaver(1.0, 1.2, 0.6-0.1, "obst1.csv")
cv2 = CircleSaver(2.8, 0.0, 0.8-0.1, "obst2.csv")
cv3 = CircleSaver(-1.3, 1.0, 0.4-0.1, "obst3.csv")
cvGoal = CircleSaver(3.0, 2.0, 0.2, "goal.csv")
cv1.save()
cv2.save()
cv3.save()
cvGoal.save()





