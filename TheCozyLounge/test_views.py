import pytest
from django.contrib.auth.models import User
from django.urls import reverse
from TheCozyLounge.models import Product, Order, OrderItem, ShippingAddress, Customer, AboutUs
from django.test import Client
@pytest.mark.django_db
def test_registerPage(client):
    response = client.post(reverse('register'), {
        'username': 'ENGYsaleh',
        'password1': 'testpassword123',
        'password2': 'testpassword123'
    })
    assert User.objects.filter(username='ENGYsaleh').exists()

@pytest.mark.django_db
def test_login(client):
    User.objects.create_user(username='Habiba', password='123456')
    response = client.post('/login/', {'username': 'Habiba', 'password': '123456'})


@pytest.mark.django_db
def test_search(client):
    Product.objects.create(
        a_name="John Doe",
        b_Language="English",
        b_title="ADHD",
        a_about="An inspiring story",
        b_description="About managing ADHD",
        b_genres="Health",
        b_version=1,
        b_nu_of_pages=200,
        b_price=15.99,
        b_rate=5,
        b_y_of_pub="2022-01-01",
        b_sound=False,
    )

    response = client.get('/search/?q=ADHD')

@pytest.mark.django_db
def test_logoutUser(client):
    user = User.objects.create_user(username='ENGYsaleh', password='password123')
    client.login(username='ENGYsaleh', password='password123')
    response = client.get(reverse('logout'))
@pytest.mark.django_db
def test_cart(client):
    user = User.objects.create_user(username='ENGYsaleh', password='password123')
    client.login(username='ENGYsaleh', password='password123')
    response = client.get(reverse('cart'))
    

@pytest.mark.django_db
def test_checkout(client):
    user = User.objects.create_user(username='ENGYsaleh', password='password123')
    client.login(username='ENGYsaleh', password='password123')
    response = client.get(reverse('checkout'))
@pytest.mark.django_db
def test_updateItem(client):
    # Setup: Create a user, customer, and product
    user = User.objects.create_user(username='ENGYsaleh', password='password123')
    customer = Customer.objects.create(user=user, name='ENGYsaleh', email='engysaleh@example.com')
    product = Product.objects.create(
        a_name="Sample Author",
        b_Language="English",
        b_title="Sample Book",
        a_about="A sample description",
        b_description="Detailed product description",
        b_genres="Fiction",
        b_version=1,
        b_nu_of_pages=200,
        b_price=19.99,
        b_rate=5,
        b_y_of_pub="2022-05-01",
        b_sound=False
    )

    # Login user
    client.login(username='ENGYsaleh', password='password123')

    response = client.post(
        reverse('update_item'),
        data={'productId': product.id, 'action': 'add'},
        content_type='application/json'
    )


    order = Order.objects.filter(customer=customer, complete=False).first()
    assert order is not None, "Order should be created"
    order_item = OrderItem.objects.filter(order=order, product=product).first()
    assert order_item is not None, "OrderItem should be created"
    assert order_item.quantity == 1, "OrderItem quantity should be 1"
    assert response.json() == 'Item was added'

@pytest.mark.django_db
def test_about_us(client):
    user = User.objects.create_user(username='ENGYsaleh', password='password123')
    client.login(username='ENGYsaleh', password='password123')
    response = client.get(reverse('about_us'))
@pytest.mark.django_db
def test_details_view(client):
    # Setup: Create a product
    product = Product.objects.create(
        a_name="Sample Author",
        b_Language="English",
        b_title="Sample Book",
        a_about="A sample description",
        b_description="Detailed product description",
        b_genres="Fiction",
        b_version=1,
        b_nu_of_pages=200,
        b_price=19.99,
        b_rate=5,
        b_y_of_pub="2022-05-01",
        b_sound=False
    )

    response = client.get(reverse('view', args=[product.id]))    

