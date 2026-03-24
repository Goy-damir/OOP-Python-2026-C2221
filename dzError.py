
print("введіть перше число - ")
a = int(input())
print("введіть друге число - ")
b = int(input())
res = 0

try:
    if b == 0:
        raise ZeroDivisionError
    if a < b:
        raise ValueError
    else:
        res = a / b
        print(res)

except ZeroDivisionError:
    print("не діли на ноль, гой")
except ValueError:
    print("так нізя")

### я вирішив переписати мало не з нуля. система з функцією і ключами не складна, і до того ж все робить в ручну.
### я також зберіг всі пункти Error