export function usernameCheck(username){
    return RegExp("^[a-zA-z0-9_]{3,10}$").test(username);
}
export function passwordCheck(password){
    return RegExp("^[a-zA-Z0-9-_]{6,32}$").test(password) && 
    (!RegExp("^[a-zA-Z]{6,32}$").test(password)) && 
    (!RegExp("^[0-9]{6,32}$").test(password)) &&
    (!RegExp("^[_-]{6,32}$").test(password));
}

export function phoneCheck(phoneNumber){
    return RegExp("^1[0-9]{10}$").test(phoneNumber);
}
export function idCodeCheck(idcode){
    var weight_factor = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2];
    var check_code = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2'];
    var code = idcode + "";
    var last = idcode[17];
    var seventeen = code.substring(0, 17);
    var arr = seventeen.split("");
    var len = arr.length;
    var num = 0;
    for (var i = 0; i < len; i++) {
        num = num + arr[i] * weight_factor[i];
    }
    var resisue = num % 11;
    var last_no = check_code[resisue];
    var idcard_patter =
        /^[1-9][0-9]{5}([1][9][0-9]{2}|[2][0][0|1][0-9])([0][1-9]|[1][0|1|2])([0][1-9]|[1|2][0-9]|[3][0|1])[0-9]{3}([0-9]|[X])$/;
    var format = idcard_patter.test(idcode);
    return last === last_no && format ? true : false;
}
export function emailCheck(email){
    let reg= /^([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+@([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$/;
    return reg.test(email);
}

export function shopNameCheck(username){
    return RegExp("^[a-zA-z0-9_]{3,10}$").test(username);
}

export function addressCheck(address){
    // return RegExp("^[a-zA-z0-9_]{3,10}$").test(address);
    return true;
}

export function identificationIDCheck(identificationID){
    return RegExp("[0-9]*$").test(identificationID);
}

export function initialFundCheck(initialFund){
    return RegExp("[0-9]*.[0-9]*$").test(initialFund);
}

export function goodsNameCheck(goodsName){
    return RegExp("^[a-zA-z0-9_]{1,128}$").test(goodsName);
}
export function goodsDescriptionCheck(description){
    return RegExp("^.{1,128}$").test(description);
}
export function pictureCheck(pictures){
    return RegExp("^([a-zA-z]+://[^\s]*;){0,3}[a-zA-z]+://[^\s]*$").test(pictures);
}
export function priceCheck(price){
    return RegExp("^[1-9]\d*\.\d*|0\.\d*[1-9]\d*$").test(price);
}
export function stockCheck(stock){
    return RegExp("^\\+?[1-9][0-9]*$").test(stock);
}