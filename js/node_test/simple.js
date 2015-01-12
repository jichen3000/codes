if (require.main === module) {
    var mm="中文";
    console.log(mm);

    var array = ['a', 'b', 'c'];

    for (var i in array) {
      console.log(array[i]);
    }
    console.dir({name:mm})
    console.log({name:mm})
}

