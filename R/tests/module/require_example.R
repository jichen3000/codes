if(require("lme4")){
    print("lme4 is loaded correctly")
} else {
    print("trying to install lme4")
    install.packages("lme4")
    if(require(lme4)){
        print("lme4 installed and loaded")
    } else {
        stop("could not install lme4")
    }
}