var myobj = (function () {
    // private members
    var name = "my, oh";

    // public part
    return {
        getName: function () {
            return name;
        }
    };
}());