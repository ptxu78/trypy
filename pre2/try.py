nums=[1,1,1,1,1,1]
ans =0
import collections
d = collections.Counter(nums)
print(d)
for k,v in d.items():
    ans += v*(v-1)/2
print(ans)