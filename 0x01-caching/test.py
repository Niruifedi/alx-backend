from collections import OrderedDict
test = OrderedDict(one = 1, two = 2, three = 3, four = 4, five = 5)
test[1] = "ifeanyi"
test[2] = "ifediniru"
test[3] = "izuchukwu"
test[4] = "ezechinyereugo"
test[5] = "ganganogu"

print(test.values())
test.popitem(last = True)

print(type(test))