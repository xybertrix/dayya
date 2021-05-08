"""
/*************************************************************************************************************
* SESSOIN KEY 'CART' [TYPE --> CLASS LIST] holds products which are add into cart by the user. Session       *
* will be created at SHOP VIEW.
* ____________________________________________________________________________________________________________
*
* CONTEXT VARIABLE [TYPE --> DICTIONARY] holds data which are about to send with request to render with      *
* template engine for user. This dictionary consists of following keys.   *
* ---------------------------------------------------------------------------------------------------
* 1. page - responsible for highlight page name on header       *
* 2. products - products available for sale     *
* 3. user_products - holds the ordered products of currently logged user       *
* 4. user - holds logged in user       *
* --->setting user<---      *
*       set to 'None' if user is not authenticated or get the user info if user is authenticated.       *      
*************************************************************************************************************/
"""

from django.shortcuts import render

# models
from .models import Product, OrderedProducts, WishlistProduct, Order
from django.contrib.auth.models import User 

def index(request):
    """
    Handles view for home page --> (index.html)
    """

    # holding data which are about to send with request
    # 1. page - responsible for highlight page name on header
    # 2. user_products - holds the wishlist products of currently logged user
    # 3. user - holds logged in user
    user_products = OrderedProducts.objects.filter(order__user__pk=request.user.id)
    user = User.objects.get(pk=request.user.id) if request.user.is_authenticated else None
    context = { 'page' : 'index', 'user_products' : user_products, 'user' :  user}

    # testing
    request.session['guest_orders'] = []

    # returning http request --> index.html page
    return render(request, 'shop/index.html', context)

def shop(request):
    """
    /*------------------------------------------------------*\
     * Handles view for product shop page --> (shop.html)   *
     * ^^^^^^^ ^^^^ ^^^ ^^^^^^^ ^^^^ ^^^^
     * 
     * Controllers used in this page are, 
     * 1. add_to_cart() -> used by 'ADD TO CART' button
    \*------------------------------------------------------*/
    """

    # 'user_products' key [context dictionary]
    user_products = []
    try:
        for CART_PRODUCT in request.session['CART']:
            user_products.append(CART_PRODUCT)
    except KeyError:
        request.session['CART'] = []

    # 'user' key [context dictionary]
    user = User.objects.get(pk=request.user.id) if request.user.is_authenticated else None
    
    # context dictionary
    context = { 'page' : 'shop', 'products' : Product.objects.all(), 'user_products' : user_products, 'user': user }

    # returning http request --> shop.html page
    return render(request, 'shop/shop.html', context)

def wishlist(request):
    """
    Handles view for product wishlist page --> (wishlist.html)
    """

    # holding data which are about to send with request
    # 1. page - responsible for highlight page name on header
    # 2. page - holds the wishlist products of currently logged user
    products = WishlistProduct.objects.filter(user__pk=request.user.id)
    context = { 'page' : 'wishlist', 'products' :  products}

    # checking whether current user is authenticated or not
    if request.user.is_authenticated:

        # returning http request --> wishlist.html page
        return render(request, 'shop/wishlist.html', context)
    else:

        # returning http request --> wishlist.html page
        return render(request, 'shop/wishlist.html', context)

def cart(request):
    """
    /*------------------------------------------------------*\
     * Handles view for product cart page --> (cart.html)   *
     * ^^^^^^^ ^^^^ ^^^ ^^^^^^^ ^^^^ ^^^^
     * 
     * Controllers used in this page are,       *
     * 1. update_cart() -> used by 'UPDATE CART' button     *
     * 2. delete_from_cart() -> used by 'X' button      *
    \*------------------------------------------------------*/
    """

    # 'user_products' key [context dictionary]
    user_products = []
    try:
        for CART_PRODUCT in request.session['CART']:
            user_products.append(CART_PRODUCT)
    except KeyError:
        request.session['CART'] = []
    
    # 'user' key [context dictionary]
    user = User.objects.get(pk=request.user.id) if request.user.is_authenticated else None

    # context dictionary
    context = { 'page' : 'cart', 'user_products': user_products, 'user': user}

    # returning http request --> cart.html page
    return render(request, 'shop/cart.html', context)

def checkout(request):
    """
    /*------------------------------------------------------*\
     * Handles view for product checkout page --> (checkout.html)   *
     * ^^^^^^^ ^^^^ ^^^ ^^^^^^^ ^^^^^^^^ ^^^^
     * 
     * Controllers used in this page are,       *
     * 1. update_cart() -> used by 'UPDATE CART' button     *
    \*------------------------------------------------------*/
    """

    # 'user_products' key [context dictionary]
    user_products = []
    try:
        for CART_PRODUCT in request.session['CART']:
            user_products.append(CART_PRODUCT)
    except KeyError:
        request.session['CART'] = []

    # 'user' key [context dictionary]
    user = User.objects.get(pk=request.user.id) if request.user.is_authenticated else None
    
    # context dictionary
    context = { 'page' : 'shop', 'user_products' : user_products, 'user': user }
    
    # returning http request --> checkout.html page
    return render(request, 'shop/checkout.html', context)

def my_account(request):
    """
    Handles view for user account page --> (my-account.html)
    """

    # holding data which are about to send with request
    # 1. page - responsible for highlight page name on header
    context = { 'page' : 'my-account' }

    # returning http request --> my-account.html page
    return render(request, 'shop/my-account.html', context)

# TODO: finalizing shop page

# TODO: look page 34 from raising 404 errors
# TODO: look page 36 for removing harcoded urls
# TODO: look page for 364 for creating user
# TODO: look page for 366, 367 for authentication