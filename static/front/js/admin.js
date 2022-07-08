$( ".field-customer" ).change(function() {
    $("#id_balance").text($(this).find(":selected").text());
    
    var x = $("#id_balance").text(); 
    var x = x.slice(-10)
    var x = x.replace(/[^0-9]+/g, "");
    document.getElementById("id_balance").value = x;
 
});
$('#id_full_payment').change( function() {
    var y = document.getElementById('id_balance').value;
    var z = document.getElementById('id_full_payment').value;
    var result = parseInt(y) - parseInt(z);
    if (!isNaN(result)) {
        document.getElementById('id_balance').value = result;
        
    }
    document.getElementById("id_full_payment").reset();
    
});
// $('#id_full_payment').change(function() {
//     var y = document.getElementById("id_full_payment").value=0
//     if (isNaN(y)) y = 0;
//     var z = document.getElementById("id_balance").value
//     if (isNaN(z)) z = 0;
//     var result = z - y;
    
//     if (result == 0)
//         document.getElementById("id_full_payment").value=0
//         $('#id_balance').val(0)
// });
