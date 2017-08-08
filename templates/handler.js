var handler = StripeCheckout.configure({
    key: 'pk_test_6pRNASCoBOKtIshFeQd4XMUh',
    image: '/square-image.png',
    token: function(token) {
        $("#stripeToken").val(token.id);
        $("#stripeEmail").val(token.email);
        $("#myForm").submit();
    }
  });

  $('#customButton').on('click', function(e) {
    var amount = $("#amount").val() *100;
    // Open Checkout with further options
    handler.open({
      name: 'Demo Site',
      description: '2 widgets ($20.00)',
      amount: amount
    });
    e.preventDefault();
  });

  // Close Checkout on page navigation
  $(window).on('popstate', function() {
    handler.close();
  });