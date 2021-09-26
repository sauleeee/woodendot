from rest_framework import serializers
from .models import Post, Product, Furniture, Order, Review
from django.contrib.auth.models import User


class PostSerializer(serializers.Serializer):
    def create(self, validated_data):
        post = Post.objects.create(title=validated_data('title'), body=validated_data('body'),
                                   img=validated_data('img'), category=validated_data('category'))
        return post

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.body = validated_data.get('body', instance.body)
        instance.img = validated_data.get('img', instance.img)
        instance.category = validated_data.get('category', instance.category)

    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    body = serializers.CharField()
    img = serializers.CharField()
    category = serializers.CharField(default='')


class ProductSerializer(serializers.Serializer):
    def create(self, validated_data):
        product = Product.objects.create(title=validated_data('title'), body=validated_data('body'),
                                         price=validated_data('price'), img=validated_data('img'))
        return product

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.body = validated_data.get('body', instance.body)
        instance.price = validated_data.get('price',instance.price)
        instance.img = validated_data.get('img', instance.img)

    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    body = serializers.CharField()
    price = serializers.CharField(default='')
    img = serializers.CharField()


class FurnitureSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = Furniture
        fields = ('id', 'title', 'body', 'price', 'img', 'img2', 'img3', 'body2', 'img4', 'body3', 'product')


# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'email', 'is_staff')


# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        user.save()
        return user


class OrderSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.IntegerField(write_only=True, default=1)

    class Meta:
        model = Order
        fields = ('id', 'img', 'title', 'price', 'user', 'user_id')


class ReviewSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = Review
        fields = ('id', 'firstName', 'lastName', 'text', 'product')
