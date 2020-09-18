function removeItem(buttonId){
    let clickOnButton = document.getElementById(buttonId)
    let itemId = clickOnButton.dataset.item_id
    let quantityInputElement = document.querySelector(
        `input[data-item_id="${itemId}"]`)
    quantityInputElement.value = 0;
    let form = document.querySelector(`form[data-item_id="${itemId}"]`)
    // if (clickOnButton){
    //     alert("Got Button")
    // }if (quantityInputElement){
    //     alert("Got Input")
    // }if (form){
    //     alert("Got Form")
    form.submit()  
}













// $('.remove-item').click(function(e) {
//         var csrfToken = "{{ csrf_token }}";
//         var itemId = $(this).attr('id').split('remove_')[1];
//         var url = `/cart/remove_button/${itemId}/`;
//         var data = {'csrfmiddlewaretoken': csrfToken};

//         $.post(url, data)
//          .done(function() {
//              location.reload();
//          });
//     })