#it tracks the number of reference
import sys
a=[1,2,3,4,5,6] #ref_count=2
b=a #ref_count=2+1=3
c=b #ref_count=3+1=4
d=c #ref_count=4+1=5
ref_count=sys.getrefcount(a)
print("Reference count is:",ref_count)

#
import gc #garbage collector module

collected=gc.collect()
print(f"Garbage Collector collected {collected} objects")

#
import gc
gc.enable()
#gc.disable()

l1=[1,2,3]
d1={'a':1,'b':2}
s1="Garbage collection"
del l1
del d1
del s1

gc.set_threshold(3,4,6)
print("Current Threshold is",gc.get_threshold())
collected=gc.collect()
print(f"Garbage collector collected {collected} objects")







