from django.http.response import HttpResponse, HttpResponseRedirect

from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

from .models import Product, Order, OrderedProducts, WishlistProduct
from django.contrib.auth.models import User 


def add_to_wishlist(request, id):
    """
    Adds specified product to currently logged user
    """
    user = User.objects.get(pk=request.user.id)
    product = Product.objects.get(pk=id)
    WishlistProduct.objects.create(user=user, product=product)
    
    # returning a redirect --> wishilist.html page
    return HttpResponseRedirect(reverse('shop:wishlist'))

def delete_from_wishlist(request,id): 
    """
    Deletes specified wishlist product from wishlist of currently logged user 
    """

    WishlistProduct.objects.get(pk=id).delete()

    # returning a redirect --> wishilist.html page
    return HttpResponseRedirect(reverse('shop:wishlist'))

def add_to_cart(request, id):
    """
    /*--------------------------------------------------------*\
     * Adds product to 'CART' SESSION.      *
     * Avoid duplicating products in 'CART' SESSION.      *
     * 
     * Arguments: id - product id       *
    /*--------------------------------------------------------*\
    """
    
    # getting product info
    product = Product.objects.get(pk=id)

    # getting cart session
    cart = request.session.get('CART', [])

    # setting product data
    for CART_PRODUCT in cart:
        if CART_PRODUCT['id'] == str(id):
            # returning a redirect --> wishlist.html page
            return HttpResponseRedirect(reverse('shop:shop'))

    car_product = {
        "id": str(product.id),
        "name": str(product.name),
        "image": str(product.image),
        "unit_price": str(product.unit_price),
        "stock": str(product.stock),
        "amount": "1",
        "total": str(product.unit_price)
    }
    cart.append(car_product)

    # modifying the 'CART' SESSION
    request.session['CART'] = cart

    # returning a redirect --> wishilist.html page
    return HttpResponseRedirect(reverse('shop:shop'))

def update_cart(request):
    """
    /*--------------------------------------------------------*\
     * Updates product quantity in 'CART' SESSION 
    /*--------------------------------------------------------*\
    """
    
    # getting cart session
    cart = request.session.get('CART', [])

    # setting data
    for CART_PRODUCT in cart:
        CART_PRODUCT['amount'] = request.POST[f"product_{CART_PRODUCT['id']}__quantity"]
        CART_PRODUCT['total'] = int(request.POST[f"product_{CART_PRODUCT['id']}__quantity"]) *  float(CART_PRODUCT['unit_price'])

    # modifying the 'CART' SESSION
    request.session['CART'] = cart

    # returning a redirect --> wishlist.html page
    return HttpResponseRedirect(reverse('shop:cart'))

def delete_from_cart(request, id):
    """
    /*--------------------------------------------------------*\
     * Deletes product from 'CART' SESSION.      *
     * 
     * Arguments: id - product id       *
    /*--------------------------------------------------------*\
    """
    
    # getting cart session
    cart = request.session.get('CART', [])

    # setting data by removing specified product
    new_cart = [CART_PRODUCT for CART_PRODUCT in cart if CART_PRODUCT['id'] != str(id)] 

    # modifying session value
    request.session['CART'] = new_cart

    # returning a redirect --> wishilist.html page
    return HttpResponseRedirect(reverse('shop:cart'))

def user_login(request):
    """
    Logs In a User to his/her account
    """
    
    # authenticating user with given credentials
    user = authenticate(username=request.POST['username'], password=request.POST['password'])

    # checking for status whether that authentication successfull or not
    if user is not None:
        
        # loggin the user to his/her account
        login(request, user)
        # returning http request --> index.html page
        return HttpResponseRedirect(reverse('shop:index'))
    else:

        # returning http request --> index.html page
        return HttpResponseRedirect(reverse('shop:index'))

def user_logout(request):
    """
    Log Out user from his/her account
    """

    # logging user out
    logout(request)

    # returning http request --> index.html page
    return HttpResponseRedirect(reverse('shop:index'))

def user_register(request):
    """
    Register a New User to the Database
    """

    # registering the user with given info
    user = User.objects.create_user(request.POST['username'],request.POST['email'],request.POST['password'])

    # returning http request --> index.html page
    return HttpResponseRedirect(reverse('shop:index'))