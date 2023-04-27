
function validateName(){
    var name = document.getElementById('fullname').value;
    const len = name.length;
  
    if(len >= 5) {
        document.getElementById('name-valid').style.visibility="visible";
    
    if(len <=14){
        document.getElementById('name-error').style.visibility="hidden";
    }
    if(len >= 14){
        document.getElementById('name-error').style.visibility="visible";
        document.getElementById('name-valid').style.visibility="hidden";
    }
    if(len = 0){
        window.location.href="{% url 'signup' %}"
        
    }
    
}
else{
    document.getElementById('name-error').style.visibility="hidden";
    document.getElementById('name-valid').style.visibility="hidden";
    window.location.href="{% url 'signup' %}"

}
const phone = document.getElementById('num').value;
    

if(phone.length >= 5) {
    document.getElementById('cont-valid').style.visibility="visible";

if(phone.length <=10){
    document.getElementById('cont-err').style.visibility="hidden";
}
if(phone.length >= 10){
    document.getElementById('cont-error').style.visibility="visible";
    document.getElementById('cont-valid').style.visibility="hidden";
}
if(phone.length = 0){
    window.location.href="{% url 'signup' %}"

}
}
   
else{
    document.getElementById('cont-error').style.visibility="hidden";
    document.getElementById('cont-valid').style.visibility="hidden";
    window.location.href="{% url 'signup' %}"
   



}
var passw = document.getElementById('pass1').value;
    

if(passw.length >= 5 ){
    document.getElementById('pass-valid').style.visibility="visible";

    
    
    if(passw.length <=10){
        document.getElementById('pass-error').style.visibility="hidden";
    
    }
    if(passw.length >= 10){
        document.getElementById('pass-error').style.visibility="visible";
        document.getElementById('pass-valid').style.visibility="hidden";

      
    }
    if(passw.length = 0){
        window.location.href="{% url 'signup' %}"

    }
    
}


else{
document.getElementById('pass-error').style.visibility="hidden";
document.getElementById('pass-valid').style.visibility="hidden";
window.location.href="{% url 'signup' %}"


}
const button = document.getElementById("mail");
if(button.length >= 5){
button.addEventListener("click", function () {
    const emailInput = document.querySelector('input[name="emailid"]');
    const isValidEmail = emailInput.checkValidity();
    alert(isValidEmail);
})
if(button.length = 0){
    window.location.href="{% url 'signup' %}"
}}
 else{
    window.location.href="{% url 'signup' %}"
 }

;
}






