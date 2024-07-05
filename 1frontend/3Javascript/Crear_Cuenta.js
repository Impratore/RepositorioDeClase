document.getElementById('registroForm').addEventListener('submit', function(event) {
    event.preventDefault();

    let nombre = document.getElementById('nombre').value;
    let apellido = document.getElementById('apellido').value;
    let correo = document.getElementById('correo').value;
    let direccion = document.getElementById('direccion').value;
    let ciudad = document.getElementById('ciudad').value;
    let codigo_postal = document.getElementById('codigo_postal').value;
    let telefono = document.getElementById('telefono').value;
    let contra = document.getElementById('contra').value;
    let confi_contra = document.getElementById('confi_contra').value;

    if (contra !== confi_contra) {
        alert('Las contraseñas no coinciden');
        return;
    }

    let datosCliente = {
        nombre: nombre,
        apellidos: apellido,
        email: correo,
        direccion: direccion,
        ciudad: ciudad,
        codigo_postal: codigo_postal,
        telefono: telefono,
    };

    fetch('/api/registrar/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(datosCliente),
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
        alert('Usuario registrado con éxito');
    })
    .catch((error) => {
        console.error('Error:', error);
        alert('Error al registrar el usuario');
    });
});
