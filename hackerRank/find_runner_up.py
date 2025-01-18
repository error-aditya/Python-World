class sports_day:
    def running(self):
        n = int(input())
        list1 = set(map(int,input().split()))
        find = list(list1)
        find.sort(reverse = True)
        return print(find[1])

sports = sports_day()
sports.running()