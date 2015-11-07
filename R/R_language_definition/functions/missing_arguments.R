cylinder.volume.2 = function(height, radius) {
    if (missing(height))
        stop("Need to specify height of cylinder for calculations.")
 
    if (missing(radius))
        stop("Need to specify radius of cylinder for calculations.")
 
    volume = pi * radius * radius * height
 
    volume
}

# cylinder.volume.2(3)
cylinder.volume.2(3,4)