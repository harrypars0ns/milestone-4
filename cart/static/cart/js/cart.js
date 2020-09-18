// Function to remove an item from the cart with a button. Sets the quantity to 0 and saves. This is for good UX 
function removeItem(buttonId){
    let clickOnButton = document.getElementById(buttonId)
    let itemId = clickOnButton.dataset.item_id
    let quantityInputElement = document.querySelector(
        `input[data-item_id="${itemId}"]`)
    quantityInputElement.value = 0;
    let form = document.querySelector(`form[data-item_id="${itemId}"]`)
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