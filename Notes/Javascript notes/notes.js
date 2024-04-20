 
console.log(3+2);

var myname="karan";
let a="change";
console.log(myname,a);

var product=11%3;
console.log(product)

console.log("Good night")

var mystr='<a ref="www.google.com" </a>';
console.log (mystr);
console.log (mystr.length);//to find the length 
console.log (mystr[20]);//indexing
console.log (mystr[mystr.length-1]);//last element


function hello(){
    return 10;
}
console.log(hello())

var array=[1,2,3,4,40]//array defined
console.log (array[3])//array indexing/

var def=16//global Variable

function greet(myname,message)
{
    var def=5 //Local vartiable
    console.log (def+" hello "+myname+" "+message);
    
}

greet("karan","How are you" )
console.log (def)


var outwear="Jacket"

function inner(){
    var INNER="T-Shirt"
    return INNER
}
console.log(inner());
console.log (outwear)


function nextitem(arr,item){
    arr.push(item)
    return arr.unshift(10) 
}
console.log(typeof(testar))//type is not defined

var testar=[1,2,3,4]
console.log("Before: "+JSON.stringify(testar));//JSON>stingify converts not defined type to js string acs as object
console.log(nextitem(testar,5));

console.log("After: "+JSON.stringify(testar));
console.log(typeof(testar))

function tr(isthattrue){//conditional statements
    if(isthattrue){
        return "Yes"
    }
    return "No"
}
console.log(tr(false))


//comparison operator 

function equal(val){//equal (=) operator when single = used for asignment,==used for compare int as well as string but in === it not converts string value into number so returns false
    if (val==12){
        return "equal"
    }
    return "Not equal"
}
console.log (equal(12))

// equal (=) operator when single = used for asignment,==used for compare int as well as string but in === it not converts string value into number so returns false

function sequal(val){
    if (val===12){
        return "equal"
    }
    return "Not equal"
}
console.log (sequal('12'))


console.log("card Game");

var count=0;

function cc(card){
    switch (card){
        case 1:
        case 2:
        case 3:
        case 4:
            count++;
            break;
        case "j":
        case "k":
        case "q":
        case "A":

            count--;
            break;
    }
    
    var holdbet="Hold";
    if(count>0){
        holdbet='Bet'
    }
    return count+" "+holdbet
}

cc(2);
cc('k');
cc(10);
cc("k");
cc('A')
console.log (cc(10))



//object Creation 
//Object name is mydog  the object consists key value pair comma separated like python dictionary ended with ;


var mydog={
    "Name":"Sheru",
    "legs":4, 
    "color":"Black",
    "DOM":20-10-2014
};

mydog.bark="BOW"
delete mydog.bark;
console.log (mydog)



// lookup TABLE


function lookup(val){
    result=" "
    
    var objlook={
      "Karan":"21-03-2000", 
     "Vishal":"26-01-2000",
      "Deepak":"01/04/2000",
      "Ashutosh":"31-01-2001"
    };
    result=objlook[val]
    return result;
    
    function check(prop){
    if (objlook.hasOwnobject(prop)){
        return objlook[prop]
    }
    else{
        return "Not Found"
    }
}
}

console.log (lookup("Ashutosh"))




var look={
      Karan:"21-03-2000", 
      Vishal:"26-01-2000",
      Deepak:"01/04/2000",
      Ashutosh:"31-01-2001"
    };
    
function check(prop)
    {
    if (look.hasOwnProperty(prop))
    {
        return look[prop];
    }
    else
    {       
        return "Not Found"
    }
    
    }
console.log(check("Deepak"))







//Movie Album Records

var albums ={
    
    "sufiyana":{
        year:[1999],
        actor:"abc",
        actresses:["cba","kho","ohk"]
        
    },
    "osm":{
         year:[2004],
        actor:"srk",
        actresses:["dp","as","ret"]
    },
    "mhn":{
         year:[2008],
        actor:"srk",
        actresses:[""]
    }
};

var copyalbums=JSON.parse(JSON.stringify(albums)) 


function update(id,prop,val){
    if(val===""){
        delete albums[id][prop];
        return "Not Available"
    }
    else if(prop==="actresses")
    {
        albums[id][prop]=albums[id][prop]||[]
        albums[id][prop].push(val)
    }
        else if(prop==="year")
    {
        albums[id][prop]=albums[id][prop]||[]
        albums[id][prop].push(val)
    }
    else{
        albums[id][prop]=val
    }
}

console.log (copyalbums)

update("mhn","actresses","lora")
console.log (albums)



console.log("While loop");

var myArr=[]

var i=0;
while(i<5){
    myArr.push(i);
    i++
}
console.log(myArr)

console.log("for loop");

var myArr1=[]

for(j=0;j<10;j+=2){
    myArr1.push(j);
}
console.log(myArr1)

console.log("for loop Array indexing");

var myArr3=[2,3,4,5,6]

var total=0

for (k=0;k<myArr3.length;k++){
    total+=myArr3[k]
}

console.log("total= ",total)

// project contact list

var contacts=[
        {
        name:"Ambulance",
        contact:108,
        des:"Hospital", 
        role:"Medicine"
    },
     {
        name:"Police",
        contact:100,
        des:"Police station",
        role:"Law &  order"
    },
    {
        name:"College",
        contact:5151,
        des:"Student",
        role:"Education",
    }
];


function profilelookup(name,prop){
    
    for (i=0;i<contacts.length;i++)
    if (name===contacts[i].name){
        return contacts[i] [prop]||"Not in The List"
    }
}

console.log(contacts)

console.log(profilelookup("College","role"))


"use strict";//compulsory use strict method while working with javascript


const sen="Hello" //read only  we cant modify it further
// sen=sen+"greet"//this lline throwa an error
console.log(sen)


// magic function

const magic=()=>new date;//used it as a error function no need of parenthesis 

const myconcat=(arr,arr1)=>arr.concat(arr1)//error function with parameters 

console.log(myconcat([1,2],[3,4,5]))


const increment=(function(){
    return function increment(number,value=1){
        return number+value;
};})();
console.log(increment(5,2))
console.log(increment(10))


// rest operator ...

const add=(function(){
    return function(...args){//(...args)takes all values those are passed
        return args.reduce((a,b)=>a+b,0);
    };
})();
console.log(add(1,2,4,5,6))


const avgtemps={
    today:78,
    tomorrow:85
};


function gettmpoftmrw(avgtemp){
    "use strict";
    
    const{tomorrow:tmrtmp}=avgtemp;
    return "temp of tommorrow : "+tmrtmp;
}


console.log(gettmpoftmrw(avgtemps))




// template literal

const person={
    name:"karan",
    age:22
};

//creating template

const greets=`Hello ${person.name} You are Now ${person.age} years old`

console.log(greets)