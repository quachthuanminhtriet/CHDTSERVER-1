import cloudinary.models
import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('catalog_name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('balance_mem', models.IntegerField(blank=True, null=True)),
                ('discount', models.IntegerField(blank=True, null=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('last_login_at', models.DateTimeField(blank=True, null=True)),
                ('avatar', cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='image')),
                ('gender', models.CharField(choices=[('male', 'Nam'), ('female', 'Nữ'), ('other', 'Khác'), ('secret', 'Bí Mật')], default='male', max_length=10)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('full_name', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('phone_number', models.CharField(max_length=20)),
                ('address_type', models.CharField(choices=[('Home', 'Home'), ('Work', 'Work'), ('Other', 'Other')], max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('email', models.EmailField(max_length=255)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Shipped', 'Shipped'), ('Delivered', 'Delivered'), ('Cancelled', 'Cancelled')], max_length=10)),
                ('total_price', models.IntegerField()),
                ('total_quantity', models.IntegerField()),
                ('status_ship', models.CharField(choices=[('Pending', 'Pending'), ('In Transit', 'In Transit'), ('Delivered', 'Delivered')], max_length=10)),
                ('status_payment', models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed'), ('Failed', 'Failed')], max_length=10)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chdt.address')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('product_name', models.CharField(max_length=100)),
                ('brand', models.CharField(blank=True, max_length=100, null=True)),
                ('image', models.CharField(blank=True, max_length=255, null=True)),
                ('specifications', models.TextField(blank=True, null=True)),
                ('catalog', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='chdt.catalog')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('quantity', models.IntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chdt.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chdt.product')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('storage', models.CharField(blank=True, max_length=50, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('color', models.CharField(blank=True, max_length=50, null=True)),
                ('image', models.CharField(blank=True, max_length=255, null=True)),
                ('installment', models.BooleanField(blank=True, null=True)),
                ('trade_in_sale', models.IntegerField(blank=True, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chdt.product')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('rating', models.FloatField()),
                ('review', models.TextField(blank=True, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chdt.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
