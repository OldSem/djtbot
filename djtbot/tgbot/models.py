from django.db import models


class CategoryClothes(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class CategoryPrice(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class User(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    id_user_in_telegram = models.IntegerField(unique=True)
    first_name = models.CharField(max_length=150, null=True)
    last_name = models.CharField(max_length=150, null=True)
    username = models.CharField(max_length=150, null=True)
    email = models.EmailField(max_length=255, null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_bot = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name


class Male(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=30)

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Country(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=30)

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class ClothesMale(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class ClothesCountry(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class ClothesPartner(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=30, unique=True)
    url = models.URLField()

    def __str__(self):
        return self.name


class Clothes(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    article_id = models.CharField(max_length=30, unique=True)
    description = models.TextField(max_length=300)
    img_center = models.ImageField(upload_to='product_top')
    img_inline = models.ImageField(upload_to='product_left')
    img_bottom = models.ImageField(upload_to='product_bottom')
    created = models.DateField(auto_now=True)
    is_active = models.BooleanField(default=True)
    price = models.PositiveSmallIntegerField()
    markup = models.PositiveSmallIntegerField()

    currency = models.ForeignKey(CategoryPrice, on_delete=models.CASCADE)
    category = models.ForeignKey(CategoryClothes, on_delete=models.CASCADE)
    partner = models.ForeignKey(ClothesPartner, on_delete=models.CASCADE)
    male = models.ForeignKey(ClothesMale, on_delete=models.CASCADE)
    country = models.ForeignKey(ClothesCountry, on_delete=models.CASCADE)

    def __str__(self):
        return self.article_id


class Basket(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    id_user_in_telegram = models.CharField(max_length=30)
    product_id = models.CharField(max_length=30)

    def __str__(self):
        return self.product_id


class SystemFoto(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=30)
    img = models.ImageField(upload_to='system_foto')

    def __str__(self):
        return self.name


class Orders(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    user_id = models.IntegerField(null=True)
    first_name = models.CharField(max_length=150, null=True)
    article_id = models.CharField(max_length=30, null=True)
    partner = models.CharField(max_length=30, null=True)
    markup = models.PositiveSmallIntegerField(null=True)
    price = models.PositiveSmallIntegerField(null=True)
    name = models.CharField(max_length=150)
    city = models.CharField(max_length=50)
    post_office = models.CharField(max_length=150)
    department = models.CharField(max_length=150)
    phone = models.CharField(max_length=30)
    size = models.CharField(max_length=30)
    tnt = models.CharField(max_length=30)
    have_ordered = models.BooleanField(default=False)
    sent = models.BooleanField(default=False)
    paid = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.article_id

