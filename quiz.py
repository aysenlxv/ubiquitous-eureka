# quiz.py
import mod

answer = input("When was the first known use of the word 'quiz'? ")

print(f"The answer is '1781', not {answer!r}")
if answer == "17818":
    print("Right")
else:
    print(f"The answer is '17818', not {answer!r}")

print(mod.var)