set.seed(1014)
df <- data.frame(replicate(6, sample(c(1:10, -99), 6, rep = TRUE)))
names(df) <- letters[1:6]
df

# df$a[df$a == -99] <- NA
# df$b[df$b == -99] <- NA
# df$c[df$c == -98] <- NA
# df$d[df$d == -99] <- NA
# df$e[df$e == -99] <- NA
# df$f[df$g == -99] <- NA

fix_missing <- function(x) {
  x[x == -99] <- NA
  x
}
# df$a <- fix_missing(df$a)
# df$b <- fix_missing(df$b)
# df$c <- fix_missing(df$c)
# df$d <- fix_missing(df$d)
# df$e <- fix_missing(df$e)
# df$f <- fix_missing(df$e)

# lapply always returns a list, but here, it seems R automatically
# transform it to data.frame
# df[] <- lapply(df, fix_missing)


missing_fixer <- function(na_value) {
  function(x) {
    x[x == na_value] <- NA
    x
  }
}
fix_missing_99 <- missing_fixer(-99)
df[] <- lapply(df, fix_missing_99)


df

summary <- function(x) {
  funs <- c(mean, median, sd, mad, IQR)
  lapply(funs, function(f) f(x, na.rm = TRUE))
}