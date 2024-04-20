let btn=document.querySelector('button');
let bn=document.querySelector('h1');


btn.addEventListener('click',inp);
btn.addEventListener('auxclick',nmsg);


function inp(){
   let name= prompt("Enter Your Name : ");
   if (len(name)=>0)
   { 
    bn.textContent='Namaste '+name;
   alert("Successfully Changed");
}
else
{
    alert("Enter valid Name");

}

}

function nmsg(){
    alert("Not allowed")
}
function msg(){
    alert("Succeed")
}

