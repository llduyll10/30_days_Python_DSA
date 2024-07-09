def selfLearning(subjects, x):
    subjects.sort()
    min_time =0
    for subject in subjects:
        min_time += subject * x
        if x > 1:
            x-=1
    return min_time

n,x = map(int, input().split())
subjects = list(map(int, input().split()))

result = selfLearning(subjects, x)
print(result)