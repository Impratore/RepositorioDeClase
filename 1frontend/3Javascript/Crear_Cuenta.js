document.getElementById('registro-form').addEventListener('submit', function(event) {
    event.preventDefault();

    const nombre = document.getElementById('nombre').value;
    const apellido = document.getElementById('apellido').value;
    const correo = document.getElementById('correo').value;
    const direccion = document.getElementById('direccion').value;
    const ciudad = document.getElementById('ciudad').value;
    const codigo_postal = document.getElementById('codigo_postal').value;
    const telefono = document.getElementById('telefono').value;

    const datos = {
        nombre: nombre,
        apellidos: apellido,
        email: correo,
        direccion: direccion,
        ciudad: ciudad,
        codigo_postal: codigo_postal,
        telefono: telefono
    };

    fetch('http://127.0.0.1:8000/api/registrar/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(datos)
    })
    .then(response => response.json())
    .then(data => {
        const mensajeDiv = document.getElementById('mensaje');
        if (data.success) {
            mensajeDiv.textContent = 'Usuario registrado exitosamente.';
            mensajeDiv.style.color = 'green';
        } else {
            mensajeDiv.textContent = 'Error al registrar el usuario.';
            mensajeDiv.style.color = 'red';
        }
    })
    .catch(error => {
        const mensajeDiv = document.getElementById('mensaje');
        mensajeDiv.textContent = 'Error al registrar el usuario.';
        mensajeDiv.style.color = 'red';
        console.error('Error:', error);
    });
});
