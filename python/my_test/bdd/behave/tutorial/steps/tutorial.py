from behave import *
# from minitest import *
# import logging
# logger = logging.getLogger('test')

@given('we have behave installed')
def step_impl(context):
    pass

@when('we implement a test')
def step_impl(context):
    assert True is not False

@then('behave will test it for us!')
def step_impl(context):
    assert context.failed is False

@given('a set of specific users')
def get_users(context):
    with open("test.log", "w") as the_file:
        the_file.write(str(context.table))
    # logger.info(context.table)
    # "start ...".pp()
    print(str(context.table)) 
    # enum34
    # print "end ..."
    # print 123
    # context.table.pp()
    # context.table.pp()
    # context.table.pp()
    # context.table[-1].pp()
    # context.table.pp()
    # context.table.pp()
    # context.table[0].pp()
    # context.table.pp()

@then('show something')
def show_something(context):
    # context.table.pp()
    pass

