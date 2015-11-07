freshmen <- 1:5
sophomores <- 1:5
juniors <- 1:5
comb <- stack(list(fresh=freshmen, soph=sophomores, jrs=juniors))
print(comb)
mode(comb)
class(comb)