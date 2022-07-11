// Event to add value of membership to Saldo
$( ".field-customer" ).change(function() {
    $("#id_balance").text($(this).find(":selected").text());
    var x = $("#id_balance").text(); 
    var x = x.slice(-10)
    var x = x.replace(/[^0-9]+/g, "");
    document.getElementById("id_balance").value = x;
 
});

// Event to add substraction of the field Saldo

$('#id_full_payment').change( function() {
    var y = document.getElementById('id_balance').value;
    var z = document.getElementById('id_full_payment').value;
    var result = parseInt(y) - parseInt(z);
    
    if (!isNaN(result)) {
        document.getElementById('id_balance').value = result;
    }
});

// Function to put . miles in field
// function numberWithCommas(x) {
//     var parts = x.toString().split(".");
//     parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ".");
//     return parts.join(".");
// }
// $('#id_full_payment').keyup(function(){
//     var x = $('#id_full_payment').val()
//     var result = numberWithCommas(x)
//     console.log(result)
//     if (!isNaN(result)) {
//         document.getElementById("id_balance").value = parseInt(result);
//     }
// });


