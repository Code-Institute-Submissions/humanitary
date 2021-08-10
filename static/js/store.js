const updateCart = document.getElementsByClassName("update-cart");

// Takes information about the product the user has clicked. Used code snippets from Denis Ivy's tutorial on
// django E-commerce, although somewhat modified to fit my own needs.

for (let i = 0; i < updateCart.length; i++) {
  updateCart[i].addEventListener("click", function () {
    let productId = this.dataset.product;
    let action = this.dataset.action;
    console.log("productId:", productId, "action:", action);
    if (user === "AnonymousUser") {
      guestUserItem(productId, action);
    } else {
      updateOrder(productId, action);
    }
  });
}

// Adds cookie items to the guest user cart
function guestUserItem(productId, action) {
  console.log("User is not logged in");

  if (action == "add") {
    if (cart[productId] == undefined) {
      cart[productId] = { quantity: 1 };
    } else {
      cart[productId]["quantity"] += 1;
    }
  }
  if (action == "remove") {
    cart[productId]["quantity"] -= 1;

    if (cart[productId]["quantity"] <= 0) {
      console.log("Remove item");
      delete cart[productId];
    }
  }
  console.log("Cart", cart);
  document.cookie = "cart=" + JSON.stringify(cart) + ";domain=;path=/";
}

updateOrder = function (productId, action) {
  console.log("User is authenticated, sending data...");

  let url = "/cart/update_cart/";

  fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrftoken,
    },
    body: JSON.stringify({ productId: productId, action: action }),
  })
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      console.log("data:", data);
      location.reload();
    });
};
