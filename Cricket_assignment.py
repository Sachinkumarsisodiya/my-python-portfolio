players = ["rohit","virat","dhoni","shubman","hardik","jaiswal","shreyas","rahul","ashwin","bumrah","asrshdeep"]
score = [
    [ 100, 150, 50, 180,131],
    [ 20, 200, 30, 28,121],
    [ 30, 35, 80, 18,13],
	[ 40, 45, 45, 19,15],
	[ 58, 55, 58, 21,18],
	[ 63, 65, 46, 1,100],
	[70 ,75 ,35 ,13 ,65],
	[8 ,85 ,47 ,38 ,75],
	[69 ,95 ,50 ,18,12],
    [ 30, 35, 80, 18,13],
    [ 58, 55, 58, 21,18]
]
for i in range(0,11):
   total = sum(score[i])
   average = total/5
   print("Player: ", players[i], "Total Score: ", total, "Average Score: ", average)
if total > 500:
	print("Super star")