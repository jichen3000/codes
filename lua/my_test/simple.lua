print 'a'

function s()
    return 1,2,3,4
end

function ff(func)
    return func()
end

print (ff(s))
