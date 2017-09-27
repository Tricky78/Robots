print(900 * 2 * 1.25 + 100 * 1.06)
robot_price = 900
print(robot_price * 2 * 1.25 + 100 * 1.06)
robot_quantity = 2
print(robot_price * robot_quantity * 1.25 + 100 * 1.06)
robot_vat = 1.25
print(robot_price * robot_quantity * robot_vat + 100 * 1.06)
book_price = 100
print(robot_price * robot_quantity * robot_vat + book_price * 1.06)
book_vat = 1.06
print(robot_price * robot_quantity * robot_vat + book_price * book_vat)

robot = {"price": 900, "quantity": 2, "vat": 1.25, "book_price": 100, "book_vat": 1.06}
print(robot["price"] * 2 * 1.25 + 100 * 1.06)




