let carts = document.querySelectorAll('.Add to cart');

for (let i = 0; i < carts.length; i++) {
    carts[i].addEventListener('click', () => {
        console.log("added to cart")
    })

}