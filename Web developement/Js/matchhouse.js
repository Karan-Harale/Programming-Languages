function match(house){

    if(house<=0){
        return 0
    }
else{
    return 6*house-(house-1)
}
}
console.log(match(0))
console.log(match(4))
console.log(match(87))