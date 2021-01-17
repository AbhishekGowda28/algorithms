from math import floor

def problem13():
    limit = 10
    longestChain = 0
    number = 1
    requiredNumber = 0
    while longestChain < limit:
        interMediate = number
        intermediateLongChain = 1
        while interMediate != 1:
            intermediateLongChain+=1
            if interMediate % 2 == 0:
                interMediate = floor(interMediate/2)
            else:
                interMediate = floor((3*interMediate)+1)
        if intermediateLongChain > longestChain:
            longestChain = intermediateLongChain
            requiredNumber = number
        limit-=1
        number+=1
    return (requiredNumber, longestChain)


print(problem13())