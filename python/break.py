def aa(msg):
    blist = range(3)

    # this two ways, cannot change local variables
    # import code; code.interact(local=locals())
    # import IPython; IPython.embed()

    # use c to exit, and the left part will run
    import debug

    print msg

    return msg

aa("123")