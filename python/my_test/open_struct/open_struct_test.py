from ostruct import OpenStruct

if __name__ == '__main__':
    from minitest import *

    with test(OpenStruct):
        car = OpenStruct()
        car.make = 'Ford'
        car.model = 'Mustang'
        car.owner.name = 'John Doe'
        car.owner.age = 30
        car.must_equal( {
                'owner': {'age': 30, 'name': 'John Doe'}, 
                'make': 'Ford', 
                'model': 'Mustang'})

    with test("new"):
        car = OpenStruct({
                'owner': {'age': 31, 'name': 'John Doe'}, 
                'make': 'Ford', 
                'model': 'Mustang'})
        car.must_equal( {
                'owner': {'age': 31, 'name': 'John Doe'}, 
                'make': 'Ford', 
                'model': 'Mustang'})
