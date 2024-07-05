from django.db import models

# Crea tus modelos aquí.

class Cliente(models.Model):
    nombre = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    direccion = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=100)
    codigo_postal = models.CharField(max_length=10)
    telefono = models.CharField(max_length=15)

    class Meta:
        verbose_name = 'cliente'
        verbose_name_plural = 'clientes'

    def __str__(self):
        return f'{self.nombre} {self.apellidos}'


class Categoria(models.Model):
    nombre = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ['nombre']
        indexes = [models.Index(fields=['nombre']),]
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    categoria = models.ForeignKey(Categoria, related_name='productos', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    imagen = models.ImageField(upload_to='productos/%Y/%m/%d', blank=True)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    disponibilidad = models.BooleanField(default=True)
    cantidad = models.IntegerField(default=0)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['nombre']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['nombre']),
            models.Index(fields=['creado']),
        ]

    def __str__(self):
        return self.nombre

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, related_name='pedidos', on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    direccion_entrega = models.CharField(max_length=250)
    ciudad_entrega = models.CharField(max_length=100)
    codigo_postal_entrega = models.CharField(max_length=10)
    pagado = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'pedido'
        verbose_name_plural = 'pedidos'

    def __str__(self):
        return f'Pedido {self.id}'

class Reseña(models.Model):
    producto = models.ForeignKey(Producto, related_name='reseñas', on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, related_name='reseñas', on_delete=models.CASCADE)
    comentario = models.TextField()
    calificacion = models.PositiveIntegerField()
    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'reseña'
        verbose_name_plural = 'reseñas'
        ordering = ['-fecha']

    def __str__(self):
        return f'Reseña de {self.cliente} para {self.producto}'