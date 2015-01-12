// transfer([
//     {"name":"abc","age":5},
//     {"name":"xyz","age":20},
//     {"name":"pqr","age":60}, 
//     {"name":"efg"}]).must_equal(
//     {'kids': ['abc'], 'old': ['pqr', 'efg'], 'adults': ['xyz']})

function transfer (theList) {
    var dispatch = function (result, person) {
        theAge = person['age'] || 41;
        if (theAge <= 10){
            result['kids'].push(person['name']);
        } else if (theAge > 10 && theAge <= 40){
            result['adults'].push(person['name']);
        } else {
            result['old'].push(person['name']);
        }
        return result;
    }
    return theList.reduce(dispatch, {'kids': [], 'old': [], 'adults': []});
}


if (require.main = module){
    result = transfer([
        {"name":"abc","age":5},
        {"name":"xyz","age":20},
        {"name":"pqr","age":60}, 
        {"name":"efg"}]);
    console.log(result);
    console.log("ok");
}