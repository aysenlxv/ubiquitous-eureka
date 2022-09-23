# quiz.py
import mod

answer = input("When was the first known use of the word 'quiz'? ")
if answer == "1781":
    print("Correct")
else:
    print(f"The answer is '1781', not {answer!r}")

print(mod.var)